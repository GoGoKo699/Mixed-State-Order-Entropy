# Physical interpretation

## A preparation frontier for retained mixedness

The central optimization varies both the prepared state and its preparation protocol. It asks for the least output entropy among all states meeting a fixed order condition and a fixed ordinary-correlation bound, when the local depth or time is limited. It does not assign a complexity to one prescribed density matrix.

The two matching laws describe a crossover between many independently prepared regions and one coherent system-scale region. If the accessible linear scale is $`\ell`$, there are approximately $`K=N/\ell^d`$ causal volumes. Product apparatus must support a logarithmic amount of mixedness in each volume, producing $`K\log(\ell+1)`$. Shared classical randomness permits the same mask information to be reused across volumes, leaving a cost of order $`K+\log N`$.

The comparison is quantitative. For a one-dimensional chain with depth of order $`\sqrt N`$, the [circuit theorem](circuit_bounds.md) gives

```math
S_{\min}^{\mathrm{prod}}=\Theta(\sqrt N\log N),
\qquad
S_{\min}^{\mathrm{shared}}=\Theta(\sqrt N).
```

At fixed depth both costs are extensive. At diameter depth both are logarithmic. Between those regimes the difference can grow logarithmically with system size. These conclusions hold for fixed positive fidelity threshold and fixed Gram-norm bound; allowing either parameter to scale requires the finite inequalities.

## Where the entropy comes from

The explicit states make two sources of mixedness visible. Boundary channels randomize the signs of block cats subject to one global charge constraint, contributing exactly $`K-1`$ bits. Local masks randomize their internal sign patterns while destroying ordinary pair correlations. The mask contribution is the rank of a binary linear map after physically redundant block complements have been removed.

Independent block masks have independent distinguishable labels, so their entropies add. A shared mask uses one label across all blocks. It need only distinguish sites *inside* a block because ordinary cross-block correlations already vanish. Thus the economical shared construction uses $`\lceil\log_2 m_*\rceil`$ seed bits, where $`m_*`$ is the largest block size, and its exact entropy is

```math
K-1+\lceil\log_2m_*\rceil.
```

This remains at least $`\log_2N`$: the boundary-sign contribution supplies the difference when the mask seed is short. The [spectrum proof](constructions.md) is needed here; the entropy of a supplied classical seed need not equal the entropy it leaves in the retained state.

The propagation of an initially local seed is a physical operation. Streaming along a block tree costs its height plus the seed length, rather than their product. Independent seeds can therefore be distributed in parallel within blocks in time of order $`\ell`$. A seed distributed over the entire lattice after the clock begins cannot be counted as free preshared randomness.

## Why the converse measures a collective requirement

A nonzero pair fidelity says that conjugation by a charged pair does not make the global state perfectly distinguishable. The [binary Holevo bound](entropy_bounds.md) quantifies how much information about such a conjugation can reach the system.

The proof applies this fact to a family of purifications labeled by the sites in a region. The ordinary correlation matrix is their Gram matrix. A bounded Gram norm forces many distinguishable directions in the purified ensemble, even though the system alone has limited label information. Subadditivity then requires entropy in the retained state.

For product-input circuits, separated output regions factor exactly and their label Gram matrices form a tensor product. The entropy requirement consequently adds over regions. The proof never assumes a fidelity bound for products of many pair operators: each binary comparison changes only one pair and keeps all other labels identical.

Continuous-time evolution has exponentially small tails instead of exact causal cones. Applying an entropy continuity bound directly to a physical block would be too expensive. The [continuous-time proof](continuous_time.md) instead represents its Gram matrix in an auxiliary register whose dimension is the *number of selected sites*. Its logarithmic dimension gives the correct continuity cost. A local shell cut compares one block with the whole union of earlier blocks, avoiding a system-size accumulation in the locality error.

## The roles of symmetry and ordinary correlations differ

