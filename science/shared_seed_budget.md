# Retained entropy with a finite shared seed

[Model](model.md) · [Circuit bounds](circuit_bounds.md) · [Constructions](constructions.md) · [Continuous time](continuous_time.md)

How much preshared randomness removes the logarithmic entropy cost of independent preparation? At maximal pair fidelity, each bit of shared entropy can replace one bit of independent mask entropy in every causal volume. The replacement saturates at the logarithm of that volume. A causal-volume contribution and a global logarithmic contribution remain.

## Resource and matched law

Use the [lattice preparation model](model.md). The complete system and apparatus start in a spatial product conditioned on a common classical variable $`R`$. The initial states and local schedules can depend on $`R`$. The budget is $`H(R)\le h`$ bits for the supplied variable. Local independent randomness is available within the original depth or time model. A signal sent during preparation obeys the ordinary spatial propagation constraint. The retained output $`\rho`$ averages over the seed and all apparatus records and has strong charge $`Q\rho=\rho`$, bounded ordinary Gram matrix $`C\preceq\kappa I`$, and pair **root** fidelities $`f_{ij}\ge c`$. The budget concerns the entropy of the preclock common variable itself. The preparation model supplies its distribution in space.

For the nearest-neighbor circuit, write

```math
\ell_D=\min\{L,D+1\},\qquad V=\ell_D^d,\qquad K=N/V,
\qquad [x]_+=\max\{x,0\}.
```

At $`c=1`$, for fixed dimension and $`\kappa\ge1`$, the infimum of the retained entropy satisfies

```math
\boxed{
S_{\min}(N,D;h,1,\kappa)
=\Theta_{d,\kappa}\!\left(K+\log_2 N+K[\log_2 V-h]_+\right).
}
```

The constants are uniform in $`h\ge0`$ and $`D\ge2`$ for sufficiently large $`N`$. Fixed gate range changes geometric constants, with the same result above a fixed feasible depth. The bounded-generator version below has the same law with a causal volume set by the elapsed time.

In a regime with $`K\gg\log_2N`$, reducing the entropy to order $`K`$ requires $`h\ge\log_2 V-O(1)`$, and $`\log_2 V+O(1)`$ bits suffice. Near diameter depth the global logarithmic floor dominates the change due to the seed. At zero seed the formula recovers the product-input law.

## Finite circuit lower bound at maximal fidelity

Select $`p\ge1`$ nonempty regions of sizes $`m_1,\ldots,m_p`$ with disjoint backward cones. Measure their physical $`Z`$ strings $`Y_1,\ldots,Y_p`$ mathematically, and define $`u_b=[\log_2(m_b/\kappa)]_+`$. For each choice of distinguished region $`j`$,

```math
S(\rho)\ge p-1+u_j+\sum_{b\ne j}[u_b-h]_+.
```

To see this, unit pair fidelity forces $`\rho`$ to commute with all $`Z_iZ_j`$. The simultaneous eigenspaces consist of complementary strings. The strong charge fixes the even cat within each such space. Each pair of complementary outcomes of the all-site $`Z`$ measurement therefore has equal probability, and

```math
H(Z_{\rm all})=S(\rho)+1.
```

