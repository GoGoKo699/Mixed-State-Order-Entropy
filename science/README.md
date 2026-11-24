# Scientific reading guide

The question is how local preparation constrains the **retained entropy of an ordered mixed state** and how much preshared classical randomness can reduce that cost.

Read the account in the following order.

1. [Model](model.md) fixes the finite-system observable, root-fidelity convention, correlation-matrix promise, and two preparation classes.
2. [Entropy bounds](entropy_bounds.md) develops the common information argument: binary distinguishability, purified orbits, and the global logarithmic floor.
3. [Circuit bounds](circuit_bounds.md) combines this argument with causal geometry, proves both finite bounds and both asymptotic laws, and states feasibility exceptions.
4. [Constructions](constructions.md) supplies exact states, spectra, strongly symmetric gates, local seed propagation, and shared-seed resource accounting.
5. [Continuous time](continuous_time.md) replaces exact causal independence by a shell-cut estimate. Its small auxiliary registers preserve the logarithmic gain.
6. [Finite shared-seed budget](shared_seed_budget.md) gives the matched law at unit fidelity, its finite-depth and continuous-time proofs, and bounds at imperfect fidelity.
7. [Scope and robustness](scope_and_robustness.md) proves what survives charge leakage and gives counterexamples for weaker assumptions.
8. [Interpretation](interpretation.md) connects the laws to physical preparation and other notions of mixed-state order.

The [related-work comparison](../references/related_work.md) owns the attribution and comparison with existing results. The [verification record](../verification/README.md) reports finite calculations and their limits.

For a route from quantum-information foundations to these proofs, use the [Watrous bridge](../learning/anchor.md), the [worked block example](../learning/worked_example.md), and the [30-milestone map](../learning/milestones.md).

Each proof page states the assumptions it uses. In particular, the static and product-input orbit bounds do not require symmetry once their Gram and fidelity promises hold. Exact strong symmetry is essential to the shared-classical causal-volume argument. The upper constructions satisfy all the main assumptions simultaneously.
