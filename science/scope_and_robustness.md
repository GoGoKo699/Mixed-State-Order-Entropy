# Scope and robustness

[Model](model.md) · [Entropy tools](entropy_bounds.md) · [Circuit frontiers](circuit_bounds.md) · [Constructions](constructions.md) · [Scope and robustness](scope_and_robustness.md)

The headline optimizations concern actual retained-state von Neumann entropy, root fidelity, and a uniformly bounded ordinary correlation Gram matrix. This page records which assumptions can be relaxed and where the preparation frontiers genuinely fail. It supplements the [finite circuit theorems](circuit_bounds.md) rather than changing their hypotheses. Write $`w(c)=1-h_2((1+c)/2)`$.

## Sector leakage

The [static orbit bound](entropy_bounds.md#corollary-e4-global-logarithmic-floor), [independent-region bound](circuit_bounds.md#theorem-b2-independent-region-orbit-bound), and [grid bound](circuit_bounds.md#corollary-b3-explicit-finite-grid-lower-bound) do not use symmetry. Therefore, with the actual Gram and fidelity promises retained, the strict-product frontier is unchanged even if the symmetry promise is removed. The upper states remain admissible because they are exactly strongly symmetric. Symmetry is load-bearing for the shared-classical causal-volume term.

Define leakage into the opposite sector by

```math
\epsilon=\mathrm{Tr}(\Pi_-\rho),\qquad \Pi_-=(I-Q)/2,
\qquad 0\le\epsilon\le\tfrac12.
\tag{R1}
```

No commutation of $`\rho`$ with $`Q`$ is assumed. Write $`\epsilon_r=\mathrm{Tr}(\Pi_-\rho_r)`$ for a shared-seed branch.

### Proposition R1: Dimension-free leakage correction

Under the hypotheses of the [finite causal-volume theorem](circuit_bounds.md#theorem-b5-finite-causal-volume-lower-bound) except exact sector support,

```math
S(\rho)\ge(m-1)w(c)-4m\epsilon(1-\epsilon).
\tag{R2}
```

**Proof.** Since $`Q`$ and $`Z_i`$ anticommute and square to the identity,

```math
|\langle Z_i\rangle_r|^2+|\langle Q\rangle_r|^2\le1.
```

Indeed, for real $`a=\langle Z_i\rangle_r`$, $`b=\langle Q\rangle_r`$, the operator $`aZ_i+bQ`$ has norm $`\sqrt{a^2+b^2}`$, while its expectation is $`a^2+b^2`$. Since $`\langle Q\rangle_r=1-2\epsilon_r`$, the branch bias $`\mu_{i,r}`$ obeys

```math
\mu_{i,r}^2\le4\epsilon_r(1-\epsilon_r).
```

The elementary binary entropy inequality

```math
h_2((1+x)/2)\ge1-x^2,\qquad |x|\le1,
\tag{R3}
```

then bounds each selected bit's entropy. One proof of (R3) expands the entropy deficit as a power series with positive coefficients summing to one at $`x=1`$; every power $`x^{2n}`$ is at most $`x^2`$.

Conditional on $`R=r`$, disjoint cones make the selected bits independent. Concavity of Shannon entropy and of $`\epsilon(1-\epsilon)`$ gives

```math
H(Z_1,\ldots,Z_m)
\ge H(Z_1,\ldots,Z_m\mid R)
\ge m[1-4\epsilon(1-\epsilon)].
```

Passing to the $`m-1`$ reference parities loses at most one bit. Apply the [commuting-twirl bound](entropy_bounds.md#proposition-e5-commuting-binary-twirls) to the unconditional state, whose reference-pair fidelities satisfy the stated promise. This yields (R2). In particular, no branch-fidelity assumption, projection onto a charge sector, or dimension-dependent continuity estimate is used.

For a fixed allowed leakage $`\epsilon_0\le1/2`$ satisfying

```math
4\epsilon_0(1-\epsilon_0)\lt w(c),
\tag{R4}
```

the [shared-classical frontier](circuit_bounds.md#theorem-b7-matched-circuit-frontiers) is unchanged, with constants depending also on $`\epsilon_0`$. For large $`m`$, (R2) has a positive constant coefficient of $`m`$; for bounded $`m`$, the unchanged global logarithmic floor controls the remaining term. The exactly symmetric upper construction remains in the allowed class.

This sufficient leakage range is not asserted to be sharp. A small commutator $`[Q,\rho]`$ does not imply small leakage; weak symmetry alone is insufficient. If one instead assumes $`\|Q\rho-\rho\|_1\le\eta`$, then $`2\epsilon\le\eta`$, so (R2) applies with that inferred bound. A global projection onto the desired sector would in general be nonlocal postselection and is not a permitted repair.

### Counterexample R2: Failure at leakage c/2

Let $`r=\lceil\log N\rceil`$, choose distinct $`a_i\in\mathbb F_2^r`$, and sample independent uniform $`y\in\mathbb F_2^r`$, $`u\in\mathbb F_2`$. Let $`\sigma_{\rm diag}`$ be the computational-basis mixture with signs $`(-1)^{u+a_i\cdot y}`$. It is a mixture of product states with entropy at most $`r+1`$, has $`C=I`$, commutes with every pair $`Z_iZ_j`$, and has $`\mathrm{Tr}(Q\sigma_{\rm diag})=0`$. It is also weakly symmetric because the uniform bit $`u`$ implements global bit flip.

The shared-classical depth-zero state

```math
\rho_c=(1-c)|+\rangle\langle+|^{\otimes N}+c\,\sigma_{\rm diag}
\tag{R5}
```

has $`C=I`$, leakage $`\epsilon=c/2`$, and $`f_{ij}\ge c`$ by joint concavity of fidelity. Its entropy is at most

```math
h_2(c)+c(r+1)=O_c(\log N).
```

Thus leakage $`c/2`$ really can destroy the shared-classical causal-volume term. The interval between the sufficient condition (R4) and this obstruction is not resolved here.

All robustness statements concern the *actual* output's Gram and fidelity promises. A fixed trace-distance error relative to an ideal state does not automatically preserve a bounded ordinary Gram norm: entrywise errors can accumulate over $`N`$ sites. The result should not be advertised as robustness to arbitrary fixed preparation noise without checking these observables.

## Bounded Gram norm versus qualitative clustering

Exact strong symmetry makes every $`\langle Z_i\rangle`$ zero, so $`C`$ is also the connected correlation matrix. A sufficient physical condition for $`C\preceq\kappa I`$ is the uniform absolute-summability bound

```math
\sup_i\sum_j|C_{ij}|\le\kappa.
\tag{R6}
```

For example, a fixed exponential correlation-length bound, with system-size-independent prefactor and length, gives a fixed $`\kappa`$ on a fixed-dimensional lattice. An algebraic bound $`|C_{ij}|\le A(1+\mathrm{dist}(i,j))^{-\alpha}`$ is sufficient when $`\alpha\gt d`$. These implications follow directly from row-sum norm bounds and lattice shell counting.

Merely having $`C_{ij}\to0`$ as separation grows is weaker. Even a uniform entrywise estimate $`|C_{ij}|\le\eta`$ for $`i\ne j`$ gives only $`\|C\|\le1+(N-1)\eta`$. It does not provide a fixed $`\kappa`$. If the known norm is $`\kappa_N`$, the exact finite inequalities remain true with $`\log\kappa_N`$, but the claimed fixed-$`\kappa`$ asymptotics cannot be inferred automatically.

### Counterexample R3: Vanishing pair correlations with smaller entropy

For $`a=1,\ldots,M`$, independently sample a sign pattern $`s^{(a)}\in\{\pm1\}^N`$ and form the even cat, where $`|s\rangle`$ denotes the computational-basis string with $`Z_i`$ eigenvalue $`s_i`$:

```math
|\mathrm{cat}(s)\rangle=(|s\rangle+|-s\rangle)/\sqrt2.
```

Set $`\tau=M^{-1}\sum_a|\mathrm{cat}(s^{(a)})\rangle\langle\mathrm{cat}(s^{(a)})|`$. It has exact strong symmetry and is fixed by conjugation with every $`Z_iZ_j`$, so $`f_{ij}=1`$. Its entropy is at most $`\log M`$, while

```math
C_{ij}=M^{-1}\sum_a s_i^{(a)}s_j^{(a)}\quad(i\ne j).
```

Hoeffding's inequality and a union bound give a positive-probability choice with all $`|C_{ij}|\le\eta`$ whenever, for example,

```math
M\ge\frac{2}{\eta^2}\ln(2N^2).
```

Taking $`\eta_N=(\log N)^{-1/4}`$ yields uniformly vanishing ordinary pair correlations and $`S(\tau)=O(\log\log N)`$, despite maximal pair fidelity. Its ordinary Gram rank is at most $`M`$, so $`\|C\|\ge N/M`$; the bounded-Gram promise fails substantially.

Thus the global logarithmic floor is a theorem about the stated uniformly controlled correlation class, not every state satisfying a qualitative SWSSB definition. The broader causal-volume theorem under local preparation remains a separate result with different assumptions.

## Other interpretation limits

The fidelity promise is about the full retained state. It does not become a one-point local-marginal fidelity statement. The [eventual-pair extension](circuit_bounds.md#eventual-rather-than-all-pair-fidelity) requires a fixed finite separation threshold and uniform finite-size bounds, not an unexamined exchange of infinite-volume and infinite-distance limits.

Output entropy is unconditional after the preparation records have been discarded. It equals entanglement with a complete discarded apparatus when the overall initial state and dilation are pure. Additional thermodynamic assumptions would be needed to identify it with heat or work. In the shared-classical model, conditioning on a retained seed is a different cost function. The model and bounds do not charge such a conditional entropy.

The matching circuit claims use local channels, for which exact dephasing is a permitted CPTP gate with a local apparatus implementation. The separate [continuous-time theorem](continuous_time.md) proves matching bounds using bounded local Hamiltonians, explicit apparatus, and final discard. A finite-rate system-only Lindbladian does not perform exact complete dephasing in finite time; that more restrictive upper-bound model is not asserted here.

The [related-work comparison](../references/related_work.md) credits the fidelity interpretation, information inequalities, causal bounds, and classical masking antecedents. The contribution claimed is the model-matched preparation frontier and the quantitative role of initially shared classical coordination.