By [strong symmetry in each positive-weight seed branch](circuit_bounds.md#lemma-b4-strong-symmetry-in-every-shared-seed-branch), every regional string and its complement have equal probability conditioned on $`R`$. Thus $`H(Y_b\mid R)\ge1`$. In the unconditional regional law, a string $`y\in\{\pm1\}^{m_b}`$ with probability $`p_y`$ and its complement contribute $`2p_y yy^{\mathsf T}`$ to the ordinary Gram matrix. All other contributions are positive. Its principal Gram bound gives $`2p_y m_b\le\kappa`$. Consequently $`H(Y_b)\ge1+u_b`$. The seed can lower this entropy by at most $`I(R:Y_b)\le h`$.

By [disjoint-cone factorization](circuit_bounds.md#lemma-b1-exact-output-factorization), the regional strings are jointly independent conditioned on the seed. Order the regions with $`j`$ first. The chain rule, monotonicity under conditioning, and factorization then give

```math
\begin{aligned}
H(Z_{\rm all})
&\ge H(Y_1,\ldots,Y_p) \\
&\ge H(Y_j)+\sum_{b\ne j}H(Y_b\mid R) \\
&\ge p+u_j+\sum_{b\ne j}[u_b-h]_+ .
\end{aligned}
```

The first region supplies its unconditional entropy. The remainder pay only for the part their shared seed cannot explain. The static bound $`S(\rho)\ge[\log_2(N/\kappa)]_+`$ follows directly by taking the entire lattice as one region. The [shared-classical packing bound](circuit_bounds.md#theorem-b5-finite-causal-volume-lower-bound) also applies independently of the budget.

## Finite construction and depth

Partition the lattice into $`p`$ rectangular blocks with sizes $`m_b`$ and bounded aspect ratio. Use the [existing strongly symmetric cat and boundary preparation](constructions.md#3-exact-cat-sector-spectrum). Set $`q_b=\lceil\log_2 m_b\rceil`$ and $`q_{\max}=\max_b q_b`$. For any integer $`0\le s\le q_{\max}`$, supply $`s`$ fair shared bits. Inside block $`b`$, use the first $`\min(s,q_b)`$ of them as its common mask coordinates. Its other $`[q_b-s]_+`$ coordinates are independent fair bits generated in that block. Within the block the complete mask label is uniform, and the site labels are the distinct binary encodings of $`0,\ldots,m_b-1`$ with label zero at the anchor.

The labels in each block include all of its coordinate vectors, so its canonical mask pattern reconstructs every coordinate used there. A largest block uses all $`s`$ common coordinates. Therefore the map from the supplied common bits and all independent bits to the joint canonical pattern is injective. The [cat-sector spectrum](constructions.md#proposition-c1-exact-spectrum) adds $`p-1`$ independent boundary phase bits. This gives the exact retained entropy

```math
S_{\rm mask}
=p-1+s+\sum_{b=1}^p[q_b-s]_+,
\qquad
s=\min\{q_{\max},\lfloor h\rfloor\}.
```

The output has $`Q\rho=\rho`$, $`C=I`$ and $`f_{ij}=1`$. Each site can be preloaded with the single mask bit computed from the shared coordinates and its fixed label. The independent coordinates use the [existing pipelined block broadcast](constructions.md#41-bounded-workspace-pipelined-broadcast), with no increase in its depth or its active workspace order. Implementing masks and boundary phases costs depth $`O_d(b)`$ for rectangular blocks of side at most $`b`$.

For the uniform upper bound choose $`b=\min\{L,\lfloor D/A_d\rfloor\}`$ for $`D\ge A_d`$, with the fixed implementation constant from the [original circuit theorem](circuit_bounds.md#theorem-b7-matched-circuit-frontiers). Then $`p=O_d(K)`$, $`q_{\max}\le\log_2 V+O_d(1)`$, and rounding the budget changes each deficit by less than one bit. The exact formula gives the stated upper scale. For $`2\le D\lt A_d`$, the existing depth-two product protocol has entropy $`N-1`$, which is the same order as the stated upper scale in that depth range.

For the lower bound before diameter depth, choose boxes of side proportional to $`D+1`$ with pairwise separation greater than $`2D`$. When $`D+1`$ is below a fixed small fraction of $`L`$, there are order $`K`$ boxes and each has $`u_b\ge\log_2 V-O_{d,\kappa}(1)`$. The finite lower bound then controls $`K[\log_2 V-h-O_{d,\kappa}(1)]_+`$. The causal-volume floor absorbs a fixed additive loss per box. When $`D+1`$ is at least that fraction of $`L`$, the global logarithmic floor controls the whole expression because $`K=O_d(1)`$ and the deficit is at most $`\log_2N`$.

### Feasibility at depths zero and one

In the one- and two-site gate convention, for $`N\ge2`$ and $`c=1`$, the least feasible shared seed entropy is $`N-1`$ at depth zero and $`\lceil N/2\rceil-1`$ at depth one. The all-site $`X`$ readout is supported on even parity by strong charge. Invariance under every $`Z_iZ_j`$ makes its law uniform on those strings, so its entropy is $`N-1`$.

In any positive-weight seed branch of a depth-zero preparation, each site has a definite local charge. At depth one the branch factors over the disjoint gate components, and every component has a definite charge since their product charge is fixed. A singleton contributes zero conditional readout entropy and a pair contributes at most one bit. There are at most $`\lfloor N/2\rfloor`$ pairs. Subtracting these bounds on conditional entropy from $`N-1`$ gives the necessary seed thresholds, including for pairings that depend on the seed. Uniform even charge signs on individual sites attain the depth-zero threshold. At depth one, take a fixed maximum nearest-neighbor matching along a lattice Hamiltonian path and supply uniform even charge signs on its components. Locally prepare the maximally mixed state of each specified charge sector in one gate layer. Both constructions yield $`(I+Q)/2^N`$ and meet the Gram promise. These feasibility thresholds precede the matched entropy law, which starts at depth two.

## Fixed imperfect fidelity

For $`0\lt c\lt 1`$, both the logarithmic order of the seed requirement and its coefficient bounds can be quantified. These use only the fidelity of the **averaged** retained state. For each of the separated regions, choose $`M_b=2^{q_b'}`$ sites and define

```math
w(c)=1-h_2((1+c)/2),
\qquad
a_b=\max\{q_b'w(c),\,c^2 q_b'-1\}.
```

A finite region bound is

```math
2S(\rho)\ge\sum_b[a_b-\log_2\kappa-h]_+ .
```

For the proof, a uniform label vector $`\mathbf a`$ selects one site in each retained region, and its orbit unitary is the product of the selected $`Z`$ operators. The normalized orbit Gram matrix $`\Gamma`$ of the actual output is an average of tensor products of the corresponding branch Gram matrices, by region factorization conditioned on $`R`$. Its marginal in region $`b`$ is $`C_b/M_b`$. Entropy concavity and the classical-label Holevo bound give

```math
S(\Gamma)\ge\sum_b S(\Gamma_b\mid R)
\ge\sum_b\bigl[q_b'-\log_2\kappa-h\bigr].
```

Here $`S(\Gamma_b\mid R)`$ is the average entropy in the classical register extension. The [orbit entropy argument](entropy_bounds.md#theorem-e3-unitary-orbit-entropy-bound) gives $`2S(\rho)\ge S(\Gamma)-\chi_S`$, where $`\chi_S`$ belongs to the system orbit states. Any two labels that differ only within one region have orbit-state root fidelity at least $`c`$. This follows by common unitary conjugation, which leaves precisely the pair product of the two respective sites. Apply the chain rule one whole region label at a time. After conditioning on the previous region labels, the states indexed by the current label are averages over all subsequent labels. Pair corresponding terms with identical subsequent labels and use joint concavity. Every pair of current-label states then has root fidelity at least $`c`$. The binary Holevo bound inside this label gives $`q_b'[1-w(c)]`$ for the term from region $`b`$.

For the other bound, fix a purification of one reference label and use Uhlmann's theorem to choose a purification of each remaining state with overlap at least $`c`$ with that reference. Their equally weighted pure-state mixture has rank at most $`M_b`$ and weight at least $`c^2`$ along the reference direction. Dephasing in a basis including that direction bounds its entropy by $`1+(1-c^2)\log_2 M_b`$. Partial trace cannot increase the Holevo information. Take the better label bound in each region and omit regions with a nonpositive contribution to obtain the displayed inequality.

The [shared-classical causal-volume and global floors](circuit_bounds.md#corollary-b6-complete-finite-shared-classical-bound) remain in force. Before the diameter cap, the finite region bound gives an entropy term of order at least $`K[c^2\log_2 V-h-O_{d,\kappa}(1)]_+`$. For any fixed $`0\lt \delta\lt c^2`$, keeping $`h\le(c^2-\delta)\log_2 V`$ preserves the logarithmic factor in the regime where it exceeds the global floor.

For achievability, a common Bernoulli flag of probability $`c`$ selects the maximal-fidelity protocol with $`s`$ common bits in that branch. The other branch outputs $`|+\rangle^{\otimes N}`$. Both branches have strong charge and $`C=I`$. Joint concavity gives $`f_{ij}\ge c`$ in the actual output. The whole shared variable has entropy $`h_2(c)+cs`$, and the retained entropy is at most $`h_2(c)+cS_{\rm mask}`$. Hence $`h\ge c\log_2 V+O_{d,c}(1)`$ suffices for order $`K+\log_2 N`$. The coefficients $`c^2`$ and $`c`$ give a bracket for the least shared entropy needed to reach that scale when $`K\gg\log_2N`$. The coefficient at intermediate fidelity remains open.

## Bounded-generator evolution

Use the [continuous-time model and bounds](continuous_time.md#2-precise-dynamical-assumptions), uniformly within each positive-weight seed branch. The generator supports can be controlled by the seed subject to the same range, overlap, and strength assumptions required by the shell-cut estimate. Let $`a`$ be the microscopic range, $`\nu`$ the overlap parameter, and $`v`$ the velocity parameter used in that account. The volume scale is

```math
V_T=\min\{L,1+vT\}^d,\qquad K_T=N/V_T .
```

At $`c=1`$ the matched law is $`\Theta(K_T+\log_2N+K_T[\log_2 V_T-h]_+)`$ for the same bounded-generator apparatus setting, above a fixed local implementation time. Below unit fidelity the preceding lower and upper coefficient bounds also apply with $`V_T`$.

For the lower bound, take $`p`$ side-$\ell$ cubes with expansions of radius $`r\ge2a`$ inside the lattice and with pairwise separation at least $`2r+2a`$, using the distance convention of the [shell-cut lemma](continuous_time.md#3-shell-cut-trace-factorization). Select $`m=2^q\ge2`$ sites in each cube. In every seed branch the cut comparison of one box with all earlier boxes has trace-distance error at most

```math
\epsilon=ad\nu(\ell+2r)^{d-1}(e^{vT}-1)e^{-r/a}.
```

Apply the local dimension-$m$ [fingerprint channel](continuous_time.md#4-orbit-ensembles-and-local-fingerprint-registers) to each box. The normalized orbit Gram is the resulting state on the unconditional system output. In a particular branch its single-box conditional entropy, given all earlier fingerprint registers, satisfies the existing [continuity estimate](continuous_time.md#5-conditional-entropy-continuity-has-only-a-log-m-cost) when $`\epsilon\le1/2`$. Its additive loss is

```math
A(\epsilon,m)
=3\epsilon\log_2m+h_2(\epsilon)
 +(1+\epsilon)h_2\!\left(\frac{\epsilon}{1+\epsilon}\right).
```

Here the term with coefficient three combines the conditional and marginal continuity losses. The estimate depends only on the fingerprint dimension of one box and is uniform over the seed. By strong subadditivity, including the classical seed among the conditioning registers gives a lower bound on each chain contribution. Averaging the branch inequalities and using $`I(R:\Gamma_b)\le h`$ then gives

```math
S(\Gamma)\ge
p(q-\log_2\kappa)-(p-1)[h+A(\epsilon,m)].
```

The first box contributes its unconditioned entropy. Pair fidelity enters only through the actual system orbit ensemble and its Holevo bound above. At maximal fidelity all its orbit states agree. Thus for general $`0\lt c\le1`$,

```math
2S(\rho)\ge
p\bigl(\max\{q w(c),\,c^2q-1\}-\log_2\kappa\bigr)
-(p-1)[h+A(\epsilon,m)] .
```

In particular, the continuity penalty can be bounded by an absolute constant for fixed microscopic parameters. Take $`z=\lceil1+vT\rceil`$, $`\ell=\ell_0 z`$ for a fixed integer $`\ell_0\ge2`$, and $`r=A_0az`$ for a fixed integer $`A_0\ge2`$. Then

```math
\epsilon\le
ad\nu(\ell_0+2A_0a)^{d-1}z^{d-1}e^{-(A_0-1)z}.
```

Choose $`A_0`$ large enough that this is at most $`1/2`$ for every $`z\ge1`$. With $`q=\lfloor\log_2(\ell^d)\rfloor`$, the exponential decay makes $`A(\epsilon,m)=O(1)`$ uniformly in $`T`$. Packing gives order $`K_T`$ boxes with $`q=\log_2 V_T+O(1)`$ before the diameter cap. The [unlimited-seed time bound](continuous_time.md#8-shared-classical-continuous-time-lower-bound) gives the complementary causal-volume and global floors. At and near diameter time the global floor covers the stated expression.

For the upper bound, the common coordinates can be preloaded as classical local controls. The independent coordinates use the [bounded-strength Hamiltonian block protocol](continuous_time.md#7-matching-bounded-hamiltonian-preparation), with its coherent seed broadcast, boundary meters, and final discard. The time remains of order the block side divided by the microscopic strength and the on-site apparatus remains logarithmic in the block side. Choosing the blocks from the available time and applying the exact rank formula gives the matched scale at maximal fidelity. The Bernoulli construction gives the corresponding imperfect-fidelity upper bracket in the same apparatus model.

## Attribution

The maximal-fidelity entropy identity and the mask spectrum build on the existing [orbit bounds](entropy_bounds.md#proposition-e6-maximal-fidelity-endpoint) and [construction](constructions.md#proposition-c1-exact-spectrum). The underlying classical sampling bounds and symmetric finite-depth fidelity-order diagnostic are established ingredients. The use of a Shannon-entropy budget for a common variable is related to [exact common information](https://arxiv.org/abs/1402.0062), where the target joint law is specified in advance. Here the common variable is charged while optimizing the retained quantum output over a fidelity and correlation class at fixed local depth or time. See the [related-work account](../references/related_work.md) for the comparison with mixed-state preparation bounds.
