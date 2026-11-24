# Mixed-State Order and Entropy

**How much mixedness must a many-body state retain when global fidelity order is prepared in a limited local time?**

This repository gives matching bounds on the retained entropy of strongly symmetric spin states with global fidelity order. Independent local apparatus pays a logarithmic entropy cost in each causal volume. A common seed reuses the same random bits across volumes, and the entropy of that seed determines how much of the cost it removes.

## Main result

Consider $`N=L^d`$ qubits in fixed spatial dimension $`d`$, with global charge $`Q=\prod_iX_i`$. The actual output satisfies

```math
Q\rho=\rho,\qquad
F(\rho,Z_iZ_j\rho Z_iZ_j)\ge c\gt 0\quad(i\ne j),
\qquad
C\preceq\kappa I,\quad C_{ij}=\mathrm{Tr}(\rho Z_iZ_j).
```

Here $`F`$ is **root Uhlmann fidelity**, and $`c,\kappa`$ are fixed independently of size and depth. Entropy is in bits. The condition on $`C`$ includes exact zero ordinary pair correlations and uniform summable clustering. Qualitative decay alone is insufficient.

For depth $`D`$ local-channel circuits, write $`\ell_D=\min\{L,D+1\}`$, $`V=\ell_D^d`$, and $`K=N/V`$. Let $`h`$ be the budget on the Shannon entropy of a common seed supplied before preparation. At **unit pair fidelity** the [finite-budget theorem](science/shared_seed_budget.md) gives

```math
S_{\min}(h)=\Theta_{d,\kappa}\!\left[
K+\log_2 N+K[\log_2 V-h]_+\right].
```

The law is uniform in $`h\ge 0`$ at depth $`D\ge 2`$ in the nearest-neighbor two-site circuit model, for sufficiently large lattices. A shared seed of about $`\log_2 V`$ bits removes the additional logarithmic cost across causal volumes. At depth zero, unit fidelity requires $`N-1`$ shared bits. The [small-depth bounds](science/shared_seed_budget.md#feasibility-at-depths-zero-and-one) detail feasibility.

At any fixed positive threshold $`c`$, the two [endpoint laws](science/circuit_bounds.md) are

```math
S_{\min}^{\mathrm{prod}}(N,D)
=\Theta_{d,c,\kappa}\!\left[
\frac{N}{\ell_D^d}\log_2(\ell_D+1)\right],
```

```math
S_{\min}^{\mathrm{shared}}(N,D)
=\Theta_{d,c,\kappa}\!\left[
\frac{N}{\ell_D^d}+\log_2N\right].
```

At imperfect fidelity, the finite-budget bounds determine the logarithmic scale of the seed budget, with the leading coefficient unresolved. Both endpoint laws saturate at order $`\log N`$ at diameter depth. An unlimited shared seed allows depth-zero preparation.

| Initial resources | Meaning of the preparation model | Entropy scale before the diameter cap |
|---|---|---|
| Product system and apparatus | Independent local inputs and random sources; any runtime broadcast is charged | $`N\log(D+2)/(D+1)^d`$ |
| Shared classical randomness | A classical variable can select local inputs and controls before the clock starts; no nonlocal quantum input or instantaneous runtime feedback | $`N/(D+1)^d+\log N`$ |

The same [finite-budget law](science/shared_seed_budget.md) holds in continuous time with the diameter-capped propagation volume of the [bounded-generator model](science/continuous_time.md). Matching preparations use local Hamiltonians, local apparatus, and a final discard. The explicit on-site apparatus can grow logarithmically with block size.

## Mechanism and matching preparations

At unit fidelity the state is diagonal in the even-cat basis, so the joint $`Z`$ readout measures its entropy up to one bit. The Gram bound forces many distinguishable outcomes in each causal volume. Conditioning on the common seed removes at most $`h`$ bits from each block's marginal entropy, and separated blocks are independent given the seed. At imperfect fidelity, a purified orbit and the Holevo–fidelity inequality replace the exact readout identity. In continuous time a local shell cut bounds the conditioning error from distant blocks.

The upper construction prepares coherent cat states in blocks, mixes their relative charge signs using local boundary channels, and applies low-entropy classical masks. Its spectrum is known exactly:

```math
S(\rho)=p-1+\mathrm{rank}_{\mathbb F_2}(TA),
```

Here $`p`$ is the number of preparation blocks and $`TA`$ describes their distinguishable mask patterns. Sharing the first mask coordinates and generating the rest within each block attains the finite-budget law. Each operation preserves strong symmetry. The [endpoint constructions](science/constructions.md) also provide masks that suppress correlations of general local charged observables.

The contribution is the matched physical preparation frontier and its dependence on initial classical coordination. Fidelity order, the information inequalities, classical small sample spaces, and Lieb–Robinson propagation are credited in the [related-work account](references/related_work.md).

## Read the scientific account

| Question | Authoritative page |
|---|---|
| What exactly is optimized? | [Model and assumptions](science/model.md) |
| How much shared randomness reduces the entropy cost? | [Finite-budget theorem](science/shared_seed_budget.md) |
| Why is there a global logarithmic entropy floor? | [Information and orbit bounds](science/entropy_bounds.md) |
| How do locality and shared randomness change the answer? | [Circuit bounds](science/circuit_bounds.md) |
| Which states attain the bounds, and what resources prepare them? | [Matching constructions](science/constructions.md) |
| Does the logarithmic factor survive continuous time? | [Continuous-time bounds](science/continuous_time.md) |
| Which assumptions are necessary, and what noise is covered? | [Scope and robustness](science/scope_and_robustness.md) |
| What is the physical consequence? | [Interpretation](science/interpretation.md) |
| Which ingredients are inherited? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

Start with the [science reading guide](science/README.md) for a connected route. The [LLM guide](llms.txt) identifies authoritative files and claim boundaries.

## Learn the argument

The [learning guide](learning/README.md) connects John Watrous's *The Theory of Quantum Information* (2018) to this problem. The [anchor and bridge](learning/anchor.md) identifies the relevant sections, translates notation, and separates textbook foundations from the locality arguments supplied here.

The [30-milestone map](learning/milestones.md) moves from states and channels to the preparation frontier. The [worked block example](learning/worked_example.md) shows how the shared seed and block-charge signs contribute to the final spectrum.

## Reproduce the finite checks

The [verification guide](verification/README.md) explains the numerical conventions, dependencies, checked systems, and negative controls. From the repository root:

    python3 -m pip install -r verification/requirements.txt
    python3 verification/constructions_check.py

The checks compare complete final masked density matrices obtained from local circuit trajectories, channel composition, and the independent cat-sector formula. They examine entropy, rank, charge, ordinary correlations, root fidelity, and selected charged-operator correlations. The general bounds and resource schedules are analytical proofs; small-system checks do not certify their asymptotics.

## Scope

This is a finite-system theorem for the stated **global** fidelity diagnostic. It does not identify global fidelity with every local or infinite-volume formulation of strong-to-weak symmetry breaking. In particular, uniformly vanishing pair correlations can coexist with only $`O(\log\log N)`$ entropy when the Gram norm is allowed to grow. The [counterexamples](science/scope_and_robustness.md) explain this boundary and the separate role of exact charge support in the shared-classical converse.

The optimized quantity is retained-state mixedness. Heat, work, irreversible entropy production, and an arbitrary fixed trace-distance preparation error require additional assumptions. The constants are not optimized as the fidelity threshold tends to zero.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
