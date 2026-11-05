# Related work and attribution

The contribution is a pair of **matching retained-entropy versus local-preparation frontiers**, together with the distinction between product apparatus and preshared classical coordination. This page separates that result from the information inequalities, order diagnostics, and classical constructions it uses.

The comparison below was checked against primary sources on 5 November 2026. Version identifiers identify the inspected scientific account; a preprint is not described as a published result unless journal metadata is verified. The [structured bibliography](references.bib) records the same source identities.

## Information-theoretic ingredients

The educational foundation is [John Watrous, *The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/). The [selected-source bridge](../learning/anchor.md) identifies the relevant states, channels, fidelity, and entropy material. This textbook role is separate from attribution of the research ingredients below.

| Source | Established ingredient used here | Relationship to this project |
|---|---|---|
| [Roga, Fannes, and Życzkowski (2010)](https://arxiv.org/abs/1004.4782), PRL 105, 040505, Eq. (26) | An upper bound on binary Holevo information in terms of fidelity | The binary step of the [orbit proof](../science/entropy_bounds.md). Their squared-fidelity convention is converted to root fidelity. This inequality is inherited. |
| [Nayak (1999), v3](https://arxiv.org/abs/quant-ph/9904093v3), Section 4.4 | Entropy bounds for quantum random-access encodings | Provides an alternative information-theoretic viewpoint on learning many parity bits from a purification. The main proof uses binary twirls and orbits directly. |
| [Babai (2013)](https://people.cs.uchicago.edu/~laci/papers/13augEntropy.pdf) and [Gavinsky–Pudlák, v4](https://arxiv.org/abs/1503.08154) | Entropy lower bounds and small sample spaces for pairwise or higher independence; Hadamard constructions | The classical endpoint and logarithmic mask seeds are established antecedents. The static logarithmic scale is not claimed as an unprecedented information principle. |
| [Barthel–Kliesch (2012), v2](https://arxiv.org/abs/1111.4210v2), Theorem 1 and Eq. (12) | A Lieb–Robinson bound for finite-range local Markovian generators, with a smaller-support prefactor | Supplies the local propagation estimate in the [shell-cut argument](../science/continuous_time.md). The proof here uses it against one box and an arbitrarily large distant union. |
| [Winter (2016), v6](https://arxiv.org/abs/1507.07775v6), Lemmas 1–2 | Marginal and conditional entropy continuity with a dimension cost only for the first register in the latter | Applied to local fingerprint registers of dimension equal to the site count in a box. The inherited continuity estimate, combined with this representation, preserves the logarithmic spatial gain. |

Purification, Uhlmann's theorem, fidelity data processing and joint concavity, Gram spectral identities, entropy subadditivity, commuting binary twirls, finite-field incidence rank, and pipelined tree broadcast are standard ingredients. Their derivations or precise uses are included where needed. The exact output spectrum and the physical accounting connect these ingredients to the optimization rather than creating new classical code families.

## Global fidelity order and purification

**Lessa et al., PRX Quantum 6, 010344 (2025), [arXiv:2405.03639v3](https://arxiv.org/abs/2405.03639v3).** This establishes global fidelity as an SWSSB diagnostic, its stability under symmetric low-depth local channels, and its connection to irrecoverability. The present work uses that order framework and asks a different optimization: how small the actual retained entropy can be at a bounded depth or time under a uniform ordinary-Gram bound. Stability of an order diagnostic alone does not give either matching entropy law.

**Sala, Gopalakrishnan, Oshikawa, and You, PRB 110, 155150 (2024), [arXiv:2405.02402](https://arxiv.org/abs/2405.02402), Section IV.B.** The purification account relates fidelity to optimized environmental observables and correlations. That interpretation is inherited. This repository's preparation dependence comes from packing independent or approximately independent spatial regions and proving matching apparatus constructions.

**Moharramipour et al., PRX Quantum 5, 040336 (2024), [arXiv:2406.08542v2](https://arxiv.org/abs/2406.08542v2), especially Section VII.** The authors analyze entanglement in maximally mixed symmetry sectors and derive preparation restrictions, including for continuous non-Abelian symmetries. Their spatial entanglement measures and prescribed sector states differ from minimizing total retained von Neumann entropy over the bounded-Gram global-fidelity class. This is a close preparation precedent, not evidence that symmetry-based preparation bounds first arise here.

## General mixed-state preparation bounds

**McGinley–Garratt, [arXiv:2510.02275v1](https://arxiv.org/abs/2510.02275), Theorems 1–2 and Supplement S2.** Their lower bounds compare a subsystem's information about a distant subsystem with its information about a purifier. The model permits ensembles of local circuits and, in the supplement, local ancillas. Shared classical correlations are therefore already explicit in their framework. The present target instead fixes global pair fidelity and ordinary Gram norm, optimizes retained entropy, and separates strict product apparatus from the shared-classical class. Their stated bounds do not supply the matched spatial logarithmic amplification and its two constructions.

**Westhoff, Murciano, and Moroder, [arXiv:2610.13784v1](https://arxiv.org/abs/2610.13784v1).** This gives locality–relaxation-time relations for quadratic fermionic dissipative preparation by optimizing jump-operator localization at fixed target. Its resource variable and dynamical class differ from the retained-entropy optimization here. In particular, the Hamiltonian-apparatus upper bound in this repository is not a claim about an exact system-only steady-state relaxation protocol.

## Local diagnostics and infinite volume

The word “order” requires care because different modern definitions use different observables and limits.

| Source inspected | Relevant distinction |
|---|---|
| [Liu, Yi, and Else, arXiv:2605.28925v3](https://arxiv.org/abs/2605.28925v3) | Develops a local description of strong symmetry and an infinite-volume formulation. The present finite-system global-sector and global-fidelity promises do not replace that framework. |
| [Divi, Lessa, and Wang, arXiv:2605.28967v1](https://arxiv.org/abs/2605.28967v1) | Uses a local one-point fidelity diagnostic and discusses pure ETH examples. A local order diagnostic need not imply a lower bound on total finite-system entropy. |
| [Carolyn Zhang, arXiv:2605.29113v1](https://arxiv.org/abs/2605.29113v1) | Studies local Markov/Lindblad transitions and marginal-fidelity diagnostics, with comparisons to global fidelity under additional assumptions. Transferring the present bounds requires those actual global promises to be established. |

These works motivate the explicit scope statements in [Interpretation](../science/interpretation.md) and the [Gram-norm counterexample](../science/scope_and_robustness.md). No equivalence among these diagnostics is assumed.

## The consequential difference

The supported result consists of the following linked statements.

1. A product-input preparation obeys a spatially amplified orbit-entropy lower bound. In circuits, disjoint backward cones give exact Gram tensorization. In continuous time, shell cuts and small fingerprint registers give a controlled conditional-entropy replacement.
2. Strong sector support yields a causal-volume entropy bound even with arbitrary preshared classical randomness. Combining it with the static floor gives the second frontier.
3. Explicit strongly symmetric preparations attain both scalings. Their exact rank formula distinguishes the number of supplied seed bits from the mixedness retained by the system, and their local schedules charge actual signal propagation.
4. Counterexamples delimit the correlation and sector assumptions; stronger local masks show that hidden composite charged correlations are not needed for the upper scaling.

The sources compared here supply important parts of the framework and methods, but do not state this pair of matching frontiers under these resource and correlation assumptions. That is a comparison of the identified models and results, not a claim that an exhaustive literature search can prove absolute priority.

## Scope of the comparison

The search and reading covered global-fidelity SWSSB and purification, symmetry-sector entanglement and preparation, general mixed-state circuit complexity, entropy bounds for independence and random-access information, local-generator propagation and entropy continuity, and the local/infinite-volume diagnostic distinctions above. Nearby model-specific Rényi-entropy growth, thermal energy costs, and other asymmetry resource measures do not automatically bound the optimized von Neumann entropy used here. The bibliography focuses on sources that support a proof ingredient or a consequential comparison.
