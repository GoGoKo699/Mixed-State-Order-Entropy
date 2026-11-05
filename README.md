# Mixed-State Order and Entropy

**How much mixedness must a many-body state retain when global fidelity order is prepared in a limited local time?**

This repository gives matching upper and lower bounds on the final von Neumann entropy of strongly symmetric qubit states with nonzero global pair fidelity and a uniformly bounded ordinary correlation matrix. The answer depends on the initial classical resources: independent local apparatus pays a logarithmic entropy cost in each causal volume; a preshared classical seed can coordinate those costs.

## Main result

Consider $N=L^d$ qubits in fixed spatial dimension $d$, with global charge $Q=\prod_iX_i$. The actual output satisfies

$$
Q\rho=\rho,\qquad
F(\rho,Z_iZ_j\rho Z_iZ_j)\ge c>0\quad(i\ne j),
\qquad
C\preceq\kappa I,\quad C_{ij}=\operatorname{Tr}(\rho Z_iZ_j).
$$

Here $F$ is **root Uhlmann fidelity**, and $c,\kappa$ are fixed independently of size and depth. Entropy is in bits. The condition on $C$ includes exact zero ordinary pair correlations and uniform summable clustering. Qualitative decay alone is insufficient.

For depth $D$ local-channel circuits, set $\ell_D=\min\{L,D+1\}$. The minimum possible retained entropy obeys

$$
S_{\min}^{\mathrm{prod}}(N,D)
=\Theta_{d,c,\kappa}\!\left[
\frac{N}{\ell_D^d}\log_2(\ell_D+1)\right],
$$

$$
S_{\min}^{\mathrm{shared}}(N,D)
=\Theta_{d,c,\kappa}\!\left[
\frac{N}{\ell_D^d}+\log_2N\right].
$$

The constants also absorb the fixed local gate range. The product-input statement holds above a fixed feasibility threshold; the nearest-neighbor two-site model has a depth-two baseline. The shared-classical model is feasible at depth zero. Both laws hold uniformly for sufficiently large systems and saturate at order $\log N$ at diameter depth. The proof pages give finite-size bounds and the small-depth exceptions.

| Initial resources | Meaning of the preparation model | Entropy scale before the diameter cap |
|---|---|---|
| Product system and apparatus | Independent local inputs and random sources; any runtime broadcast is charged | $N\log(D+2)/(D+1)^d$ |
| Shared classical randomness | A classical variable can select local inputs and controls before the clock starts; no nonlocal quantum input or instantaneous runtime feedback | $N/(D+1)^d+\log N$ |

The [continuous-time theorem](science/continuous_time.md) gives the corresponding bounds for finite-range generators with uniformly bounded strength and overlap. Matching preparations use local Hamiltonians, explicit local apparatus, and a final discard. Their on-site apparatus can grow logarithmically with block size. Exact matching within a fixed-dimensional, system-only Markovian model is a separate question.

## Mechanism and matching preparations

The lower bound combines an inherited binary Holevo–fidelity inequality with a spatial family of purified unitary orbits. A correlation-matrix norm bound supplies entropy in each orbit label. Product initial resources make sufficiently separated circuit regions independent, so the local logarithmic costs add. For continuous time, local fingerprint registers and conditional-entropy continuity retain this addition despite Lieb–Robinson tails.

The upper construction prepares coherent cat states in blocks, mixes their relative charge signs using local boundary channels, and applies low-entropy classical masks. Its spectrum is known exactly:

$$
S(\rho)=K-1+\operatorname{rank}_{\mathbb F_2}(TA),
$$

where $K$ is the block count and $TA$ records distinguishable mask patterns after blockwise complement symmetry is removed. Independent block seeds and one reused shared seed give the two matching entropy laws. Strong symmetry is maintained at every preparation step. A stronger mask also removes correlations of arbitrary fixed-support charged observables without changing the asymptotic costs.

The contribution is the matched physical preparation frontier and its dependence on initial classical coordination. Fidelity order, the information inequalities, classical small sample spaces, and Lieb–Robinson propagation are credited in the [related-work account](references/related_work.md).

## Read the scientific account

| Question | Authoritative page |
|---|---|
| What exactly is optimized? | [Model and assumptions](science/model.md) |
| Why is there a global logarithmic entropy floor? | [Information and orbit bounds](science/entropy_bounds.md) |
| How do locality and shared randomness change the answer? | [Circuit bounds](science/circuit_bounds.md) |
| Which states attain the bounds, and what resources prepare them? | [Matching constructions](science/constructions.md) |
| Does the logarithmic factor survive continuous time? | [Continuous-time bounds](science/continuous_time.md) |
| Which assumptions are necessary, and what noise is covered? | [Scope and robustness](science/scope_and_robustness.md) |
| What is the physical consequence? | [Interpretation](science/interpretation.md) |
| Which ingredients are inherited? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

Start with the [science reading guide](science/README.md) for a connected route. The [LLM guide](llms.txt) identifies authoritative files and claim boundaries.

## Reproduce the finite checks

The [verification guide](verification/README.md) explains the numerical conventions, dependencies, checked systems, and negative controls. From the repository root:

    python3 -m pip install -r verification/requirements.txt
    python3 verification/constructions_check.py

The checks compare complete final masked density matrices obtained from local circuit trajectories, channel composition, and the independent cat-sector formula. They examine entropy, rank, charge, ordinary correlations, root fidelity, and selected charged-operator correlations. The general bounds and resource schedules are analytical proofs; small-system checks do not certify their asymptotics.

## Scope

This is a finite-system theorem for the stated **global** fidelity diagnostic. It does not identify global fidelity with every local or infinite-volume formulation of strong-to-weak symmetry breaking. In particular, uniformly vanishing pair correlations can coexist with only $O(\log\log N)$ entropy when the Gram norm is allowed to grow. The [counterexamples](science/scope_and_robustness.md) explain this boundary and the separate role of exact charge support in the shared-classical converse.

The optimized quantity is retained-state mixedness. Heat, work, irreversible entropy production, and an arbitrary fixed trace-distance preparation error require additional assumptions. The constants are not optimized as the fidelity threshold tends to zero.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
