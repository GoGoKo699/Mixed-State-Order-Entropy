# Watrous and the bridge to mixed-state order

[Milestone map](milestones.md) · [Worked example](worked_example.md) · [Scientific account](../science/README.md)

The starting task is concrete: prepare a lattice of spins using local operations, discard the apparatus, and ask how much entropy must remain in the spins if they retain global fidelity order. Understanding the answer requires both quantum information and a careful account of where the preparation's classical correlations came from.

John Watrous's textbook supplies the finite-dimensional language of states, channels, fidelity, and entropy. The project then adds spatial preparation constraints, symmetry-sector information, and matching constructions. The [30-milestone map](milestones.md) organizes that scientific story. The sections below are targeted reference points, rather than a requirement to read the whole book first.

## Selected source and version

**John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018.**

Use the author's [book page](https://cs.uwaterloo.ca/~watrous/TQI/) and its **standard-layout chapter PDFs**. This is the sole educational anchor. The author's freely readable manuscript is a pre-publication version, with a January 2018 preface; the published book appeared in 2018. Section and theorem numbers below were checked against that manuscript. The [front matter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) gives its contents and version notice. Page references below mean printed page numbers, not a PDF viewer's page counter.

The author also provides [errata dated June 21, 2021](https://cs.uwaterloo.ca/~watrous/TQI/TQI.errata.pdf). Those errata distinguish the published text from additional typographical issues in the manuscript. The repository links to the author's files rather than reproducing the book.

The book is a mathematical reference for the foundations. Its chapter order is not the project's milestone order, and the research papers cited in the scientific account are proof dependencies and attribution, not additional educational anchors.

## Targeted sections

The middle column describes what to extract for this project; it is not a list of additional prerequisites.

| Verified location | Useful content | Connection to the project |
|---|---|---|
| [Sections 1.1.1–1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) | Tensor products, adjoints, spectral decompositions, and matrix norms | Read density matrices and the trace norm; understand why $`AA^\dagger`$ and $`A^\dagger A`$ have the same nonzero eigenvalues. |
| [Section 1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) | Finite probability distributions and expectations | Distinguish independent local coins from one correlated classical seed. |
| [Sections 2.1.1–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Registers, density operators, reduced states, and purification | Define the retained output, discarded apparatus, and the auxiliary purifier used in entropy proofs. |
| [Sections 2.2.1–2.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Quantum channels and their representations | Model local gates, randomization, and discard. Section 2.2.2 includes complete positivity in Theorem 2.22 and the trace-preservation conditions in Theorem 2.26. |
| [Sections 2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Measurement probabilities and ensembles | Relate a joint spin measurement to a classical law without replacing the quantum state by that law. |
| [Sections 3.2.1–3.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Fidelity and its purification and channel properties | Use Definition 3.11, Theorem 3.22, Corollary 3.26, and Theorem 3.27 in the entropy arguments. |
| [Section 4.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) | Mixtures of unitary channels and pinching | Recognize a random Pauli operation and a binary twirl as ordinary channels with discarded records. |
| [Sections 5.1.1–5.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Shannon entropy and its basic relations | Count independent fair labels and define binary entropy. |
| [Sections 5.2.1–5.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Quantum entropy, subadditivity, continuity, and data processing | Translate spectral entropy into a lower bound; separate a valid dimension-dependent continuity estimate from the stronger continuity input needed later. |
| [Section 5.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Classical labels encoded in quantum states | Use the Holevo quantity, particularly Eq. (5.260), while distinguishing it from accessible measurement information. |
| [Section 6.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) | Product states and convex mixtures of product states | Understand how an initially separable resource may still contain shared classical correlations. Spatial preparation cost requires further assumptions. |

For locating the central statements quickly: the manuscript defines root fidelity on p. 139; Uhlmann's theorem is Theorem 3.22 on p. 151; joint concavity and channel monotonicity appear in Section 3.2.3 on pp. 155–156. Entropy subadditivity is Theorem 5.24 on p. 270, relative-entropy data processing is Theorem 5.35 on p. 280, and the Holevo quantity is developed in Section 5.3.3, with Eq. (5.260) on p. 297. These identify the statements used, rather than suggesting that every result in those sections is needed.

## Notation and assumption bridge

| Watrous's convention | Convention in this repository | What to keep distinct |
|---|---|---|
| A vector $`u`$ and its projector $`uu^*`$ | $`\lvert\psi\rangle`$ and $`\lvert\psi\rangle\langle\psi\rvert`$ | The star in the book is the adjoint, written $`\dagger`$ here. A state vector and a density operator are different objects. |
| A complex Euclidean space $`\mathcal X`$ and $`\mathrm D(\mathcal X)`$ | A finite-dimensional Hilbert space and a density matrix $`\rho`$ | The site's Pauli $`X_i`$ is an operator, not the book's register or space name. |
| $`H(\rho)`$ for quantum entropy | $`S(\rho)=-\mathrm{Tr}(\rho\log_2\rho)`$ | This repository reserves $`H(P)`$ for a classical probability law. Both use bits. |
| $`F(\rho,\sigma)=\lVert\sqrt\rho\sqrt\sigma\rVert_1`$ | The same root fidelity | No squaring is needed when translating from this anchor. Some research papers use the squared convention. |
| An ensemble $`\eta(a)=p(a)\rho_a`$ | The pair $`\{p(a),\rho_a\}`$ | The book can package a probability into a subnormalized operator; the individual $`\rho_a`$ here is normalized. |
| $`\mathrm C(\mathcal X,\mathcal Y)`$, a set of channels | A preparation channel $`\Phi`$, with depth $`D`$ | The project's $`C`$ is instead the ordinary correlation matrix. |
| An unrestricted finite channel or purification | A local physical preparation, or an auxiliary mathematical purification | Existence of a dilation or a purifier does not establish a local implementation or its depth. |

The physical state has $`N=L^d`$ retained spins. The spatial dimension is $`d`$, and the circuit depth is $`D`$. Define

```math
Q=\prod_{i=1}^N X_i,\qquad
C_{ij}=\mathrm{Tr}(\rho Z_iZ_j),\qquad
f_{ij}=F(\rho,Z_iZ_j\rho Z_iZ_j).
```

The project imposes three different conditions:

- $`Q\rho=\rho`$ fixes the support to the plus-charge sector. Mere invariance $`Q\rho Q=\rho`$ permits a mixture of sectors and is weaker.
- $`C\preceq\kappa I`$, with fixed $`\kappa`$, controls the entire ordinary correlation matrix. Small individual entries alone do not give this uniform spectral bound.
- $`f_{ij}\ge c>0`$ compares the original **global** state with a pair-conjugated global state. It is not an ordinary expectation value and does not describe a fidelity between two-site marginals.

These are the [model's promises](../science/model.md), not assumptions built into the textbook's definitions. Likewise, a shared classical seed and a product initial apparatus belong to different resource classes. Averaging product states conditioned on a seed need not produce an unconditionally product state.

The entropy cost is always the entropy of the actual retained density matrix after records are discarded. It is not the entropy of one convenient preparation log, the entropy conditioned on knowing a seed, or a heat cost. The [worked example](worked_example.md) shows these distinctions with explicit matrices.

## From the anchor to the project

### A binary information step

Take two states $`\alpha,\beta`$ with equal prior probabilities. Their Holevo information is

```math
\chi(\alpha,\beta)
=S((\alpha+\beta)/2)-\frac{S(\alpha)+S(\beta)}2.
```

Uhlmann's theorem permits purifications whose overlap equals the root fidelity. The equal mixture of those two pure states has eigenvalues $`(1\pm F(\alpha,\beta))/2`$. Discarding the purifying register cannot increase the Holevo quantity, so

```math
\chi(\alpha,\beta)
\le h_2((1+F(\alpha,\beta))/2),
```

where $`h_2(p)=-p\log_2p-(1-p)\log_2(1-p)`$. This connects the book's fidelity and entropy machinery. The inequality itself is an inherited research ingredient, attributed in [Proposition E1](../science/entropy_bounds.md#proposition-e1-binary-holevo-information-from-fidelity); it is not a new theorem about two states.

### From one bit to an orbit

The project organizes a family of unitarily related states by binary labels. Joint concavity controls the two average states at each split of the label tree. Adding the binary information costs bounds the full ensemble's Holevo information. A purification then turns overlaps between orbit vectors into a Gram matrix. Subadditivity converts the entropy of that Gram matrix into a lower bound on $`S(\rho)`$.

The precise arguments are [Proposition E2 and Theorem E3](../science/entropy_bounds.md#proposition-e2-binary-tree-holevo-bound). The purifier is a proof device. Its preparation is not an uncharged physical step in the protocol.

### From an orbit to spatial preparation

This is where the model changes the conclusion. In a product-resource circuit, sufficiently separated output regions have disjoint backward causal cones and factor exactly. Their orbit Gram matrices therefore tensorize, allowing entropy contributions from many regions to add. With a preshared classical seed, only conditional factorization is automatic. The shared-classical proof instead uses strong symmetry in every positive-weight branch to establish a uniform classical measurement law.

Neither implication follows from the definition of a channel alone. They are established in [Circuit bounds](../science/circuit_bounds.md). The matching upper examples require an additional constructive argument: create coherent blocks, randomize their relative charge signs, and choose masks whose distinguishable patterns have controlled rank. [Constructions](../science/constructions.md) proves the spectrum and counts signal propagation, gates, and workspace.

### From exact cones to finite propagation speed

For continuous time, distant regions are generally only approximately independent. The proof therefore needs a local propagation estimate, a controlled cut of interactions around a region, and an entropy estimate that remains useful while conditioning on a large distant system.

The project's local fingerprint register has dimension equal to the number of selected sites in a box. Applying conditional entropy continuity to that register costs a logarithm of the site count. Applying an ordinary continuity estimate directly to the full physical spin space would pay a much larger dimension factor and does not establish the claimed result. The separate [continuous-time proof](../science/continuous_time.md) supplies the required argument and its Hamiltonian-apparatus assumptions.

## Research-level dependencies

The textbook provides the vocabulary and standard information inequalities. The following additional steps remain part of the scientific proof:

| Step beyond the anchor | Where the complete account is supplied |
|---|---|
| The inherited binary Holevo–fidelity inequality and its attribution | [Entropy bounds, E1](../science/entropy_bounds.md#proposition-e1-binary-holevo-information-from-fidelity), citing Roga, Fannes, and Życzkowski |
| Spatially amplified orbits and the distinct shared-seed converse | [Circuit bounds](../science/circuit_bounds.md) |
| Exact cat-sector spectrum, classical masks, and local schedules | [Constructions](../science/constructions.md), including attribution to the classical independence constructions |
| Lieb–Robinson propagation, shell cuts, and conditional entropy continuity | [Continuous-time bounds](../science/continuous_time.md), using the primary Barthel–Kliesch and Winter results identified there |
| Sharp support assumptions, leakage corrections, and failures of qualitative clustering | [Scope and robustness](../science/scope_and_robustness.md) |
| Interpretation of global fidelity order and comparison with neighboring results | [Interpretation](../science/interpretation.md) and [Related work](../references/related_work.md) |

These are directed links into the proof, not a second textbook list. In particular, familiarity with states and entropy does not replace the spatial or continuity arguments. The complete story is the relation between a specified preparation resource, an actual retained state, and a matching upper and lower entropy law.
