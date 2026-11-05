#!/usr/bin/env python3
"""Finite checks for the completed masked preparations.

This script compares three independently organized descriptions:
  (i) local GHZ growth, streamed/local X-mask trajectories, boundary coins;
 (ii) composition of the corresponding CPTP twirling channels;
(iii) the uniform orthogonal cat-sector mixture.

It checks the actual final density matrices, including entropy, root fidelity,
ordinary Gram entries, local charged correlations, and negative controls.
It does not infer an asymptotic theorem from small systems.

Run:
    python verification/constructions_check.py
"""

from __future__ import annotations

import hashlib
import itertools
import json
import platform
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


ATOL = 2e-10
ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "constructions_check.json"
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PLUS = np.ones(2, dtype=complex) / np.sqrt(2)
FUSION = (np.eye(4, dtype=complex) + 1j * np.kron(Z, Y)) / np.sqrt(2)


def popcount(x: int) -> int:
    return int(x).bit_count()


def parity(x: int) -> int:
    return popcount(x) & 1


def gf2_basis(vectors: list[int]) -> list[int]:
    """Independent integer bit-vectors, with elimination separate from spectra."""
    pivots: dict[int, int] = {}
    for original in vectors:
        v = int(original)
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return [pivots[p] for p in sorted(pivots)]


def gf2_span(vectors: list[int]) -> list[int]:
    span = [0]
    for v in gf2_basis(vectors):
        span += [x ^ v for x in span]
    return sorted(span)


def block(sites: list[int], edges: list[tuple[int, int]] | None = None) -> dict:
    if edges is None:
        edges = list(zip(sites[:-1], sites[1:]))
    root = sites[0]
    children = {i: [] for i in sites}
    for a, b in edges:
        children[a].append(b)
    depth = {root: 0}
    queue = deque([root])
    while queue:
        a = queue.popleft()
        for b in children[a]:
            assert b not in depth
            depth[b] = depth[a] + 1
            queue.append(b)
    assert set(depth) == set(sites)
    assert len(edges) == len(sites) - 1
    return {
        "sites": sites,
        "root": root,
        "edges": edges,
        "children": children,
        "depth": depth,
        "height": max(depth.values()),
        "mask": sum(1 << i for i in sites),
    }


