# Thirty milestones for the preparation–entropy frontier

This is a common map of the project's ideas. The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018), as identified on the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). The [anchor and bridge](anchor.md#targeted-sections) records the verified section references and connects the book's notation to this repository. The section pointers below select foundations; they do not prescribe reading the whole book. Project links identify the authoritative assumptions, statements, and proofs.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The first phase assembles the state, channel, information, and spatial-resource language needed to formulate one precise optimization. The second has more room because the result needs two different converse mechanisms, an explicit matching preparation, and a controlled continuous-time extension. Both phases run from individual objects and local operations toward a complete many-body statement. Their final milestones integrate the preceding ideas.

| Phase | Milestones | Local-to-global progression |
|---|---|---|
| Background / preliminaries | M01–M04 | A retained spin, mixtures, and local channels become a joint system with an apparatus and a purification. |
| Background / preliminaries | M05–M08 | Charge support, ordinary correlations, and fidelity become distinct global state conditions. |
| Background / preliminaries | M09–M12 | Ensemble information and entropy identities combine with spatial resources to define the optimization. |
| Narrative / innovation | M13–M16 | A binary information inequality becomes an orbit argument and a preparation-independent entropy floor. |
| Narrative / innovation | M17–M20 | Local causal structure produces different spatial lower bounds for product and shared-classical resources. |
| Narrative / innovation | M21–M24 | Symmetric gates and classical masks become exact-spectrum preparations matching the circuit bounds. |
| Narrative / innovation | M25–M27 | Local propagation estimates and small auxiliary registers extend the result to continuous time. |
| Narrative / innovation | M28–M30 | Robustness, counterexamples, and attribution delimit the final physical conclusion. |

Dependencies below name the main conceptual inputs, rather than every earlier definition. Research papers cited by the canonical scientific pages supply attribution and specialized ingredients; they are not additional educational anchors.

## Phase I: Background and preliminaries

### M01. Retained spin and apparatus

**Central question:** Which physical degrees of freedom constitute the state whose entropy is minimized?

**Understanding target:** Distinguish a retained qubit, its density operator, and local preparation apparatus. The output is the joint state of the retained spins after the apparatus is discarded; its entropy is a property of that specified output.

**Dependencies and story role:** No earlier milestone is required. This fixes the object that every later bound and construction must describe.

**Conceptual connection:** Choosing a subsystem is part of defining an information resource. An entropy statement is incomplete until its retained registers are identified.

