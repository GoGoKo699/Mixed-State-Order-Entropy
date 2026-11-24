# Learning guide

How can a state have little ordinary pair correlation, retain global fidelity order, and still be forced to carry entropy? How much preshared randomness does it take to lower that entropy?

The learning route builds toward these questions from the finite-dimensional language of quantum information. Its single educational anchor is John Watrous's *The Theory of Quantum Information* (Cambridge University Press, 2018), available through the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). The book supplies states, channels, fidelity, and entropy. The repository supplies the spatial preparation models, the information argument applied to many-body orbits, and the matching constructions.

## Choose a reading route

| Starting question | Route |
|---|---|
| Which textbook ideas are actually needed? | [Anchor and bridge](anchor.md), including the notation and research-dependency map |
| What changes when some mask bits are shared? | [Worked block examples](worked_example.md#eight-spins-with-zero-one-or-two-shared-bits), then the [exact spectrum and frontier](../science/shared_seed_budget.md) |
| How do all the ideas fit together? | [30-milestone map](milestones.md), with background/preliminaries followed by narrative/innovation |
| Where are the precise hypotheses and proofs? | [Model](../science/model.md) and [scientific reading guide](../science/README.md) |
| What does the finite computation establish? | [Verification guide](../verification/README.md) |

The milestones are understanding targets, not a requirement to read the entire textbook first. Each points to the needed foundation and the authoritative project statement. The worked example makes one construction tangible; the general bounds remain in the scientific account.

| Phase | Milestones | Scientific progression |
|---|---|---|
| Background/preliminaries | M01–M12 | Build from states and channels through symmetry, fidelity, entropy, and spatial resources to the precise optimization problem. |
| Narrative/innovation | M13–M30 | Derive the static entropy floor, quantify how much each shared bit can save across distant boxes, match the result with explicit masks, and extend the bounds to continuous time. |

The allocation gives the two converse mechanisms, the preparation resource accounting, and the continuous-time extension room to connect. Each phase ends by assembling its components into the global question or result.

## Keep the operational distinctions visible

The output entropy is the entropy of the retained spins after averaging over seeds and discarding apparatus. The seed budget $`h`$ caps the Shannon entropy of the whole common variable. Local coins generated from product apparatus can supply additional randomness, and any signals sent during the run propagate locally.

Strong charge support, global pair fidelity, and the norm of the ordinary correlation matrix are separate conditions. At exact unit pair fidelity, the density matrix is diagonal in the global even-cat basis, and the joint computational-basis readout has one bit more entropy than the retained state. This gives the matched finite-seed law. The proof at a fixed imperfect fidelity threshold gives separate upper and lower bounds. [Seed budget](../science/shared_seed_budget.md) · [Scope](../science/scope_and_robustness.md)

The circuit upper construction uses local resets and bounded active workspace. Its explicit coherent continuous-time realization retains logarithmically many auxiliary qubits per site until the final discard. These statements describe different apparatus resources. The [continuous-time proof](../science/continuous_time.md) states the allowed generator model and the limit of the matching claim.

For attribution of the research ingredients beyond Watrous, consult [related work](../references/related_work.md). For the complete result and physical interpretation, return to the [repository overview](../README.md) and [interpretation](../science/interpretation.md).