def greedy_edge_colors(edges: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    colors: list[list[tuple[int, int]]] = []
    occupied: list[set[int]] = []
    for e in edges:
        for k, used in enumerate(occupied):
            if e[0] not in used and e[1] not in used:
                colors[k].append(e)
                used.update(e)
                break
        else:
            colors.append([e])
            occupied.append(set(e))
    for color in colors:
        endpoints = [v for e in color for v in e]
        assert len(endpoints) == len(set(endpoints))
    return colors


def apply_two_site(psi: np.ndarray, u: np.ndarray, a: int, b: int) -> np.ndarray:
    """Site i is bit i (least significant first); u uses basis |a,b>."""
    out = psi.copy()
    ma, mb = 1 << a, 1 << b
    for base in range(len(psi)):
        if base & (ma | mb):
            continue
        ix = [base, base | mb, base | ma, base | ma | mb]
        out[ix] = u @ psi[ix]
    return out


def apply_x(psi: np.ndarray, site: int) -> np.ndarray:
    return psi[np.arange(len(psi)) ^ (1 << site)]


def z_signs(n: int, mask: int) -> np.ndarray:
    return np.array([1 - 2 * parity(i & mask) for i in range(1 << n)])


def ghz_circuit(n: int, blocks: list[dict]) -> np.ndarray:
    psi = np.ones(1 << n, dtype=complex) / np.sqrt(1 << n)
    for b in blocks:
        for a, child in sorted(b["edges"], key=lambda e: b["depth"][e[1]]):
            psi = apply_two_site(psi, FUSION, a, child)
    return psi


def cat_product(n: int, blocks: list[dict], u: int, epsilon: int) -> np.ndarray:
    """Closed form, independent of the GHZ growth gate implementation."""
    psi = np.zeros(1 << n, dtype=complex)
    for orientation in range(1 << len(blocks)):
        basis_index = u
        for j, b in enumerate(blocks):
            if orientation & (1 << j):
                basis_index ^= b["mask"]
        psi[basis_index] = (1 - 2 * parity(orientation & epsilon)) / np.sqrt(
            1 << len(blocks)
        )
    return psi


def strict_group(b: dict, labels: list[int], r: int) -> dict:
    return {"sites": b["sites"], "labels": labels, "r": r, "tree": b}


def shared_group(n: int, labels: list[int], r: int) -> dict:
    return {"sites": list(range(n)), "labels": labels, "r": r, "tree": None}


def label_dict(group: dict) -> dict[int, int]:
    return dict(zip(group["sites"], group["labels"]))


def stream_events(group: dict, seed: int) -> tuple[list[int], dict]:
    """Simulate the two-buffer schedule, returning actual local X flips.

    Source preparation, edge copies, reset and buffer exchange are scheduled
    locally. The expected linear mask is checked independently afterward.
    """
    b, r = group["tree"], group["r"]
    assert b is not None
    sites, root = b["sites"], b["root"]
    labels = label_dict(group)
    current = {i: 0 for i in sites}
    nxt = {i: 0 for i in sites}
    flips: list[int] = []
    transmissions = controls = resets = swaps = 0
    colors = greedy_edge_colors(b["edges"])
    if r == 0:
        return [], {
            "rounds": 0,
            "height": b["height"],
            "source_bits": 0,
            "transmissions": 0,
            "controlled_x_gates": 0,
            "resets": 0,
            "buffer_swaps": 0,
            "edge_colors": len(colors),
            "max_buffers_per_site": 2,
        }
    for t in range(b["height"] + r):
        assert current[root] == 0
        if t < r:
            current[root] = (seed >> t) & 1
        for i in sites:
            j = t - b["depth"][i]
            active = 0 <= j < r
            expected_bit = ((seed >> j) & 1) if active else 0
            assert current[i] == expected_bit
            if active and ((labels[i] >> j) & 1):
                controls += 1
                if current[i]:
                    flips.append(i)
        for color in colors:
            for a, child in color:
                j = t - b["depth"][a]
                if 0 <= j < r:
                    assert nxt[child] == 0
                    nxt[child] ^= current[a]
                    transmissions += 1
        for i in sites:
            if 0 <= t - b["depth"][i] < r:
                resets += 1
            current[i] = 0
        for i in sites:
            arriving_index = t + 1 - b["depth"][i]
            if i != root and 0 <= arriving_index < r:
                current[i], nxt[i] = nxt[i], current[i]
                swaps += 1
            else:
                assert nxt[i] == 0
    assert not any(current.values()) and not any(nxt.values())
    actual_mask = 0
    for i in flips:
        actual_mask ^= 1 << i
    expected_mask = sum(
        (parity(labels[i] & seed) << i) for i in sites
    )
    assert actual_mask == expected_mask
    assert transmissions == (len(sites) - 1) * r
    assert controls == sum(popcount(a) for a in group["labels"])
    assert resets == len(sites) * r
    assert swaps == (len(sites) - 1) * r
    return flips, {
        "rounds": b["height"] + r,
        "height": b["height"],
        "source_bits": r,
        "transmissions": transmissions,
        "controlled_x_gates": controls,
        "resets": resets,
        "buffer_swaps": swaps,
        "edge_colors": len(colors),
        "max_buffers_per_site": 2,
    }


def mask_generators(groups: list[dict]) -> list[int]:
    generators = []
    for g in groups:
        for j in range(g["r"]):
            generators.append(
                sum(
                    (1 << i)
                    for i, a in zip(g["sites"], g["labels"])
                    if (a >> j) & 1
                )
            )
    return generators


def canonicalize(raw: int, blocks: list[dict]) -> int:
    u = raw
    for b in blocks:
        if raw & (1 << b["root"]):
            u ^= b["mask"]
    return u


def phase_generators(blocks: list[dict], boundary: list[tuple[int, int]]) -> list[int]:
    owner = {i: j for j, b in enumerate(blocks) for i in b["sites"]}
    return [(1 << owner[a]) ^ (1 << owner[b]) for a, b in boundary]


def trajectory_density(case: dict) -> tuple[np.ndarray, dict]:
    n, blocks, groups, boundary = (
        case["n"], case["blocks"], case["groups"], case["boundary"]
    )
    psi0 = ghz_circuit(n, blocks)
    reference = cat_product(n, blocks, 0, 0)
    ghz_error = float(np.linalg.norm(psi0 - reference))
    assert ghz_error < ATOL
    rho = np.zeros((1 << n, 1 << n), dtype=complex)
    seed_ranges = [range(1 << g["r"]) for g in groups]
    total_branches = 1 << (sum(g["r"] for g in groups) + len(boundary))
    phase_signs = [z_signs(n, (1 << a) | (1 << b)) for a, b in boundary]
    resources = []
    for g in groups:
        if g["tree"] is not None:
            _, stats = stream_events(g, 0)
            resources.append(stats)
    for seeds in itertools.product(*seed_ranges):
        psi_masked = psi0.copy()
        for g, seed in zip(groups, seeds):
            if g["tree"] is not None:
                flips, _ = stream_events(g, seed)
            else:
                flips = [
                    i for i, a in zip(g["sites"], g["labels"])
                    if parity(a & seed)
                ]
            for i in flips:
                psi_masked = apply_x(psi_masked, i)
        for coins in range(1 << len(boundary)):
            psi = psi_masked.copy()
            for j, signs in enumerate(phase_signs):
                if coins & (1 << j):
                    psi *= signs
            rho += np.outer(psi, psi.conj()) / total_branches
    return rho, {
        "trajectory_branches": total_branches,
        "ghz_gate_to_cat_vector_residual": ghz_error,
        "strict_streams": resources,
    }


def channel_density(case: dict, reversed_order: bool = False) -> np.ndarray:
    n, groups, boundary = case["n"], case["groups"], case["boundary"]
    psi = ghz_circuit(n, case["blocks"])
    rho = np.outer(psi, psi.conj())
    index = np.arange(1 << n)

    def masks(a: np.ndarray) -> np.ndarray:
        for generator in mask_generators(groups):
            permutation = index ^ generator
            a = (a + a[np.ix_(permutation, permutation)]) / 2
        return a

    def phases(a: np.ndarray) -> np.ndarray:
        for u, v in boundary:
            signs = z_signs(n, (1 << u) | (1 << v))
            a = (a + signs[:, None] * a * signs[None, :]) / 2
        return a

    return masks(phases(rho)) if reversed_order else phases(masks(rho))


def closed_density(case: dict) -> tuple[np.ndarray, dict]:
    n, blocks = case["n"], case["blocks"]
    u_generators = [
        canonicalize(g, blocks) for g in mask_generators(case["groups"])
    ]
    e_generators = phase_generators(blocks, case["boundary"])
    patterns, phases = gf2_span(u_generators), gf2_span(e_generators)
    rho = np.zeros((1 << n, 1 << n), dtype=complex)
    for u in patterns:
        for epsilon in phases:
            psi = cat_product(n, blocks, u, epsilon)
            rho += np.outer(psi, psi.conj()) / (len(patterns) * len(phases))
    return rho, {
        "mask_image_rank": len(gf2_basis(u_generators)),
        "boundary_incidence_rank": len(gf2_basis(e_generators)),
        "predicted_state_rank": len(patterns) * len(phases),
        "predicted_entropy_bits": float(
            len(gf2_basis(u_generators)) + len(gf2_basis(e_generators))
        ),
        "raw_seed_bits": sum(g["r"] for g in case["groups"]),
        "independent_boundary_coins": len(case["boundary"]),
    }


def pauli_expectation(rho: np.ndarray, xmask: int, zmask: int) -> complex:
    """P = i^(number of Y) X^x Z^z, a Hermitian tensor Pauli."""
    n = len(rho).bit_length() - 1
    indices = np.arange(len(rho))
    phase = (1j) ** popcount(xmask & zmask)
    return phase * np.sum(rho[indices, indices ^ xmask] * z_signs(n, zmask))


def pauli_string(n: int, xmask: int, zmask: int) -> str:
    lookup = {(0, 0): "I", (1, 0): "X", (0, 1): "Z", (1, 1): "Y"}
    return "".join(lookup[((xmask >> i) & 1, (zmask >> i) & 1)] for i in range(n))


def charged_local_paulis(n: int, max_interval: int) -> list[tuple[int, int]]:
    strings = set()
    # The numerical local geometry in this diagnostic is the index-order chain.
    # It is used only to enumerate bounded support, independently of block trees.
    for length in range(1, max_interval + 1):
        for start in range(n - length + 1):
            for digits in itertools.product(range(4), repeat=length):
                xmask = zmask = 0
                for offset, digit in enumerate(digits):
                    i = start + offset
                    if digit in (1, 3):
                        xmask |= 1 << i
                    if digit in (2, 3):
                        zmask |= 1 << i
                if parity(zmask):
                    strings.add((xmask, zmask))
    return sorted(strings)


def local_charged_diagnostic(rho: np.ndarray, max_interval: int) -> dict:
    n = len(rho).bit_length() - 1
    strings = charged_local_paulis(n, max_interval)
    cache: dict[tuple[int, int], complex] = {}
    maximum = 0.0
    witness = None
    pairs = 0
    for p_index, (xp, zp) in enumerate(strings):
        for xq, zq in strings[p_index + 1:]:
            if (xp | zp) & (xq | zq):
                continue
            pairs += 1
            key = (xp ^ xq, zp ^ zq)
            if key not in cache:
                cache[key] = pauli_expectation(rho, *key)
            value = cache[key]
            if abs(value) > maximum:
                maximum = float(abs(value))
                witness = {
                    "operator_a": pauli_string(n, xp, zp),
                    "operator_b": pauli_string(n, xq, zq),
                    "correlation_real": float(value.real),
                    "correlation_imag": float(value.imag),
                }
    one_point = max(
        (float(abs(pauli_expectation(rho, x, z))) for x, z in strings),
        default=0.0,
    )
    return {
        "support_family": f"subsets of index-chain intervals of at most {max_interval} sites",
        "charged_pauli_count": len(strings),
        "disjoint_pairs_checked": pairs,
        "distinct_products_evaluated": len(cache),
        "max_absolute_one_point": one_point,
        "max_absolute_two_point": maximum,
        "largest_correlation_witness": witness,
    }


def metrics(rho: np.ndarray, case: dict) -> dict:
    n, dim = case["n"], len(rho)
    evals, vectors = np.linalg.eigh((rho + rho.conj().T) / 2)
    positive = evals[evals > ATOL]
    # All examples have flat nonzero spectra >= 1/128. Remove only numerical
    # null-space eigenvalues before taking the square root; otherwise roundoff
    # in an exact zero becomes a spurious O(sqrt(machine epsilon)) fidelity.
    sqrt_rho = (vectors * np.sqrt(np.where(evals > ATOL, evals, 0))) @ vectors.conj().T
    entropy = float(-np.sum(positive * np.log2(positive)))
    gram = np.eye(n)
    fidelity = np.eye(n)
    invariance_error = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            signs = z_signs(n, (1 << i) | (1 << j))
            gram[i, j] = gram[j, i] = float(
                np.dot(np.diag(rho).real, signs)
            )
            # Hermitian trace norm form of root fidelity.
            a = (sqrt_rho * signs[None, :]) @ sqrt_rho
            f = float(np.sum(np.abs(np.linalg.eigvalsh((a + a.conj().T) / 2))))
            fidelity[i, j] = fidelity[j, i] = f
            changed = signs[:, None] * rho * signs[None, :]
            invariance_error = max(
                invariance_error, float(np.linalg.norm(changed - rho, "fro"))
            )
    one_fidelity = []
    for i in range(n):
        a = (sqrt_rho * z_signs(n, 1 << i)[None, :]) @ sqrt_rho
        one_fidelity.append(
            float(np.sum(np.abs(np.linalg.eigvalsh((a + a.conj().T) / 2))))
        )
    flip = np.arange(dim) ^ (dim - 1)
    strong_residual = float(np.linalg.norm(rho[flip, :] - rho, "fro"))
    upper = np.triu_indices(n, 1)
    return {
        "trace_real": float(np.trace(rho).real),
        "hermiticity_frobenius_residual": float(np.linalg.norm(rho - rho.conj().T)),
        "minimum_eigenvalue": float(evals.min()),
        "numerical_rank": len(positive),
        "entropy_bits": entropy,
        "purity": float(np.trace(rho @ rho).real),
        "nonzero_eigenvalue_min": float(positive.min()),
        "nonzero_eigenvalue_max": float(positive.max()),
        "strong_Q_plus_frobenius_residual": strong_residual,
        "ordinary_gram": gram.tolist(),
        "ordinary_gram_to_identity_frobenius_residual": float(np.linalg.norm(gram - np.eye(n))),
        "max_off_diagonal_ordinary_ZZ": float(np.max(np.abs(gram[upper]))),
        "pair_root_fidelity_matrix": fidelity.tolist(),
        "pair_root_fidelity_min": float(np.min(fidelity[upper])),
        "pair_root_fidelity_max": float(np.max(fidelity[upper])),
        "max_pair_Z_conjugation_frobenius_residual": invariance_error,
        "single_Z_root_fidelity_max": max(one_fidelity),
        "local_charged": local_charged_diagnostic(rho, case.get("charged_interval", 1)),
    }


def mask_constraint_check(case: dict) -> dict | None:
    mode = case.get("growing")
    if mode is None:
        return None
    n = case["n"]
    max_interval = case["charged_interval"]
    local = charged_local_paulis(n, max_interval)
    z_products = set()
    for j, (xa, za) in enumerate(local):
        for xb, zb in local[j + 1:]:
            if not ((xa | za) & (xb | zb)):
                z_products.add(za ^ zb)
    failed = 0
    for zmask in z_products:
        # An independent group with nonzero label XOR suffices to kill the term.
        killed = False
        for g in case["groups"]:
            total = 0
            for i, a in zip(g["sites"], g["labels"]):
                if zmask & (1 << i):
                    total ^= a
            killed |= total != 0
        if not killed:
            failed += 1
    assert failed == 0
    return {
        "mode": mode,
        "distinct_local_charged_pair_YZ_constraints": len(z_products),
        "failed_constraints": failed,
    }


def make_cases() -> list[dict]:
    seven = [block([0, 1, 2]), block([3, 4, 5, 6])]
    eight = [
        block([0, 1, 4, 5], [(0, 1), (0, 4), (1, 5)]),
        block([2, 3, 6, 7], [(2, 3), (2, 6), (3, 7)]),
    ]
    strict7 = [
        strict_group(seven[0], [0, 1, 2], 2),
        strict_group(seven[1], [0, 1, 2, 3], 2),
    ]
    strict8 = [strict_group(b, [0, 1, 2, 3], 2) for b in eight]
    reused7 = [0, 1, 2, 0, 1, 2, 3]
    reused8 = [0] * 8
    for b in eight:
        for i, label in zip(b["sites"], [0, 1, 2, 3]):
            reused8[i] = label
    singleton = [block([i]) for i in range(4)]
    cases = [
        {
            "name": "strict_unequal_blocks_7",
            "n": 7, "blocks": seven, "groups": strict7, "boundary": [(2, 3)],
            "model": "strict_product", "charged_interval": 3,
        },
        {
            "name": "shared_reused_labels_7",
            "n": 7, "blocks": seven,
            "groups": [shared_group(7, reused7, 2)], "boundary": [(2, 3)],
            "model": "preshared_classical", "charged_interval": 3,
        },
        {
            "name": "strict_branched_blocks_8",
            "n": 8, "blocks": eight, "groups": strict8, "boundary": [(1, 2)],
            "model": "strict_product", "charged_interval": 3,
        },
        {
            "name": "shared_global_labels_8",
            "n": 8, "blocks": eight,
            "groups": [shared_group(8, list(range(8)), 3)], "boundary": [(1, 2)],
            "model": "preshared_classical", "charged_interval": 3,
        },
        {
            "name": "shared_reused_labels_8",
            "n": 8, "blocks": eight,
            "groups": [shared_group(8, reused8, 2)], "boundary": [(1, 2)],
            "model": "preshared_classical", "charged_interval": 3,
        },
        {
            "name": "strict_growing_support_masks_8",
            "n": 8, "blocks": eight,
            "groups": [strict_group(b, [1, 2, 4, 8], 4) for b in eight],
            "boundary": [(1, 2)], "model": "strict_product",
            "charged_interval": 3, "growing": "independent_full_rank_block_labels",
        },
        {
            "name": "shared_growing_support_masks_8",
            "n": 8, "blocks": eight,
            "groups": [shared_group(8, [1, 2, 4, 8, 16, 32, 64, 127], 7)],
            "boundary": [(1, 2)], "model": "preshared_classical",
            "charged_interval": 3, "growing": "only_label_dependency_uses_all_eight_sites",
        },
        {
            "name": "strict_single_block_6",
            "n": 6, "blocks": [block(list(range(6)))],
            "groups": [strict_group(block(list(range(6))), list(range(6)), 3)],
            "boundary": [], "model": "strict_product", "charged_interval": 3,
        },
        {
            "name": "singleton_blocks_4",
            "n": 4, "blocks": singleton,
            "groups": [strict_group(b, [0], 0) for b in singleton],
            "boundary": [(0, 1), (1, 2), (2, 3)],
            "model": "strict_product", "charged_interval": 1,
        },
        {
            "name": "negative_control_no_masks_8",
            "n": 8, "blocks": eight, "groups": [], "boundary": [(1, 2)],
            "model": "negative_control", "charged_interval": 1,
            "negative": "ordinary_gram_fails",
        },
        {
            "name": "negative_control_missing_boundary_8",
            "n": 8, "blocks": eight, "groups": strict8, "boundary": [],
            "model": "negative_control", "charged_interval": 1,
            "negative": "cross_block_fidelity_fails",
        },
    ]
    return cases


def main() -> None:
    if not __debug__:
        raise RuntimeError("Run without -O: the finite checks use assertions.")
    q2 = np.kron(X, X)
    fusion_checks = {
        "unitarity_residual": float(np.linalg.norm(FUSION.conj().T @ FUSION - np.eye(4))),
        "XX_commutator_residual": float(np.linalg.norm(FUSION @ q2 - q2 @ FUSION)),
        "copy_zero_residual": float(np.linalg.norm(FUSION @ np.kron([1, 0], PLUS) - [1, 0, 0, 0])),
        "copy_one_residual": float(np.linalg.norm(FUSION @ np.kron([0, 1], PLUS) - [0, 0, 0, 1])),
    }
    assert max(fusion_checks.values()) < ATOL
    results = []
    densities = {}
    for case in make_cases():
        rho, implementation = trajectory_density(case)
        closed, prediction = closed_density(case)
        channel = channel_density(case)
        reverse = channel_density(case, reversed_order=True)
        comparisons = {
            "trajectory_to_cat_sector_frobenius_residual": float(np.linalg.norm(rho - closed)),
            "trajectory_to_channel_composition_frobenius_residual": float(np.linalg.norm(rho - channel)),
            "mask_boundary_order_frobenius_residual": float(np.linalg.norm(channel - reverse)),
        }
        assert max(comparisons.values()) < ATOL
        observed = metrics(rho, case)
        assert abs(observed["trace_real"] - 1) < ATOL
        assert observed["minimum_eigenvalue"] > -ATOL
        assert observed["numerical_rank"] == prediction["predicted_state_rank"]
        assert abs(observed["entropy_bits"] - prediction["predicted_entropy_bits"]) < ATOL
        assert abs(observed["purity"] - 1 / prediction["predicted_state_rank"]) < ATOL
        assert observed["strong_Q_plus_frobenius_residual"] < ATOL
        assert observed["single_Z_root_fidelity_max"] < ATOL
        assert observed["local_charged"]["max_absolute_one_point"] < ATOL
        if case.get("negative") != "ordinary_gram_fails":
            assert observed["ordinary_gram_to_identity_frobenius_residual"] < ATOL
        else:
            assert observed["max_off_diagonal_ordinary_ZZ"] > 0.99
        if case.get("negative") != "cross_block_fidelity_fails":
            assert abs(observed["pair_root_fidelity_min"] - 1) < ATOL
            assert observed["max_pair_Z_conjugation_frobenius_residual"] < ATOL
        else:
            assert observed["pair_root_fidelity_min"] < ATOL
        if case.get("growing"):
            assert observed["local_charged"]["max_absolute_two_point"] < ATOL
        result = {
            "name": case["name"],
            "model": case["model"],
            "n": case["n"],
            "block_sites": [b["sites"] for b in case["blocks"]],
            "block_tree_edges": [b["edges"] for b in case["blocks"]],
            "boundary_edges": case["boundary"],
            "mask_groups": [
                {"sites": g["sites"], "row_labels": g["labels"], "seed_bits": g["r"]}
                for g in case["groups"]
            ],
            "negative_control": case.get("negative"),
            "exact_prediction": prediction,
            "implementation": implementation,
            "representation_comparisons": comparisons,
            "mask_constraints": mask_constraint_check(case),
            "observed": observed,
            "all_case_assertions_passed": True,
        }
        results.append(result)
        densities[case["name"]] = rho
        print(
            f"{case['name']}: S={observed['entropy_bits']:.12g}, "
            f"rank={observed['numerical_rank']}, "
            f"min pair root F={observed['pair_root_fidelity_min']:.12g}",
            flush=True,
        )
    global_reused_residual = float(
        np.linalg.norm(densities["shared_global_labels_8"] - densities["shared_reused_labels_8"])
    )
    assert global_reused_residual < ATOL
    baseline_higher = next(
        r for r in results if r["name"] == "strict_single_block_6"
    )["observed"]["local_charged"]["max_absolute_two_point"]
    assert baseline_higher > 0.99
    payload = {
        "schema": "mixed-state-order-entropy-construction-checks-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "finite final masked states; analytic proofs are in science/constructions.md",
        "fidelity_convention": "root fidelity; for Hermitian G, ||sqrt(rho) G sqrt(rho)||_1",
        "entropy_units": "bits",
        "qubit_index_convention": "site i is computational-basis bit i, least significant first",
        "local_charged_check_convention": (
            "all Pauli strings odd under product X, supported within an index-chain interval "
            "of the recorded length; all pairs with disjoint actual supports"
        ),
        "numerical_tolerance": ATOL,
        "square_root_null_space_cutoff": ATOL,
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fusion_checks": fusion_checks,
        "shared_global_and_reused_label_density_residual": global_reused_residual,
        "unrepaired_Hadamard_higher_local_charged_correlation_detected": baseline_higher,
        "cases": results,
        "all_assertions_passed": True,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"Wrote {OUTPUT}", flush=True)


if __name__ == "__main__":
    main()