**Sources:** [Watrous §§2.1.1–2.1.2](anchor.md#targeted-sections); [Model: what is charged](../science/model.md#what-is-charged).

### M02. Mixtures and the meaning of output entropy

**Central question:** How can pure states in every classical branch yield a mixed retained state?

**Understanding target:** Interpret a classical ensemble and its average density operator. Distinguish the entropy of a supplied seed, the average entropy conditioned on that seed, and the entropy of the unconditional output. These quantities need not agree.

**Dependencies and story role:** Builds on [M01](#m01-retained-spin-and-apparatus). It establishes the accounting needed when the same random label is used at many sites.

**Conceptual connection:** Forgetting a preparation record changes the state available to an observer. The optimization charges the resulting retained state, not a selected branch.

**Sources:** [Watrous §§2.1.2, 5.1.1, 5.2.1](anchor.md#targeted-sections); [Interpretation: what the resource is](../science/interpretation.md#what-the-resource-is).

### M03. A local quantum channel

**Central question:** What operations can one local preparation step perform?

**Understanding target:** Relate a completely positive, trace-preserving map to a physical implementation with an apparatus, unitary interaction, measurement, and discard. Recognize that a classical outcome can be part of a channel without selecting successful outcomes.

**Dependencies and story role:** Uses [M01](#m01-retained-spin-and-apparatus) and [M02](#m02-mixtures-and-the-meaning-of-output-entropy). It supplies the elementary operation from which the circuit model is built.

**Conceptual connection:** A channel describes the transformation of the retained state; its apparatus realization reveals which correlations and signals must be physically supplied.

**Sources:** [Watrous §§2.2.1–2.2.3, 2.3.1](anchor.md#targeted-sections); [Model: channels, records, and causal constraints](../science/model.md#what-is-charged).

### M04. Joint systems and purification

**Central question:** How can a mixed state be studied through a pure state on a larger system?

**Understanding target:** Connect partial trace, purification, and the equality of the two marginal entropies of a bipartite pure state. A purification used in a converse is a mathematical representation; it is not initial nonlocal entanglement supplied to the preparation.

**Dependencies and story role:** Combines [M01](#m01-retained-spin-and-apparatus)–[M03](#m03-a-local-quantum-channel). It prepares the system–environment viewpoint used in the orbit proof.

**Conceptual connection:** Retained mixedness can be represented as entanglement with a purifier, while remaining distinct from entanglement between spatial regions or from thermodynamic heat.

**Sources:** [Watrous §§2.1.3, 2.2.2, 5.2.2](anchor.md#targeted-sections); [Interpretation: what the resource is](../science/interpretation.md#what-the-resource-is).

### M05. Symmetry as a support condition

**Central question:** What extra information does a sharp global charge sector provide?

**Understanding target:** Distinguish $`Q\rho=\rho`$ from $`Q\rho Q=\rho`$ for $`Q=\prod_iX_i`$. Exact sector support forces every observable anticommuting with $`Q`$, including each $`Z_i`$, to have zero expectation. The project supplies this physical symmetry condition; the anchor supplies the state and operator language.

**Dependencies and story role:** Uses [M01](#m01-retained-spin-and-apparatus) and [M04](#m04-joint-systems-and-purification). It identifies the assumption later needed in shared-classical branches.

**Conceptual connection:** Invariance of a density operator and confinement of its support to one eigenspace are different constraints.

**Sources:** [Watrous §§1.1.2, 2.1.2](anchor.md#targeted-sections); [Model: state, geometry, and order](../science/model.md#state-geometry-and-order).

### M06. Ordinary correlations as a Gram matrix

**Central question:** What collective restriction is expressed by a bounded ordinary-correlation matrix?

**Understanding target:** View $`C_{ij}=\mathrm{Tr}(\rho Z_iZ_j)`$ as a positive semidefinite Gram matrix. Distinguish the size-independent condition $`C\preceq\kappa I`$ from small individual off-diagonal entries. A matrix can have individually vanishing entries and a growing operator norm.

**Dependencies and story role:** Uses [M04](#m04-joint-systems-and-purification). It introduces the spectral condition that later forces many distinguishable directions in an orbit ensemble.

**Conceptual connection:** Pair observations become a collective constraint through matrix spectrum, not through entrywise size alone.

**Sources:** [Watrous §§1.1.2–1.1.3, 2.1.3](anchor.md#targeted-sections); [Model: ordinary Gram condition](../science/model.md#state-geometry-and-order); [Scope: bounded norm versus clustering](../science/scope_and_robustness.md#bounded-gram-norm-versus-qualitative-clustering).

### M07. Global fidelity and purification overlap

**Central question:** What does it mean for a charged pair operation to leave a global state partly indistinguishable?

**Understanding target:** Interpret root fidelity $`F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1`$ through optimal purification overlap. The project's $`f_{ij}`$ compares the complete retained state with its conjugate by $`Z_iZ_j`$, rather than comparing only the two-site reduced states.

**Dependencies and story role:** Uses [M04](#m04-joint-systems-and-purification) and [M05](#m05-symmetry-as-a-support-condition). It fixes both the fidelity convention and the global diagnostic.

**Conceptual connection:** A local operator can probe a global distinction. The size of the operator's support does not determine which state is being compared.

**Sources:** [Watrous §§3.2.1–3.2.2](anchor.md#targeted-sections); [Model: root fidelity](../science/model.md#state-geometry-and-order).

### M08. Fidelity under channels and classical mixing

**Central question:** Which fidelity statements remain valid after information is discarded or branches are averaged?

**Understanding target:** Understand channel monotonicity and joint concavity of root fidelity. Matched mixtures can inherit a lower fidelity bound from their paired components. A fidelity bound on an average state, however, does not assert the same bound in every classical branch.

**Dependencies and story role:** Combines [M02](#m02-mixtures-and-the-meaning-of-output-entropy), [M03](#m03-a-local-quantum-channel), and [M07](#m07-global-fidelity-and-purification-overlap). These are the operations used in the binary tree and twirl arguments.

**Conceptual connection:** Forgetting information makes states harder to distinguish; it does not justify transferring an unconditional promise to each hidden preparation record.

**Sources:** [Watrous §3.2.3](anchor.md#targeted-sections); [Binary-tree proof](../science/entropy_bounds.md#proposition-e2-binary-tree-holevo-bound); [Shared-branch lemma](../science/circuit_bounds.md#lemma-b4-strong-symmetry-in-every-shared-seed-branch).

### M09. Ensemble entropy and Holevo information

**Central question:** How is information about a classical label represented in a quantum ensemble?

**Understanding target:** Interpret Holevo information as the entropy of the average state minus the average component entropy, or equivalently as classical–quantum mutual information. Separate this quantity from the entropy of the label and from information obtainable by one specified measurement.

**Dependencies and story role:** Uses [M02](#m02-mixtures-and-the-meaning-of-output-entropy) and [M04](#m04-joint-systems-and-purification). It provides the information quantity bounded by pair fidelity in the converse.

**Conceptual connection:** An ensemble can contain many labels while the quantum system reveals little about which label was used.

**Sources:** [Watrous §§5.2.1, 5.3.3](anchor.md#targeted-sections); [Binary Holevo information from fidelity](../science/entropy_bounds.md#proposition-e1-binary-holevo-information-from-fidelity).

### M10. Entropy identities that assemble many parts

**Central question:** How can information about many labels be decomposed without assuming those labels remain independent after observation?

**Understanding target:** Connect entropy chain rules, conditional entropy, subadditivity, and data processing. These identities distinguish an exact algebraic decomposition from the physical independence assumption that may later simplify it.

**Dependencies and story role:** Builds on [M09](#m09-ensemble-entropy-and-holevo-information). It supplies the transition from a binary label to a large ensemble and from a pure system–environment state to a retained-state lower bound.

**Conceptual connection:** Chain rules organize dependence instead of removing it. Subadditivity compares a joint description with its marginal descriptions.

**Sources:** [Watrous §§5.1.2, 5.2.1–5.2.3](anchor.md#targeted-sections); [Binary-tree bound](../science/entropy_bounds.md#proposition-e2-binary-tree-holevo-bound); [Orbit theorem](../science/entropy_bounds.md#theorem-e3-unitary-orbit-entropy-bound).

### M11. Spatial preparation resources

**Central question:** Which correlations are supplied before preparation, and which must propagate during it?

**Understanding target:** Distinguish a product initial system–apparatus state from a classically correlated mixture of product branches. Recognize that separability permits shared classical correlation, while the strict product model excludes it. Signals generated during either preparation obey the same spatial locality constraint.

**Dependencies and story role:** Combines [M02](#m02-mixtures-and-the-meaning-of-output-entropy), [M03](#m03-a-local-quantum-channel), and [M04](#m04-joint-systems-and-purification). It defines the two classes compared by the main theorem.

**Conceptual connection:** A shared classical seed is an initial resource. Its availability is distinct from an allowed local channel or from communication sent after the clock begins.

**Sources:** [Watrous §§2.2.2, 6.1.1](anchor.md#targeted-sections); [Model: preparation classes](../science/model.md#what-is-charged).

### M12. The complete operational question

**Central question:** What is optimized when order, ordinary correlations, and preparation resources are fixed?

**Understanding target:** Assemble one finite-system problem: minimize unconditional retained entropy over both states and protocols, with fixed fidelity threshold $`c\gt0`$, fixed Gram bound $`\kappa`$, and a specified local depth or time. Interpret an empty feasible class and the diameter cap before using asymptotic notation.

**Dependencies and story role:** Integrates [M05](#m05-symmetry-as-a-support-condition)–[M11](#m11-spatial-preparation-resources). This closes the background phase by stating the exact question that the narrative answers.

**Conceptual connection:** The result is a frontier over an admissible state class and preparation class, rather than the preparation complexity of one prescribed density matrix.

**Sources:** [Watrous §§2.1–2.2, 3.2, 5.2](anchor.md#targeted-sections); [Model: optimization and scaling](../science/model.md#optimization-and-scaling-convention); [Interpretation: the preparation frontier](../science/interpretation.md#a-preparation-frontier-for-retained-mixedness).

## Phase II: Narrative and innovation

### M13. The binary information cost of fidelity

**Central question:** How much information can distinguish two states whose root fidelity is at least $`c`$?

**Understanding target:** Follow the inherited binary Holevo bound $`\chi\leq h_2((1+c)/2)`$: choose purifications with the prescribed overlap, diagonalize their equal mixture, and discard the purifier. Identify $`w(c)=1-h_2((1+c)/2)`$ as the positive information deficit that drives the lower bounds.

**Dependencies and story role:** Uses [M04](#m04-joint-systems-and-purification), [M07](#m07-global-fidelity-and-purification-overlap), and [M09](#m09-ensemble-entropy-and-holevo-information). This is the local information step, not a new standalone inequality.

**Conceptual connection:** A geometric overlap becomes an entropic restriction through a two-dimensional purified ensemble.

**Sources:** [Watrous §§3.2.2, 5.2.3, 5.3.3](anchor.md#targeted-sections); [Proposition E1](../science/entropy_bounds.md#proposition-e1-binary-holevo-information-from-fidelity); [Ingredient attribution](../references/related_work.md#information-theoretic-ingredients).

### M14. A binary tree for many labels

**Central question:** How can a pairwise fidelity promise control information about a long label?

**Understanding target:** Split a uniform label one bit at a time, pair equal remaining suffixes, and use joint concavity before applying the binary bound. The chain rule then sums the conditional information costs. Only the paired edges used by this construction require fidelity bounds.

**Dependencies and story role:** Combines [M08](#m08-fidelity-under-channels-and-classical-mixing), [M10](#m10-entropy-identities-that-assemble-many-parts), and [M13](#m13-the-binary-information-cost-of-fidelity). It turns one binary restriction into a scalable ensemble statement.

**Conceptual connection:** Coordinated pairings let a large label be analyzed without assuming fidelity for every product of charged-pair operators.

**Sources:** [Watrous §§3.2.3, 5.2.1, 5.3.3](anchor.md#targeted-sections); [Proposition E2](../science/entropy_bounds.md#proposition-e2-binary-tree-holevo-bound).

### M15. Entropy from a purified unitary orbit

**Central question:** Where must label information reside when the purified ensemble has more distinguishable directions than the system can reveal?

**Understanding target:** Relate the nonzero spectrum of a pure-state ensemble average to its normalized Gram matrix. For a system-unitary orbit, the purifier marginal stays fixed. Combine the Gram entropy, the system Holevo bound, and subadditivity to obtain the orbit lower bound on twice the retained entropy.

**Dependencies and story role:** Uses [M04](#m04-joint-systems-and-purification), [M06](#m06-ordinary-correlations-as-a-gram-matrix), [M10](#m10-entropy-identities-that-assemble-many-parts), and [M14](#m14-a-binary-tree-for-many-labels). This is the common mechanism behind the static and product-input converses.

**Conceptual connection:** The system–purifier split converts a mismatch between global and local label information into unavoidable retained mixedness.

**Sources:** [Watrous §§1.1.3, 2.1.3, 5.2.2, 5.3.3](anchor.md#targeted-sections); [Theorem E3](../science/entropy_bounds.md#theorem-e3-unitary-orbit-entropy-bound).

### M16. A static entropy floor and its classical endpoint

**Central question:** Why does bounded ordinary Gram norm already prohibit a constant-entropy state at fixed positive pair fidelity?

**Understanding target:** Apply the orbit argument to site labels with unitaries $`Z_i`$. A bounded Gram norm forces logarithmic ensemble entropy. At maximal fidelity, commuting pair parities instead give a classical sector-weight bound $`S\geq\log_2N-\log_2\kappa`$. Understand the improvement at this endpoint and its established pairwise-independence ancestry.

**Dependencies and story role:** Builds on [M06](#m06-ordinary-correlations-as-a-gram-matrix) and [M15](#m15-entropy-from-a-purified-unitary-orbit). It provides the preparation-independent floor used when spatial bounds saturate.

**Conceptual connection:** A quantum orbit argument meets a classical small-sample-space entropy constraint when the pair operations leave the state exactly invariant.

**Sources:** [Watrous §§1.1.3, 5.1.2, 5.2.2](anchor.md#targeted-sections); [Corollary E4](../science/entropy_bounds.md#corollary-e4-global-logarithmic-floor); [Proposition E6](../science/entropy_bounds.md#proposition-e6-maximal-fidelity-endpoint).

### M17. Independent output regions from causal cones

**Central question:** When does finite circuit depth imply exact independence of separated output regions?

**Understanding target:** Trace backward the input systems and channels influencing each chosen output region. Disjoint backward cones and a product initial system–apparatus state make the full reduced output factorize. Pairwise covariance alone would not establish this factorization.

**Dependencies and story role:** Uses [M03](#m03-a-local-quantum-channel) and [M11](#m11-spatial-preparation-resources). It supplies the physical independence statement needed to amplify the orbit bound over space.

**Conceptual connection:** A local dynamical constraint becomes an exact tensor-product statement only after the initial correlation resource has been specified.

**Sources:** [Watrous §§2.1.3, 2.2.1–2.2.2](anchor.md#targeted-sections); [Lemma B1](../science/circuit_bounds.md#lemma-b1-exact-output-factorization).

### M18. A logarithmic cost in every independent region

**Central question:** Why does product apparatus incur more than one bit of entropy per causal volume?

**Understanding target:** Give each separated box a site label and multiply the corresponding $`Z`$ operators. Exact output factorization makes the orbit Gram matrix a tensor product. Each binary comparison still changes only one charged pair, so the information deficit adds over all label bits. Spatial packing yields a contribution of order $`K\log m`$ for $`K`$ boxes with $`m`$ sites each.

**Dependencies and story role:** Combines [M14](#m14-a-binary-tree-for-many-labels)–[M17](#m17-independent-output-regions-from-causal-cones). This is the stronger product-input converse.

**Conceptual connection:** Independence multiplies distinguishable orbit labels; entropy turns that multiplicative number into an additive regional cost.

**Sources:** [Watrous §§2.1.3, 5.2.2, 5.3.3](anchor.md#targeted-sections); [Theorem B2](../science/circuit_bounds.md#theorem-b2-independent-region-orbit-bound); [Finite-grid packing](../science/circuit_bounds.md#corollary-b3-explicit-finite-grid-lower-bound).

### M19. What survives a preshared classical seed

**Central question:** Which properties hold in every preparation branch when only the averaged state is promised to be ordered?

**Understanding target:** Use positivity to show that exact sector support of the average forces every positive-weight branch into the same sector. Hence each branch has balanced single-site $`Z`$ outcomes. Unconditional fidelity and Gram promises need not hold branchwise, and separated regions need not factorize after the seed is averaged out.

**Dependencies and story role:** Uses [M05](#m05-symmetry-as-a-support-condition), [M08](#m08-fidelity-under-channels-and-classical-mixing), [M11](#m11-spatial-preparation-resources), and [M17](#m17-independent-output-regions-from-causal-cones). It identifies the replacement for the product converse's unconditional factorization.

**Conceptual connection:** Positivity transfers an exact zero-support condition through a mixture, while nonlinear quantitative promises require separate arguments.

**Sources:** [Watrous §§2.1.2, 3.2.3, 6.1.1](anchor.md#targeted-sections); [Lemma B4](../science/circuit_bounds.md#lemma-b4-strong-symmetry-in-every-shared-seed-branch).

### M20. Parity twirls and the shared causal-volume bound

**Central question:** How can balanced separated outcomes force entropy even after arbitrary classical coordination?

**Understanding target:** Conditioned on the seed, separated single-site outcomes are independent and fair, so their joint law remains uniform after averaging. Relative parities with one reference site then contain one fewer independent bit. Commuting pair twirls expose that entropy, while unconditional fidelity bounds limit the entropy each twirl can add.

**Dependencies and story role:** Combines [M08](#m08-fidelity-under-channels-and-classical-mixing), [M13](#m13-the-binary-information-cost-of-fidelity), [M16](#m16-a-static-entropy-floor-and-its-classical-endpoint), and [M19](#m19-what-survives-a-preshared-classical-seed). It yields the shared-classical volume bound, which is combined with the static floor.

**Conceptual connection:** Classical coordination can correlate branches without changing a joint outcome law that is identical and uniform in every branch.

**Sources:** [Watrous §§4.1.1, 5.1.2, 5.2.2](anchor.md#targeted-sections); [Proposition E5](../science/entropy_bounds.md#proposition-e5-commuting-binary-twirls); [Theorem B5](../science/circuit_bounds.md#theorem-b5-finite-causal-volume-lower-bound); [Corollary B6](../science/circuit_bounds.md#corollary-b6-complete-finite-shared-classical-bound).

### M21. Growing a symmetric coherent block

**Central question:** How can local gates grow a GHZ block while preserving the global charge?

**Understanding target:** Follow the two-site fusion gate acting on an existing block and a fresh $`X`$-polarized spin. Its charge commutation and its action on the two coherent branches explain why block diameter, rather than block volume, controls the growth depth on a bounded-degree tree.

**Dependencies and story role:** Uses [M03](#m03-a-local-quantum-channel), [M05](#m05-symmetry-as-a-support-condition), and [M11](#m11-spatial-preparation-resources). It introduces the local coherent building block for the matching upper bounds.

**Conceptual connection:** A symmetry-preserving operation can enlarge a coherent region without choosing or measuring its macroscopic branch.

**Sources:** [Watrous §§1.1.2, 2.2.2](anchor.md#targeted-sections); [Strongly symmetric GHZ growth](../science/constructions.md#2-strongly-symmetric-ghz-growth).

### M22. Masks, shared seeds, and charged propagation

**Central question:** How can a short classical label erase ordinary pair correlations, and when can that label be reused?

**Understanding target:** Associate distinct binary site labels with linear sign masks. Independent block seeds and one shared seed give different joint ensembles despite identical pair diagnostics. A seed created locally must be streamed through the block; pipelining costs tree height plus seed length. Presharing changes the initial resource, not the speed of later signals.

**Dependencies and story role:** Combines [M02](#m02-mixtures-and-the-meaning-of-output-entropy), [M06](#m06-ordinary-correlations-as-a-gram-matrix), [M11](#m11-spatial-preparation-resources), and [M21](#m21-growing-a-symmetric-coherent-block). It constructs the resource-dependent difference in the upper bounds.

**Conceptual connection:** Classical pairwise-independence constructions acquire a preparation cost when their control labels must travel through space.

**Sources:** [Watrous §§1.2.2, 2.2.3, 5.1.1](anchor.md#targeted-sections); [Proposition C2](../science/constructions.md#proposition-c2-strict-product-masks); [Pipelined broadcast](../science/constructions.md#41-bounded-workspace-pipelined-broadcast); [Proposition C3](../science/constructions.md#proposition-c3-shared-classical-masks).

### M23. Boundary phases and the exact retained spectrum

**Central question:** Which random labels remain physically distinguishable after the construction is complete?

**Understanding target:** Quotient out redundant whole-block mask complements, then combine the remaining mask rank $`q`$ with the $`K-1`$ independent even-charge boundary phases. The final orthogonal cat ensemble has entropy $`q+K-1`$, exact strong charge support, unit pair fidelity, and the promised ordinary correlations.

**Dependencies and story role:** Uses [M02](#m02-mixtures-and-the-meaning-of-output-entropy), [M05](#m05-symmetry-as-a-support-condition)–[M07](#m07-global-fidelity-and-purification-overlap), and [M21](#m21-growing-a-symmetric-coherent-block)–[M22](#m22-masks-shared-seeds-and-charged-propagation). It verifies the actual output cost rather than equating that cost with the number of random choices.

**Conceptual connection:** Entropy counts distinguishable retained states. Linear dependencies and physical redundancies can make that count smaller than the supplied randomness.

**Sources:** [Watrous §§1.1.3, 5.1.1, 5.2.2](anchor.md#targeted-sections); [Proposition C1](../science/constructions.md#proposition-c1-exact-spectrum); [Fidelity and ordinary correlations](../science/constructions.md#34-fidelity-and-ordinary-correlations); [Worked block example](worked_example.md).

### M24. Matching the circuit frontiers

**Central question:** When do the lower and upper bounds describe the same operational optimization?

**Understanding target:** Match the resource class, retained output, fidelity and Gram promises, and depth accounting on both sides. Combine packing with block constructions to obtain the two circuit laws. Retain the small-depth feasibility exceptions, the fixed-parameter meaning of the constants, and the saturation at diameter depth.

**Dependencies and story role:** Integrates [M18](#m18-a-logarithmic-cost-in-every-independent-region), [M20](#m20-parity-twirls-and-the-shared-causal-volume-bound), and [M21](#m21-growing-a-symmetric-coherent-block)–[M23](#m23-boundary-phases-and-the-exact-retained-spectrum). It closes the exact-circuit part of the narrative.

**Conceptual connection:** A matching frontier requires agreement of physical resources as well as agreement of algebraic scaling.

**Sources:** [Watrous §§2.2, 5.2](anchor.md#targeted-sections); [Theorem B7](../science/circuit_bounds.md#theorem-b7-matched-circuit-frontiers); [Finite-depth feasibility](../science/circuit_bounds.md#construction-inputs-and-finite-depth-feasibility); [Proposition C4](../science/constructions.md#proposition-c4-depth-and-resource-bounds).

### M25. From exact cones to a continuous-time shell cut

**Central question:** What replaces exact spatial independence when local dynamics has exponentially small tails?

**Understanding target:** Understand the shell cut around one box under bounded finite-range generators. Each local summand is itself a valid Lindblad generator, so removing boundary terms preserves channel evolution. The smaller-support Lieb–Robinson estimate controls full trace-distance factorization between that box and the entire distant union, without a prefactor proportional to the union's size.

**Dependencies and story role:** Uses [M03](#m03-a-local-quantum-channel) and [M17](#m17-independent-output-regions-from-causal-cones). It replaces the exact circuit independence input; the propagation theorem is a research ingredient beyond the anchor.

**Conceptual connection:** A local approximation is useful globally only if its error remains controlled when the distant comparison system grows.

**Sources:** [Watrous §§1.1.3, 2.2.1–2.2.2](anchor.md#targeted-sections); [Dynamical assumptions](../science/continuous_time.md#2-precise-dynamical-assumptions); [Shell-cut factorization](../science/continuous_time.md#3-shell-cut-trace-factorization); [Research dependencies](anchor.md#research-level-dependencies).

### M26. Small registers preserve the logarithmic gain

**Central question:** How can an approximate factorization error be converted to an entropy error without paying for an entire physical block?

**Understanding target:** Represent a box's orbit Gram matrix using a measure-and-prepare channel whose auxiliary register has dimension equal to the selected site count $`m`$, rather than $`2^m`$. Chain conditional entropies across boxes and apply continuity with an $`O(\epsilon\log m)`$ local cost. The dimension of the distant conditioning register does not enter that cost.

**Dependencies and story role:** Combines [M10](#m10-entropy-identities-that-assemble-many-parts), [M15](#m15-entropy-from-a-purified-unitary-orbit), [M18](#m18-a-logarithmic-cost-in-every-independent-region), and [M25](#m25-from-exact-cones-to-a-continuous-time-shell-cut). This preserves the product-input logarithmic enhancement in continuous time.

**Conceptual connection:** A representation tailored to the information being bounded can reduce the dimension relevant to continuity without approximating away the physical state conditions.

**Sources:** [Watrous §§2.2.3, 5.2.1–5.2.3](anchor.md#targeted-sections); [Fingerprint registers and the ensuing continuity proof](../science/continuous_time.md#4-orbit-ensembles-and-local-fingerprint-registers); [Finite-box theorem](../science/continuous_time.md#6-finite-box-theorem-constants-packing-and-the-diameter-cap).

### M27. Continuous-time matching and its apparatus model

**Central question:** Under which physical implementation assumptions do the time-dependent lower and upper bounds match?

**Understanding target:** Combine shell-cut packing, the small-register bound, and the static floor with the diameter cap. For shared randomness, apply conditional factorization to balanced branch outcomes while keeping fidelity unconditional. Match both laws with bounded Hamiltonian interactions and local apparatus retained until the final discard; distinguish its logarithmic local storage from the reset-assisted circuit's bounded active workspace.

**Dependencies and story role:** Integrates [M19](#m19-what-survives-a-preshared-classical-seed)–[M20](#m20-parity-twirls-and-the-shared-causal-volume-bound) and [M24](#m24-matching-the-circuit-frontiers)–[M26](#m26-small-registers-preserve-the-logarithmic-gain). It completes the time extension in the stated local-apparatus model.

**Conceptual connection:** A local channel realization and a bounded system-only Markovian evolution need not have the same exact finite-time capabilities.

**Sources:** [Watrous §§2.2.2–2.2.3, 5.2.1](anchor.md#targeted-sections); [Finite-time constants and cap](../science/continuous_time.md#6-finite-box-theorem-constants-packing-and-the-diameter-cap); [Hamiltonian preparation](../science/continuous_time.md#7-matching-bounded-hamiltonian-preparation); [Shared-classical time bound](../science/continuous_time.md#8-shared-classical-continuous-time-lower-bound).

### M28. Robustness to actual charge-sector leakage

**Central question:** Which part of the theorem survives when the prepared state has a small weight in the wrong charge sector?

**Understanding target:** Follow the dimension-independent correction to the shared causal-volume bound and its sufficient condition $`4\epsilon(1-\epsilon)\lt w(c)`$. Contrast that controlled range with the depth-zero counterexample at leakage $`c/2`$. The product-input orbit bound and the static floor need no sector assumption when their actual fidelity and Gram promises hold.

**Dependencies and story role:** Uses [M05](#m05-symmetry-as-a-support-condition), [M18](#m18-a-logarithmic-cost-in-every-independent-region), and [M19](#m19-what-survives-a-preshared-classical-seed)–[M20](#m20-parity-twirls-and-the-shared-causal-volume-bound). It separates supported noise tolerance from an unresolved sharp leakage threshold.

**Conceptual connection:** Robustness should track the specific hypothesis used by each proof, rather than treating every conclusion as equally dependent on exact symmetry.

**Sources:** [Watrous §§2.1.2, 5.1.2](anchor.md#targeted-sections); [Proposition R1](../science/scope_and_robustness.md#proposition-r1-dimension-free-leakage-correction); [Counterexample R2](../science/scope_and_robustness.md#counterexample-r2-failure-at-leakage-c2); [Continuous-time correction](../science/continuous_time.md#optional-actual-state-sector-leakage-correction).

### M29. Correlation assumptions and the boundary of the order claim

**Central question:** Why is qualitative disappearance of ordinary pair correlations insufficient for the stated entropy law?

**Understanding target:** Understand the small cat-mixture counterexample with vanishing pair entries, unit global pair fidelity, and only $`O(\log\log N)`$ entropy. Its growing Gram norm identifies the missing hypothesis. Distinguish zero ordinary pair correlations from absence of all local charged correlations, and recognize how stronger masks improve the examples without changing the converse's assumptions.

**Dependencies and story role:** Uses [M06](#m06-ordinary-correlations-as-a-gram-matrix), [M16](#m16-a-static-entropy-floor-and-its-classical-endpoint), and [M22](#m22-masks-shared-seeds-and-charged-propagation)–[M23](#m23-boundary-phases-and-the-exact-retained-spectrum). It places the frontier within a precisely specified finite-system global-fidelity framework.

**Conceptual connection:** A counterexample can identify the collective condition missing from an apparently similar local diagnostic.

**Sources:** [Watrous §§1.1.3, 5.2.2](anchor.md#targeted-sections); [Gram-norm counterexample](../science/scope_and_robustness.md#counterexample-r3-vanishing-pair-correlations-with-smaller-entropy); [Stronger local charged masks](../science/constructions.md#7-masks-that-suppress-general-local-charged-correlations); [Relation to mixed-state order](../science/interpretation.md#relation-to-mixed-state-order).

### M30. The global physical conclusion

**Central question:** What does classical coordination change about the least mixedness compatible with locally prepared global fidelity order?

**Understanding target:** Integrate the two mechanisms and their matching preparations. At accessible linear scale $`\ell`$, product resources require a logarithmic cost in each causal volume, while a preshared seed permits mask information to be reused:

```math
S_{\min}^{\mathrm{prod}}
=\Theta_{d,c,\kappa}\!\left[\frac{N}{\ell^d}\log_2(\ell+1)\right],
\qquad
S_{\min}^{\mathrm{sh}}
=\Theta_{d,c,\kappa}\!\left[\frac{N}{\ell^d}+\log_2N\right].
```

Here $`\ell=\min\{L,D+1\}`$ in the circuit theorem; the time theorem uses its separately specified propagation scale and apparatus assumptions. Keep the implementation thresholds and finite-size qualifications attached to these laws.

**Dependencies and story role:** Integrates [M12](#m12-the-complete-operational-question), [M24](#m24-matching-the-circuit-frontiers), and [M27](#m27-continuous-time-matching-and-its-apparatus-model)–[M29](#m29-correlation-assumptions-and-the-boundary-of-the-order-claim). This closes the narrative by separating the established ingredients from the consequential matched preparation result.

**Conceptual connection:** The scientific contribution is the resource-dependent pair of preparation frontiers and its physical accounting. The binary fidelity inequality, purification interpretation, static logarithmic scale, and classical masks have antecedents. Retained entropy is neither a universal order parameter nor a thermodynamic heat cost.

**Sources:** [Watrous §§2.2, 3.2, 5.2, 5.3.3](anchor.md#targeted-sections); [Matched circuit theorem](../science/circuit_bounds.md#theorem-b7-matched-circuit-frontiers); [Continuous-time result and scope](../science/continuous_time.md#1-result-and-scope); [Physical interpretation](../science/interpretation.md#a-preparation-frontier-for-retained-mixedness); [The consequential difference from prior work](../references/related_work.md#the-consequential-difference).

Return to the [learning guide](README.md), [anchor and notation bridge](anchor.md), or [scientific reading guide](../science/README.md).
