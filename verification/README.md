# Finite construction checks

The script checks the **final masked density matrices** of the preparations in
[Matching local preparations](../science/constructions.md). It verifies finite
instances of both preparation models and includes controls that deliberately
violate one of the target promises.

The rank, entropy, locality, asymptotic depth, and growing-support statements are
proved on the construction page. The computations here check arithmetic and
implementation details on small systems; they do not establish those general
statements by extrapolation.

## Reproduce

Run from the repository root with Python 3.12 and NumPy:

```bash
python -m pip install -r verification/requirements.txt
python verification/constructions_check.py
```

The recorded environment uses Python 3.12.14 and NumPy 2.3.5. The script writes
[`constructions_check.json`](constructions_check.json) next to itself, prints one
summary per case, and fails on any violated assertion. Do not use Python's
`-O` option, which disables assertions; the script rejects that mode.

The JSON includes the actual run time in UTC, software versions, the script's
SHA-256, all block trees and mask labels, exact rank predictions, numerical
observations, and the conventions listed below. Rerunning replaces that result
file. There is no random sampling in the finite checks: all specified seed and
boundary-coin branches are averaged.

## Three descriptions of each state

Each final state is computed in three ways.

1. **Local circuit trajectories.** The data start in a product of plus states.
   The two-site fusion gate grows each GHZ block. For the strict model, an
   explicit two-buffer schedule moves every seed bit down its local tree and
   applies the corresponding local controlled-X operations. The shared model
   starts from the specified preloaded classical mask law. Independent
   boundary coins are then applied, and all branches are averaged.
2. **Channel composition.** Each binary mask generator and each boundary
   operator is applied as a two-Kraus twirling channel. The reverse order of
   mask and boundary channels is also evaluated.
3. **Cat-sector formula.** Binary linear algebra computes the canonical mask
   image and boundary incidence image. A density matrix is built from the
   resulting orthogonal cat projectors, independently of the fusion-gate and
   stream implementations.

The script compares the resulting matrices and checks their numerical spectra
against the separate binary-rank prediction. It also checks:

- the fusion gate's unitarity, symmetry, and two copying identities;
- trace, positivity, flat nonzero spectrum, entropy, and purity;
- exact global plus-charge support;
- every ordinary two-site ZZ expectation;
- every pair root fidelity and every single-Z root fidelity;
- local charged Pauli correlations on the support family specified below;
- stream arrival times, two-buffer use, edge-color conflicts, and exact
  transmission, controlled-X, reset, and swap counts.

The stream simulator follows classical registers after their source
preparations. This is exact for the stated classical-coin implementation. It
does not construct the entire data-plus-apparatus density matrix or optimize
the circuit depth.

## Cases and recorded results

All 11 case assertions passed in the recorded run. The nine intended
construction cases have the identity ordinary ZZ Gram matrix and pair root
fidelity one to numerical tolerance. The two controls show the expected
failure of one promise.

| Case | Qubits | Entropy in bits | Rank | Diagnostic |
|---|---:|---:|---:|---|
| Strict masks, unequal blocks | 7 | 5 | 32 | Independent block seeds |
| Shared masks, unequal blocks | 7 | 3 | 8 | Reused labels and one common seed |
| Strict masks, branched trees | 8 | 5 | 32 | Local fan-out and pipelined buffers |
| Shared global labels | 8 | 3 | 8 | Canonical rank is smaller than raw seed size |
| Shared reused labels | 8 | 3 | 8 | Same final density matrix as the preceding row |
| Strict local-support repair | 8 | 7 | 128 | All tested charged correlations vanish |
| Shared local-support repair | 8 | 6 | 64 | All tested charged correlations vanish |
| One strict block | 6 | 3 | 8 | Unrepaired higher charged correlation detected |
| Singleton blocks | 4 | 3 | 8 | Boundary incidence rank is three |
| Control: remove masks | 8 | 1 | 2 | Ordinary within-block ZZ correlation is one |
| Control: remove boundary channel | 8 | 4 | 16 | Cross-block root fidelity is zero |

The shared global-label and reused-label eight-site states coincide exactly in
the recorded floating-point arrays. Their canonical mask rank is two, although
the global-label implementation supplies three raw seed bits. This checks why
the exact entropy depends on the canonical image rank, rather than on the
number of supplied random bits.

The unrepaired six-site Hadamard mask retains a charged one-site/three-site
correlation of magnitude one. This is a deliberate diagnostic: the ordinary
ZZ promise alone does not remove all higher local charged order. Both repaired
eight-site examples have zero for every tested charged pair.

## Conventions and limits

**Fidelity.** The script uses root fidelity. For a Hermitian unitary `G`, it
computes the trace norm of `sqrt(rho) @ G @ sqrt(rho)`. It does not square this
quantity.

**Numerical null space.** The absolute assertion tolerance is `2e-10`.
Eigenvalues below that value are set to zero when forming the matrix square
root. The smallest genuine nonzero eigenvalue in these cases is `1/128`, so
the cutoff is separated from the populated spectrum. The cutoff prevents
square roots of numerical null-space noise from producing spurious
single-Z fidelities.

**Qubit ordering.** Site `i` is bit `i` of the computational-basis integer,
with the least significant bit first. Each JSON case records its actual
block and boundary graph.

**Local charged support family.** For each case, the script enumerates all
Pauli strings odd under the global product-X charge whose actual supports
fit inside an interval of the recorded length in the site-index chain. It
tests every pair with disjoint actual supports. The containing intervals
may overlap. The length is three for the repaired cases, giving 152 charged
strings and 5,280 disjoint pairs per eight-site case. Some preparation trees
are branched; their graph is distinct from this index-chain diagnostic
support family. No claim that those intervals exhaust all balls of a
higher-dimensional lattice is made.

The script also checks the zero-XOR mask constraints for the repaired finite
examples directly. These fixed small tables illustrate the analytic repair;
they are not a numerical demonstration of its asymptotic logarithmic seed
size.

**Scope.** The check uses four, six, seven, and eight qubits. It is an exact
branch enumeration followed by floating-point matrix arithmetic. It is not a
formal proof, a large-system simulation, a hardware noise model, a test of the
continuous-time bounds, or a resource estimate for preparing the shared
classical seed from a local product apparatus. The shared seed is an explicit
input resource in that model.
