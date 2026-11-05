# Finite-size circuit bounds

[Model](model.md) · [Entropy tools](entropy_bounds.md) · [Circuit frontiers](circuit_bounds.md) · [Constructions](constructions.md) · [Scope and robustness](scope_and_robustness.md)

The optimization and resource classes are defined in the [model](model.md). Write $`\mathcal P_D`$ for product-resource depth-$`D`$ outputs and $`\mathcal C_D`$ for their convex hull under an initially shared classical variable. A circuit layer is the tensor product of its disjoint-support channels; a hidden common noise source is not part of $`\mathcal P_D`$.

For explicit finite formulas, use a nearest-neighbor, one- or two-site gate convention on $`\{1,\ldots,L\}^d`$, with $`N=L^d`$. A range-$`a`$ convention replaces the causal radius $`D`$ below by $`aD`$; all headline scalings change only fixed constants. The lower bounds allow arbitrary finite local apparatus dimensions and channels that need not preserve $`Q`$ during the circuit; only the promised final-state conditions are imposed. The upper constructions use bounded local workspace and preserve the global charge at every step.

Throughout,

```math
C_{ij}=\mathrm{Tr}(\rho Z_iZ_j),\qquad
f_{ij}=F(\rho,Z_iZ_j\rho Z_iZ_j),\qquad
h=h_2((1+c)/2),\quad w(c)=1-h.
```

The headline promises are $`C\preceq\kappa I`$, all distinct-pair $`f_{ij}\ge c\gt 0`$, and $`Q\rho=\rho`$. The first family of lower bounds below does not need the symmetry promise.

## Independent output regions

### Lemma B1: Exact output factorization

For a state prepared in $`\mathcal P_D`$, let $`A_1,\ldots,A_K`$ be output regions whose backward causal cones are disjoint. Then

```math
\rho_{A_1\cdots A_K}=\bigotimes_{b=1}^K\rho_{A_b}.
\tag{B1}
```

A sufficient geometric condition is $`\mathrm{dist}(A_b,A_{b'})\gt 2D`$.

**Proof.** Include every apparatus wire and classical register in the causal circuit. Pull back a product of arbitrary observables on the output regions through the adjoint channels. No gate intersects the active cones of two different regions; otherwise their backward cones would overlap. At each layer the pulled-back product consequently remains the product of the separately pulled-back observables. At the initial layer these observables occupy disjoint sets of sites. The initial state factors across those sets, so the expectation of every such product factors. This is equivalent to (B1). Local resets and measurements do not change the argument because the complete unconditioned channels are CPTP. Conditioning on a collection of measurement outcomes would be a different statement and is not being done here.

### Theorem B2: Independent-region orbit bound

Suppose (B1) holds. In each $`A_b`$, choose $`M_b=2^{q_b}`$ sites with ordinary Gram $`C_b`$, and suppose all pair root fidelities within the chosen list are at least $`c_b`$. Then

```math
2S(\rho)\ge
\sum_{b=1}^K\left[S(C_b/M_b)-q_bh_2((1+c_b)/2)\right].
\tag{B2}
```

If $`C_b\preceq\kappa_b I`$, one may in particular use

```math
S(\rho)\ge\frac12\sum_{b=1}^K
[q_bw(c_b)-\log\kappa_b]_+.
\tag{B3}
```

**Proof.** For the multi-label $`a=(a_1,\ldots,a_K)`$, set

```math
U_a=\prod_{b=1}^K Z_{b,a_b}.
```

All these operators commute. Output factorization gives

```math
G_{aa'}=\mathrm{Tr}\!\left(\rho\prod_bZ_{b,a_b}Z_{b,a'_b}\right)
=\prod_b(C_b)_{a_ba'_b}.
```

Hence the normalized orbit Gram is $`\bigotimes_b(C_b/M_b)`$, of entropy $`\sum_bS(C_b/M_b)`$.