Strong charge support supplies a useful statement in every branch of a shared classical ensemble. Positivity forces each branch to occupy the same charge sector. For circuits, single-site $`Z`$ outcomes with disjoint backward cones are individually fair and conditionally independent; their joint law remains uniform after the seed is forgotten. For continuous-time dynamics, shell cuts replace exact independence by approximate factorization with a dimension-independent single-bit entropy correction. These arguments yield the shared-classical causal-volume lower bounds.

The orbit argument has a different assumption set: it uses the actual Gram and pair-fidelity promises, without needing symmetry. It therefore supplies the global logarithmic floor and the stronger product-input bound even outside the exact charge sector. The matching examples nevertheless preserve the charge at every operation.

The ordinary-correlation condition cannot be replaced by a qualitative phrase. A mixture of a small number of randomly chosen even cats can have pair fidelity exactly one while all ordinary pairs tend uniformly to zero. With a suitable sample size its entropy is only $`O(\log\log N)`$. Its correlation Gram norm grows with size, so it lies outside the theorem. The [explicit construction and proof](scope_and_robustness.md) prevent interpreting the logarithmic floor as a universal consequence of every weak notion of clustering.

Charge leakage has its own boundary. A dimension-independent correction preserves the shared causal-volume bound for a specified small leakage range. A separate shared-seed example with leakage $`c/2`$ has only logarithmic entropy already at depth zero. The gap between that example and the sufficient robustness range remains open; the result does not claim a sharp noise threshold.

## Relation to mixed-state order

The finite-system global pair-fidelity framework is established in [Lessa et al.](https://arxiv.org/abs/2405.03639v3). Its purification interpretation is developed by [Sala et al.](https://arxiv.org/abs/2405.02402). This project fixes that global diagnostic and studies an entropy-constrained preparation problem within it.

Later formulations distinguish local and infinite-volume notions of strong symmetry and order. [Liu, Yi, and Else](https://arxiv.org/abs/2605.28925v3) develop a local infinite-volume description. [Divi, Lessa, and Wang](https://arxiv.org/abs/2605.28967v1) use a local one-point fidelity diagnostic, including examples related to pure ETH states. A local diagnostic can therefore have a different implication for the total entropy of a finite global state. Transferring the present bound to such a definition requires an additional implication proving the actual global promises used here.

Even the baseline mask construction has a narrower ordinary-order guarantee than a full phase statement: pairwise independence can leave higher charged products. The stronger masks in [Constructions, Section 7](constructions.md#7-masks-that-suppress-general-local-charged-correlations) suppress correlations of arbitrary charged operators on growing local balls at the same asymptotic preparation cost. This strengthens the examples while leaving the converse's stated assumptions explicit.

## What the resource is

The cost is the von Neumann entropy of the retained spins after all preparation records are discarded. It is not entanglement of formation between spatial regions. For example, the high-entropy constant-depth endpoint $`(I+Q)/2^N`$ is a mixture of product $`X`$ eigenstates. The lower bound does not require the entropy to have a particular spatial entanglement interpretation.

For a globally pure dilation, retained entropy equals entanglement entropy with the discarded apparatus. This equality does not turn the theorem into a heat or irreversible entropy-production law. Resets, control generation, and disposal of records need their own thermodynamic accounting.

Finally, a local CPTP circuit and a bounded-rate system-only master equation are distinct models. Exact complete dephasing is an allowed circuit channel and can be realized by a bounded interaction with a local meter followed by a trace. It is not the exact finite-time channel of a bounded system-only Markovian generator. The continuous-time upper theorem explicitly retains local apparatus, with logarithmic local storage in the direct coherent implementation.

## Remaining directions within the stated boundaries

The finite bounds leave room to improve coefficients, particularly when the fidelity threshold becomes small. The leakage range, a matching implementation with fixed local dimension and no intermediate reset, and exact optimal preparation under a system-only Markovian restriction are separate unresolved questions. None is needed for the matched circuit and local-apparatus time frontiers proved here.
