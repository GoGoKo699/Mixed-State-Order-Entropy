# Model and operational question

The resource is the mixedness left in a many-body state after local preparation. We ask for the least possible final von Neumann entropy at a prescribed preparation depth, subject to finite global fidelity order and bounded ordinary correlations. Two preparation models distinguish initially independent local apparatus from apparatus coordinated by a preshared classical seed.

## State, geometry, and order

Let $`\Lambda=\{1,\ldots,L\}^d`$ be a cubic lattice with open boundaries, $`N=L^d`$, and fixed spatial dimension $`d`$. Each site retains one qubit. Additional apparatus lives at lattice sites or bounded-diameter lattice cells. The Pauli operators on retained site $`i`$ are $`X_i,Z_i`$. Set

```math
Q=\prod_{i\in\Lambda}X_i,
\qquad Q\rho=\rho.
```

This is a strong symmetry: the entire support of $`\rho`$ lies in one charge sector. Choosing the other sector gives the same bounds. In particular $`\mathrm{Tr}(\rho Z_i)=0`$. The weaker condition $`Q\rho Q=\rho`$ alone does not supply the shared-seed lower bound.

Throughout, fidelity means **root Uhlmann fidelity**:

```math
F(\rho,\sigma)=\left\|\sqrt\rho\sqrt\sigma\right\|_1,
\qquad
f_{ij}=F(\rho,Z_iZ_j\rho Z_jZ_i)
=\left\|\sqrt\rho Z_iZ_j\sqrt\rho\right\|_1.
```

Fix $`0\lt c\leq1`$ independently of $`N`$ and require $`f_{ij}\geq c`$ for distinct selected sites. The headline optimization uses all distinct sites. If the promise starts only beyond a fixed microscopic separation, select a fixed-spacing sublattice; the same asymptotic laws hold with changed constants. Statements based only on a nonuniform or iterated infinite-distance limit require their own uniformity argument.

The ordinary correlation Gram matrix is

```math
C_{ij}=\mathrm{Tr}(\rho Z_iZ_j),
\qquad 0\preceq C\preceq\kappa I,
```

where $`\kappa\geq1`$ is independent of system size and preparation depth. The exact special case $`C=I`$ has zero ordinary $`Z_iZ_j`$ correlations at every distinct pair. Uniformly summable spatial correlations imply the norm condition; for example a uniform exponential bound at fixed correlation length gives fixed $`\kappa`$. Merely requiring qualitative decay, or a fixed entrywise error $`|C_{ij}|\leq\epsilon`$, does not imply it. The proofs use the matrix inequality as stated.

These are finite-system global fidelity conditions, following the global SWSSB framework in [Lessa et al.](../references/related_work.md). They do not identify global fidelity order with a local one-point diagnostic or assert an infinite-volume phase classification. The [interpretation](interpretation.md) explains that distinction.

## What is charged

The output cost, in bits, is

```math
S(\rho)=-\mathrm{Tr}(\rho\log_2\rho).
```

It is an actual property of the retained state. For a pure dilation it equals entanglement entropy with the complete discarded apparatus. A thermodynamic work or heat cost needs additional assumptions and is not part of this optimization.

A depth-$`D`$ preparation consists of $`D`$ layers of bounded-range local quantum channels. Gates within a layer act on disjoint physical cells, and the layer is the tensor product of those channels; an implicit common noise source is not supplied in the product model. A constant number of coloring layers changes only constants. A local channel may use local apparatus, measurements, classical registers, and discarded systems. Adaptive classical signals generated during preparation obey the same spatial causal constraint. No postselection is allowed.

Initial nonlocal quantum entanglement is not supplied. Local mixed inputs can be purified by further local apparatus, so allowing them does not weaken the product-input converses. The circuit construction uses bounded active local workspace, with local resets and signal propagation. The direct fully coherent Hamiltonian implementation retains logarithmically many ancillary qubits per site until its final discard; its total instantaneous local generator strength remains bounded. These are distinct memory statements. Fixed, spatially dependent classical control instructions are part of the known protocol.

| Preparation model | Initial resource and controls |
|---|---|
| Product model | The complete initial system and apparatus state factors over sites. All random sources are local and independent. A seed broadcast during the run is charged to the depth. |
| Shared-classical model | A classical variable $`R`$ may be distributed before the charged run. Conditioned on $`R`$, the initial state factors over sites and the preparation is local. The output averages over $`R`$. No outcome-dependent nonlocal communication during the run is supplied. |

The latter model includes fully separable initial resources with arbitrary classical correlations. A preshared seed is an explicit resource; it is not equivalent to a globally acting quantum gate or to free nonlocal feedback after measurements. Any retained seed register would be part of the output whose entropy is charged; here the retained output is precisely the $`N`$ spins.

The lower bounds permit arbitrary local channels with the stated final-state conditions. The matching preparations can be chosen strongly symmetric at every step. They therefore also attain the bounds in the more restrictive strongly symmetric preparation class.

## Optimization and scaling convention

For fixed $`d,c,\kappa`$ and local gate range, let $`S_{\min}^{\mathrm{prod}}(N,D)`$ and $`S_{\min}^{\mathrm{sh}}(N,D)`$ be the infima of output entropy over the two classes, subject to the order and ordinary-correlation conditions above. An empty feasible class has infimum $`+\infty`$.

Write

```math
\ell_D=\min\{L,D+1\}.
```

For sufficiently large $`N`$ and depth above a fixed implementation threshold, the [circuit bounds](circuit_bounds.md) and [constructions](constructions.md) give

```math
S_{\min}^{\mathrm{prod}}(N,D)
=\Theta_{d,c,\kappa}\!\left(
\frac{N}{\ell_D^d}\log_2(\ell_D+1)\right),
```

```math
S_{\min}^{\mathrm{sh}}(N,D)
=\Theta_{d,c,\kappa}\!\left(
\frac{N}{\ell_D^d}+\log_2N\right).
```

Gate range and fixed implementation constants are also included in the implicit constants. The explicit finite inequalities in the proof pages retain additive losses and do not assert a positive entropy for a one-site or otherwise infeasible endpoint. Near and beyond diameter depth both laws have scale $`\log N`$; increasing the allowed depth further cannot remove the preparation-independent entropy floor.

The [continuous-time account](continuous_time.md) specifies its generator assumptions and the corresponding time variable separately. Circuit depth is not silently identified with elapsed time in an arbitrary physical implementation.