Use all $`\sum_bq_b`$ label bits in the tree proof. If one bit in block $`b`$ changes, all other labels remain identical. The two physical orbit states therefore differ, after a common unitary conjugation, by precisely one $`Z_iZ_j`$ from that block. Its fidelity is at least $`c_b`$. [Theorem E3](entropy_bounds.md#theorem-e3-unitary-orbit-entropy-bound) proves (B2). The Gram-norm estimate proves the same statement with each bracket replaced by $`q_bw(c_b)-\log\kappa_b`$. Regions with negative such brackets can be omitted before applying the theorem, proving (B3).

This proof uses the unconditional factorization (B1). Conditional factorization given a global seed does not suffice: averaging generally destroys the tensor-product Gram structure. Neither symmetry nor sector support is used in Theorem B2.

### Corollary B3: Explicit finite-grid lower bound

For $`1\le b\le L`$, define

```math
p_D(b)=\left\lfloor\frac{L+2D}{b+2D}\right\rfloor,
\qquad q(b)=\lfloor\log(b^d)\rfloor.
\tag{B4}
```

Any $`\rho\in\mathcal P_D`$ satisfying the Gram and fidelity promises in the [model](model.md), even without the symmetry promise, obeys

```math
S(\rho)\ge\frac12\max_{1\le b\le L}
p_D(b)^d[q(b)w(c)-\log\kappa]_+.
\tag{B5}
```

**Proof.** Along each axis place intervals of $`b`$ sites beginning at $`1+j(b+2D)`$, for $`j=0,\ldots,p_D(b)-1`$. Their Cartesian products give $`p_D(b)^d`$ boxes. Distinct boxes are separated by at least $`2D+1`$, so Lemma B1 applies. Each box contains $`b^d`$ sites; select any $`2^{q(b)}`$ of them. Principal Gram matrices inherit the bound $`\kappa I`$. Apply (B3) and optimize $`b`$. Taking $`b=L`$ also recovers the global logarithmic floor, so (B5) remains meaningful at and beyond the diameter.

## Shared-classical preparations and strong symmetry

### Lemma B4: Strong symmetry in every shared-seed branch

If $`\rho=\sum_rp_r\rho_r`$ and $`Q\rho=\rho`$, then every positive-weight $`\rho_r`$ obeys $`Q\rho_r=\rho_r`$.

**Proof.** Write $`\Pi_-=(I-Q)/2`$. The nonnegative numbers $`\mathrm{Tr}(\Pi_-\rho_r)`$ average to zero, so each is zero. For a positive state, zero weight in this subspace means its support is contained in the complementary subspace: $`\|\rho_r^{1/2}\Pi_-\|_2^2=0`$. Hence $`\Pi_-\rho_r=\rho_r\Pi_-=0`$.

Since $`QZ_iQ=-Z_i`$, every such branch has $`\mathrm{Tr}(\rho_rZ_i)=0`$. At sites with disjoint backward cones, the branch's joint $`Z`$-measurement law is therefore the same uniform product law. Averaging over $`R`$ preserves that law. This argument does not assume that branch fidelities obey the target promise; fidelity is used only for the unconditional state.

### Theorem B5: Finite causal-volume lower bound

Let $`\rho\in\mathcal C_D`$ have exact strong symmetry. Choose $`m`$ sites with disjoint backward cones, one designated as a reference, and suppose their reference-pair root fidelities are at least $`c`$. Then

```math
S(\rho)\ge(m-1)w(c).
\tag{B6}
```

For the nearest-neighbor grid, the all-pair fidelity promise allows

```math
m_D=\left\lceil\frac L{2D+1}\right\rceil^d,
\qquad S(\rho)\ge(m_D-1)w(c).
\tag{B7}
```

No Gram-norm promise is needed for this theorem.

**Proof.** By Lemma B4 the selected $`Z`$ outcomes are uniformly independent, even after averaging the shared seed. Their $`m-1`$ relative parities to the reference are therefore uniform. Apply [Proposition E5](entropy_bounds.md#proposition-e5-commuting-binary-twirls) to the commuting involutions $`Z_iZ_{\rm ref}`$. A grid of spacing $`2D+1`$ has the stated number of sites.

### Corollary B6: Complete finite shared-classical bound

Combining (B7) and the [global logarithmic floor](entropy_bounds.md#corollary-e4-global-logarithmic-floor) gives the complete finite shared-classical lower bound

```math
S(\rho)\ge\max\left\{(m_D-1)w(c),
\frac12[\lfloor\log N\rfloor w(c)-\log\kappa]_+\right\}.
\tag{B8}
```

## Construction inputs and finite-depth feasibility

The complete upper proofs and exact spectra are in [constructions](constructions.md): [Proposition C1](constructions.md#proposition-c1-exact-spectrum), [Proposition C2](constructions.md#proposition-c2-strict-product-masks), [Proposition C3](constructions.md#proposition-c3-shared-classical-masks), and [Proposition C4](constructions.md#proposition-c4-depth-and-resource-bounds). The following consequences suffice for the frontier.

Partition each coordinate into intervals of at most $`b`$ sites. There are $`K=\lceil L/b\rceil^d`$ connected rectangular blocks, of sizes $`m_B\le b^d`$, and $`m_*:=\max_Bm_B`$. The construction propositions give exact entropy

```math
S_{\rm prod}=K-1+\sum_B\lceil\log m_B\rceil,
\qquad
S_{\rm sh}=K-1+\lceil\log m_*\rceil,
\tag{B9}
```

and in particular the bounds

```math
S_{\rm prod}\le K[1+\lceil d\log b\rceil]-1,
\qquad
S_{\rm sh}\le K-1+\lceil\log N\rceil.
```

Every output has exact strong symmetry, $`C=I`$, and $`f_{ij}=1`$. Both preparations have depth at most $`A_db`$, where the conservative fixed constant $`A_d=64(d+1)^2`$ covers the explicit tree schedules. Indeed, a block tree has height at most $`d(b-1)`$, degree at most $`2d`$, and at most $`\lceil d\log b\rceil`$ streamed mask bits. The quoted depth-and-resource proposition supplies a constant number of edge-color layers per streamed round. This charges actual seed propagation in the product model; only the shared-classical model supplies the seed before the run.

### Constant-depth baseline

Taking singleton blocks and a nearest-neighbor Hamiltonian path in the construction gives

```math
\rho_*=(I+Q)/2^N,
\qquad S(\rho_*)=N-1,
\qquad C(\rho_*)=I,
\qquad f_{ij}(\rho_*)=1.
\tag{B10}
```

The path has two edge colors, so this state is available in $`\mathcal P_2`$. In $`\mathcal C_0`$, sample an even-parity string of local $`X`$ eigenvalues and initialize the corresponding product state; the same state is available at depth zero.

### Small-depth exceptions

In the explicit two-site-gate model, exact strong symmetry and nonzero all-pair fidelity make $`\mathcal P_0`$ infeasible for $`N\ge2`$: a product state in one global $`X`$ sector has every site in a pure $`X`$ eigenstate, and distinct-pair conjugation produces an orthogonal state.

For $`N\ge3`$, $`\mathcal P_1`$ is also infeasible. The output factors into components of at most two sites. If $`\rho=\bigotimes_B\rho_B`$ has $`\mathrm{Tr}(Q\rho)=1`$, then $`\prod_B\mathrm{Tr}(Q_B\rho_B)=1`$; each real factor has absolute value at most one, so each component occupies a sharp local charge sector. A pair supported in different components flips both local sectors and has fidelity zero. For $`N=2`$, one dephasing gate suffices. Larger elementary supports change these finite thresholds; the existence of a fixed implementation threshold and the asymptotic laws do not depend on this convention. One-site endpoints have no distinct pair and are not assigned a positive entropy cost by the finite inequalities.

## Theorem B7: Matched circuit frontiers

Fix $`d\ge1`$, $`0\lt c\le1`$, and $`\kappa\ge1`$. Set

```math
\ell_D=\min\{L,D+1\}.
```

There are positive constants depending only on $`d,c,\kappa`$ and a threshold $`L_0`$ with the same dependence such that, for all $`L\ge L_0`$,

```math
S_{\min}^{\mathrm{prod}}(N,D)
=\Theta_{d,c,\kappa}\!\left[
\frac{N}{\ell_D^d}\log(\ell_D+1)\right]
\quad(D\ge2),
\tag{B11}
```

```math
S_{\min}^{\mathrm{sh}}(N,D)
=\Theta_{d,c,\kappa}\!\left[
\frac{N}{\ell_D^d}+\log N\right]
\quad(D\ge0).
\tag{B12}
```

The constants are uniform in $`N`$ and $`D`$. The exact finite lower bounds (B5) and (B8), and the [construction consequences](#construction-inputs-and-finite-depth-feasibility), apply before this asymptotic threshold as well.

**Product lower bound.** Choose an integer $`b_0\ge2`$, depending only on $`c,\kappa,d`$, such that

```math
d\log b_0\ge 2\log\kappa/w(c)+1.
```

Assume $`L\ge b_0`$ and take $`b=\min\{L,\max\{b_0,D+1\}\}`$ in (B5). Then $`\ell_D\le b\le b_0\ell_D`$, and

```math
q(b)w(c)-\log\kappa\ge\tfrac12q(b)w(c).
```

Moreover $`p_D(b)\ge L/(6b)`$: if $`D\lt L`$, then $`b\ge D+1`$ and $`b+2D\le3b`$, and the floor of a number at least one is at least half that number; if $`D\ge L`$, then $`b=L`$ and $`p_D(b)=1`$. Finally

```math
q(b)\ge\frac{d}{4}\log(b+1)\ge\frac{d}{4}\log(\ell_D+1).
```

Thus (B5) gives, for example,

```math
S(\rho)\ge
\frac{w(c)d}{16\,6^d b_0^d}
\frac{N}{\ell_D^d}\log(\ell_D+1).
```

This entire lower-bound argument is independent of symmetry.

**Shared-classical lower bound.** The [global logarithmic floor](entropy_bounds.md#corollary-e4-global-logarithmic-floor) is at least $`\tfrac14w(c)\log N`$ once $`\log N\ge2+2\log\kappa/w(c)`$. If $`m_D\ge2`$, then $`m_D-1\ge m_D/2`$ and (B7) controls $`N/\ell_D^d`$ up to a constant depending on $`d,c`$. If $`m_D=1`$, then $`\ell_D\ge L/2`$, so $`N/\ell_D^d\le2^d`$ and the logarithmic bound also controls this bounded term. Taking the maximum of the two lower bounds is equivalent, up to a constant factor, to their sum. This proves the lower half of (B12).

**Upper bounds.** For $`D\ge A_d`$, use the block construction with

```math
b=\min\{L,\lfloor D/A_d\rfloor\}.
```

Then $`b\ge\ell_D/(4A_d)`$, $`K\le(2L/b)^d`$, and the product upper bound in (B9) gives the upper half of (B11). The shared upper bound in (B9) gives the upper half of (B12). For $`2\le D\lt A_d`$, the depth-two baseline (B10) has entropy $`N-1`$, which is within a constant factor of the right side of (B11). For $`0\le D\lt A_d`$, the shared-classical depth-zero baseline does the same for (B12). All upper outputs have $`c=1`$, $`\kappa=1`$, and exact strong symmetry.

At $`D\gtrsim L`$, (B11) is $`\Theta(\log N)`$, as is (B12). Extrapolating $`N/D^d`$ beyond the diameter without this saturation would be incorrect.

## Eventual rather than all-pair fidelity

The all-pair promise can be weakened in a quantitative finite-size way. Suppose instead that

```math
f_{ij}(\rho)\ge c\quad\text{whenever }\mathrm{dist}(i,j)\ge r_f,
\tag{B13}
```

where the positive integer $`r_f`$ is fixed independently of $`N`$ and depth.

For the causal-volume bound use sites on a grid of spacing

```math
g=\max\{2D+1,r_f\},
\qquad m=\lceil L/g\rceil^d.
```

For an orbit bound inside a side-$`b`$ box, retain the subgrid of spacing $`r_f`$. It has $`\lceil b/r_f\rceil^d`$ points, so replace $`q(b)`$ in (B5) by

```math
q_{r_f}(b)=\left\lfloor\log\big(\lceil b/r_f\rceil^d\big)\right\rfloor.
\tag{B14}
```

Every distinct chosen pair is separated by at least $`r_f`$. Global and within-box principal Gram bounds remain valid. The preceding proofs are otherwise unchanged.

For fixed $`r_f`$, the same asymptotic frontiers follow with constants and the finite-size threshold also depending on $`r_f`$: choose the minimum box size large enough to contain the required fixed number of separated labels. The existing upper constructions satisfy the stronger all-pair promise.

If $`r_f`$ grows with $`N`$, retain the explicit packing and subgrid formulas; do not absorb it into a constant. A thermodynamic limiting statement with no uniform finite-$`N`$ lower bound and no density of admissible pairs is not by itself assumption (B13). The order of thermodynamic and separation limits cannot be exchanged silently.

## Scope of the conclusion

The [robustness account](scope_and_robustness.md) proves a dimension-free sector-leakage correction, explains why the product orbit bound is sector-independent, and gives counterexamples to replacing the Gram promise by qualitative correlation decay. These circuit results do not identify depth with physical time in an arbitrary implementation; the [continuous-time account](continuous_time.md) states its generator assumptions separately. The upper channel construction is not a claim of exact finite-time complete dephasing by a bounded finite-rate system-only Lindbladian.
