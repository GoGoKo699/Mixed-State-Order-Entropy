# Matching local preparations for mixed-state order

[Model](model.md) · [Entropy tools](entropy_bounds.md) · [Circuit frontiers](circuit_bounds.md) · [Constructions](constructions.md) · [Scope and robustness](scope_and_robustness.md)

This page proves local circuit constructions with maximal pair fidelity order, their resource costs, and their exact output spectra. It gives matching upper bounds for the strict product and shared classical randomness models in [Circuit bounds](circuit_bounds.md). The finite numerical checks at the end audit the implementations separately from the general proofs.

## 1. Setting and common construction

There are $`N\ge 2`$ retained qubits on a finite lattice of fixed spatial dimension $`d`$. Write

```math
Q=\prod_{i=1}^N X_i,
\qquad
F_{ij}(\rho)=\|\sqrt\rho Z_iZ_j\sqrt\rho\|_1.
```

Fidelity is the **root** convention. The states constructed below obey

```math
Q\rho=\rho,
\qquad F_{ij}(\rho)=1\quad(i\ne j),
\qquad C_{ij}:=\mathrm{Tr}(\rho Z_iZ_j)=\delta_{ij}.
\tag{1}
```

Their entropy is unconditional: all preparation records and ancillary registers are discarded. There is no postselection. All logarithms and entropies are in bits.

Partition the lattice into $`K`$ connected blocks $`B_b`$, with sizes $`m_b\ge1`$, bounded aspect ratios, and diameter at most $`h`$ in a chosen bounded-degree block spanning tree. Each block has a fixed anchor $`o_b`$. The block adjacency graph is connected and has bounded degree; choose a spanning tree $`\mathsf T`$ of that graph. For every edge $`e=(b,b')\in\mathsf T`$, choose neighboring physical sites $`u_e\in B_b`$, $`v_e\in B_{b'}`$.

The preparation consists of three operations:

1. Prepare a GHZ+ state inside each block.
2. Apply random on-site $`X`$ masks, with the correlation pattern specified below.
3. Apply independent boundary channels
   ```math
   \mathcal D_e(\sigma)=\tfrac12\bigl(\sigma+Z_{u_e}Z_{v_e}\sigma Z_{u_e}Z_{v_e}\bigr)
   \tag{2}
   ```
   on the edges of $`\mathsf T`$.

The mask channel and the boundary channels commute as superoperators: conjugation by any $`X`$ mask commutes with conjugation by any $`Z_iZ_j`$, even when the underlying Pauli operators anticommute. Thus their order can be reversed without changing the retained output. The displayed order is convenient for the proof.

Each data operation can be chosen strongly $`Q`$-symmetric. The converse may allow a larger class of channels with only final-state symmetry; the upper already works in this stricter subclass.

## 2. Strongly symmetric GHZ growth

Start the data in the product state $`|+\rangle^{\otimes N}`$. On a parent site $`a`$ and fresh child $`b`$, use

```math
V_{ab}=\exp\!\left(\frac{i\pi}{4}Z_aY_b\right)
=\frac{I+iZ_aY_b}{\sqrt2}.
\tag{3}
```

It satisfies

```math
[V_{ab},X_aX_b]=0,
\qquad
V_{ab}|0,+\rangle=|00\rangle,
\qquad
V_{ab}|1,+\rangle=|11\rangle.
\tag{4}
```

The commutator vanishes because $`Z_aY_b`$ anticommutes with each of $`X_a`$ and $`X_b`$, and therefore commutes with their product. The two copying identities follow by applying $`\exp(\pm i\pi Y/4)`$ to $`|+\rangle`$. Consequently $`V_{ab}`$ extends an existing GHZ cat to the new child while preserving the global $`X`$ charge.

A breadth-first schedule on a block tree of height $`h_b`$ and maximum degree $`\Delta`$ uses $`m_b-1`$ two-site gates and at most $`O(\Delta h_b)`$ layers. Different parents' attachments commute when their supports are disjoint; a fixed edge-color schedule handles multiple children. All blocks run in parallel. A rectangular block of side $`\ell`$ has a tree of height $`O_d(\ell)`$ and degree at most $`2d`$, giving depth $`O_d(\ell)`$.

Equation (3) directly has a bounded, strongly symmetric two-site Hamiltonian generator, so no decomposition into individually nonsymmetric gates is required.

## 3. Exact cat-sector spectrum

### 3.1 Canonical block cats

Represent a binary pattern $`u_b\in\mathbb F_2^{m_b}`$ with $`u_{b,o_b}=0`$. For a phase bit $`\epsilon_b\in\mathbb F_2`$, define

```math
|u_b;\epsilon_b\rangle
=\frac{|u_b\rangle+(-1)^{\epsilon_b}|u_b+\mathbf1_b\rangle}{\sqrt2}.
\tag{5}
```

For $`m_b=1`$, the only canonical $`u_b`$ is zero and these are $`|+\rangle`$, $`|-\rangle`$. For every block, the states (5), indexed by its $`2^{m_b-1}`$ canonical patterns and two phase bits, form an orthonormal basis. They obey

```math
Q_b|u_b;\epsilon_b\rangle=(-1)^{\epsilon_b}|u_b;\epsilon_b\rangle,
\quad Q_b=\prod_{i\in B_b}X_i,
\tag{6}
```

and

```math
Z_i|u_b;\epsilon_b\rangle
=(-1)^{u_{b,i}}|u_b;\epsilon_b+1\rangle.
\tag{7}
```

All additions of binary labels are modulo two.

### 3.2 A general linear mask family

Let the raw mask be $`x=A y\in\mathbb F_2^N`$, where $`y\in\mathbb F_2^r`$ is uniform and $`A`$ is a fixed binary matrix. Write $`a_i\in\mathbb F_2^r`$ for its row at site $`i`$, so $`x_i=a_i\cdot y`$. The physical operation is

```math
X(x)=\prod_i X_i^{x_i}.
\tag{8}
```

Define the blockwise canonicalization map

```math
(Tx)_{b,i}=x_i+x_{o_b},\qquad (Tx)_{b,o_b}=0.
\tag{9}
```

The phase incurred when a whole block is complemented is irrelevant to its density matrix. Acting on the initial GHZ+ product, (8) therefore produces the cat product labeled by $`u=TAy`$. Let

```math
\mathcal U=\mathrm{im}(TA),\qquad q=\mathrm{rank}_{\mathbb F_2}(TA).
\tag{10}
```

The uniform seed gives the uniform law on $`\mathcal U`$, because all fibers of a linear map have the same size. Thus $`q`$, rather than the number of supplied seed bits, is the exact entropy contributed by distinguishable mask patterns. This distinction matters when some seed directions complement entire blocks and hence do not change the cat projectors.

### 3.3 Boundary phases and incidence rank

For a boundary edge, (7) shows that $`Z_{u_e}Z_{v_e}`$ flips the phase bits at its two endpoint blocks, up to an irrelevant overall sign. The independent edge coins in (2) therefore generate

```math
\epsilon=\partial s,
\qquad s\in\mathbb F_2^{K-1},
\tag{11}
```

where $`\partial`$ is the incidence matrix of the block tree over $`\mathbb F_2`$. Its image is

```math
\mathcal E_K=\left\{\epsilon\in\mathbb F_2^K:
\sum_b\epsilon_b=0\right\},
\qquad \dim\mathcal E_K=K-1.
\tag{12}
```

For completeness, every incidence column has even parity, so the image lies in $`\mathcal E_K`$. If a sum of tree-edge columns vanishes, a leaf forces the coefficient of its incident edge to vanish. Removing leaves inductively shows the columns are independent. There are $`K-1`$ of them, proving (12). Thus fair independent edge coins produce the uniform law on $`\mathcal E_K`$. A connected graph with extra edges gives the same output law but has redundant coins; a tree realizes the rank with exactly $`K-1`$ coins.

### Proposition C1. Exact spectrum

The final state is exactly

```math
\rho_{A,\mathsf T}
=2^{-(q+K-1)}
\sum_{u\in\mathcal U}\sum_{\epsilon\in\mathcal E_K}
\bigotimes_{b=1}^K
|u_b;\epsilon_b\rangle\langle u_b;\epsilon_b|.
\tag{13}
```

Every summand is orthogonal to every other. Hence

```math
\boxed{S(\rho_{A,\mathsf T})=q+K-1,\qquad
\mathrm{rank}\rho_{A,\mathsf T}=2^{q+K-1}.}
\tag{14}
```

Its nonzero eigenvalues are all equal. Since $`q\le N-K`$, the rank never exceeds the dimension $`2^{N-1}`$ of the global $`Q=+1`$ sector. The formula includes $`K=1`$, for which there is no boundary channel and $`\mathcal E_1=\{0\}`$.

### 3.4 Fidelity and ordinary correlations

Equation (6) and even parity of $`\epsilon`$ prove $`Q\rho=\rho`$. If $`i,j`$ lie in the same block, $`Z_iZ_j`$ changes only a phase of each cat vector. If they lie in different blocks, it translates $`\epsilon`$ by an even vector. The uniform sum in (13) is invariant in both cases. Therefore

```math
Z_iZ_j\rho Z_iZ_j=\rho,
\qquad F_{ij}(\rho)=1.
\tag{15}
```

For a single site, $`Z_i\rho Z_i`$ lies in the opposite global charge sector, so

```math
F(\rho,Z_i\rho Z_i)=0.
\tag{16}
```

Every cat has zero one-point $`Z_i`$. Correlations between different blocks therefore vanish even when the mask seeds or phase bits are correlated. Within one block,

```math
\mathrm{Tr}(\rho Z_iZ_j)
=\mathbb E_y(-1)^{(a_i+a_j)\cdot y}
=\begin{cases}1,&a_i=a_j,\\0,&a_i\ne a_j.\end{cases}
\tag{17}
```

Consequently **distinct row labels within each block are sufficient for $`C=I_N`$**. Labels in different blocks may be reused. Strong symmetry also forces every one-point expectation of an operator odd under $`Q`$ to vanish. Suppressing correlations between general local charged operators requires the additional construction in Section 7; it must not be inferred merely from $`C=I_N`$.

## 4. Strict product-input construction

The data and all ancillary registers start as a tensor product over sites. The apparatus supplies no shared seed between different sites. Random bits are generated locally and physically propagated along nearest-neighbor edges.

### Proposition C2. Strict product masks

For block $`b`$, let

```math
r_b=\lceil\log_2 m_b\rceil,
\tag{18}
```

with $`r_b=0`$ when $`m_b=1`$. Assign its sites the binary labels $`0,1,\ldots,m_b-1`$ in $`\mathbb F_2^{r_b}`$, with label zero at the anchor. Generate a uniform independent seed $`y_b\in\mathbb F_2^{r_b}`$. Use

```math
x_i=a_i\cdot y_b\quad(i\in B_b).
\tag{19}
```

Distinct labels give (17). The seed-to-canonical-pattern map has rank $`r_b`$: the labels include zero and all binary basis vectors $`1,2,4,\ldots,2^{r_b-1}`$, because $`2^{r_b-1}\lt m_b`$ when $`m_b\ge2`$. The seeds of different blocks are independent, so

```math
q=\sum_b r_b,
\qquad
\boxed{S_{\mathrm{strict}}=K-1+\sum_b\lceil\log_2m_b\rceil.}
\tag{20}
```

This is an exact equality for every block size, including singleton blocks. The construction uses $`\sum_b r_b`$ independent mask coins and $`K-1`$ independent boundary coins, all generated during the preparation from local product apparatus.

### 4.1 Bounded-workspace pipelined broadcast

The following explicit schedule prevents a hidden $`r_b h_b`$ depth cost or an unbounded on-site register.

Fix the rooted block tree and each node's depth $`d_i`$. Give every site two ancillary classical-bit registers, `current` and `next`, initially zero. The randomness source at the root generates bit $`y_{b,t}`$ in round $`t`$ for $`0\le t\lt r_b`$. A local preparation of $`I/2`$ produces this fair bit; equivalently, prepare $`|+\rangle`$ and locally dephase it in $`Z`$. No nonlocal state is supplied.

In round $`t=0,\ldots,h_b+r_b-1`$, the active current bit at site $`i`$ is $`y_{b,j}`$, where $`j=t-d_i`$ and $`0\le j\lt r_b`$. An inactive current register is zero. Each round consists of:

1. At an active root, prepare the next independent source bit.
2. At every active site, apply a controlled $`X_i`$ from `current` to the retained qubit if the hardwired coefficient $`a_{i,j}`$ is one.
3. Copy `current` into each child's zero `next` register. A fixed coloring of the bounded-degree tree schedules these edge CNOTs in a constant number of layers.
4. Reset the used current registers locally, then swap each arriving `next` bit into `current` for the following round.

The two buffers ensure that a bit received in a round cannot move another edge in the same round. They also prevent overwriting a bit that is still being processed. After the final round, all relevant bits have reached all sites and all buffers can be zeroed and discarded. Conditioned on the independently generated source bits, the retained operation is exactly (19); averaging gives the required mask channel.

If the tree has maximum degree $`\Delta`$, a greedy edge coloring uses at most $`2\Delta-1`$ colors. Counting source preparation, local controlled $`X`$, copies, reset, and swap gives the conservative bound

```math
D_{\mathrm{mask},b}\le (2\Delta+6)(h_b+r_b+1).
\tag{21}
```

Constants can be reduced; their optimization is irrelevant to the frontier. The active workspace is two bit registers per site, independent of $`r_b,m_b,N`$. The schedule has exactly $`(m_b-1)r_b`$ bit transmissions, at most $`m_b r_b`$ data-controlled $`X`$ gates, and $`O(m_b(r_b+1))`$ local reset/swap/preparation operations. Idle zero-register actions are omitted. Thus the latency is $`O(h_b+r_b)`$ and the gate count is $`O(m_b(r_b+1))`$, rather than their product with the tree height.

The classical control table $`a_{i,j}`$, the tree, and the round schedule are fixed by the geometry. They are not unknown input data or QRAM. Ancilla resets and discarding are permitted local CPTP operations and are explicitly counted as operations; the entropy theorem is not a thermodynamic claim that these resets are free of work or heat.

Every data-controlled $`X_i`$ commutes with the data charge $`Q`$. Copying, randomization, resetting, and swapping the uncharged ancillary registers act trivially on $`Q`$. Therefore the whole broadcast implementation is strongly symmetric on the retained system.

## 5. Shared-classical-randomness construction

This model permits an initially shared classical seed, but no preexisting nonlocal quantum state. A seed may be represented by one preloaded mask bit at each site, with a specified correlated joint law. Conditional on that shared classical variable, all initial quantum registers are local products. The preexisting classical correlations are a supplied resource; they are not generated by the charged local preparation depth.

### Proposition C3. Shared classical masks

Let $`m_* =\max_b m_b`$ and $`r=\lceil\log_2m_*\rceil`$. Give block $`b`$ the labels $`0,1,\ldots,m_b-1`$, now padded into the common space $`\mathbb F_2^r`$. Reuse this table in different blocks, and use the same uniform seed $`y`$ everywhere. Equation (17) still gives $`C=I_N`$, since interblock correlations already vanish.

The largest block contains all $`r`$ basis labels. The canonical mask map therefore has rank exactly $`r`$, giving

```math
\boxed{S_{\mathrm{shared}}=K-1+\lceil\log_2m_*\rceil.}
\tag{22}
```

This sharper exact form implies the advertised $`O(K+\log N)`$ upper. It is also at least $`\log_2N`$, since $`N\le K m_*`$ and $`\log_2K\le K-1`$. For balanced blocks it is $`\Theta(K+\log N)`$. No contradiction with the static logarithmic lower bound occurs when the shared seed is shorter than $`\log_2N`$: the $`K-1`$ boundary-phase bits supply the rest of the mixedness.

One can instead assign all $`N`$ sites distinct global binary labels with $`r=\lceil\log_2N\rceil`$. That familiar global Hadamard construction gives

```math
S=K-1+\mathrm{rank}\{a_i+a_{o_b}:i\in B_b,\ b\in[K]\}
\le K-1+\lceil\log_2N\rceil.
\tag{23}
```

Equality to the supplied seed length is not automatic. For example, with eight sites and two consecutive four-site blocks, global binary labels $`0,\ldots,7`$ have only two independent within-block differences. The final entropy is three bits, although the supplied global seed has three bits and there is an additional boundary coin.

### 5.2 Charged depth and workspace

Preload each site's one-bit value $`x_i=a_i\cdot y`$ in a local classical control cell. Apply all local controlled $`X_i`$ gates in parallel and discard the control cells. This takes one local gate layer, $`N`$ controlled gates, and one classical bit of active control storage per site. The joint preloaded mask law has entropy at most $`r`$; the $`N`$ stored mask bits are not independent.

If the mask bits are instead to be generated and distributed from one physical source after the clock starts, their propagation must be charged and the model is no longer this free-shared-randomness model. The strict construction in Section 4 charges precisely that propagation within each block.

## 6. Geometry, resource counts, and frontier matching

### Proposition C4. Depth and resource bounds

For a cubic $`d`$-dimensional box of side $`L`$, $`N=L^d`$, choose a partition into rectangular blocks with side lengths between fixed positive multiples of $`\ell`$, with $`1\le\ell\le L`$. Rounding can be implemented by choosing the number of pieces per coordinate first and splitting each coordinate as evenly as possible. Then

```math
K=\Theta_d(N/\ell^d),
\qquad m_b=\Theta_d(\ell^d),
\qquad h_b=O_d(\ell).
\tag{24}
```

For $`\ell`$ near $`L`$, take a single block. A bounded-degree tree of block adjacencies and a constant edge-color schedule implement all boundary channels (2) in $`O_d(1)`$ layers. The boundary channels have Kraus operators $`I/\sqrt2`$ and $`Z_{u_e}Z_{v_e}/\sqrt2`$, each commuting with the global $`X`$ charge. Their exact local CPTP realization may use a local meter that is discarded.

For an explicit finite bound, suppose every block has side lengths at most the integer $`b\ge1`$. Its tree can have height $`h_b\le d(b-1)`$ and degree at most $`2d`$, while its baseline mask has $`r_b\le\lceil d\log_2 b\rceil\le d(b-1)`$ bits. Use a greedy edge coloring with at most $`4d-1`$ colors. A level-by-level GHZ schedule costs at most $`(4d-1)h_b`$ layers. Equation (21) bounds the mask schedule by $`(4d+6)(h_b+r_b+1)`$, and the physical boundary-edge graph needs at most $`4d-1`$ further layers. All blocks run in parallel, so both baseline constructions satisfy the conservative common bound

```math
D_{\mathrm{prep}}
\le (12d^2+11d)(b-1)+8d+5
\le A_db,\qquad A_d=64(d+1)^2.
\tag{24a}
```

The shared-seed mask step is only one layer; the displayed common bound deliberately also covers the strict stream. The constants are implementation bounds, not claims of minimum depth.

Combining GHZ growth, masks, and boundary channels gives:

| Resource | Strict product apparatus | Free shared classical seed |
|---|---:|---:|
| Retained data | $`N`$ qubits | $`N`$ qubits |
| Active local mask workspace | two bit buffers/site | one preloaded bit/site |
| GHZ gates | $`N-K`$ | $`N-K`$ |
| Charged mask transmission count | $`\sum_b(m_b-1)r_b`$ | zero after preload |
| Mask/local-control gate count | $`O(\sum_bm_b(r_b+1))`$ | $`O(N)`$ after preload |
| Boundary channels / independent coins | $`K-1`$ | $`K-1`$ |
| Total local circuit depth | $`O_d(\ell)`$ | $`O_d(\ell)`$ |
| Exact entropy, baseline masks | $`K-1+\sum_b\lceil\log_2m_b\rceil`$ | $`K-1+\lceil\log_2m_*\rceil`$ |

For fixed $`d`$, $`\log m_b=O_d(\log(\ell+1))=O_d(\ell)`$, so pipelining preserves the stated depth. The strict gate count is $`O_d(N\log(\ell+1))`$. The shared model's preloaded-mask generation and its classical correlations are explicitly outside the charged depth, not asserted to cost zero in a fully local apparatus model.

Thus the constructions attain

```math
S_{\mathrm{strict}}
=O_d\!\left(\frac{N}{\ell^d}\log(\ell+1)\right),
\qquad
S_{\mathrm{shared}}
=O_d\!\left(\frac{N}{\ell^d}+\log N\right),
\tag{25}
```

with exact maximal fidelity order and $`C=I`$. Choosing $`\ell`$ a sufficiently small constant multiple of a prescribed depth budget $`D`$ gives the matching upper laws for all sufficiently large constant $`D`$, up to the fixed-dimensional implementation constants. At a constant depth, singleton or bounded-size blocks give entropy $`\Theta(N)`$. At and beyond diameter depth, a single block gives entropy $`\lceil\log_2N\rceil`$, so the scale saturates at $`\Theta(\log N)`$.

The factor $`N/D^d`$ is capped at diameter depth; it does not continue below one. A notation such as $`D+1`$ does not assert zero-depth feasibility in the strict product model. For $`N\ge3`$, its ordered class is empty at depth zero or one under the stated two-site-gate convention; the shared-classical class has a depth-zero baseline. These exceptions and a depth-two strict baseline are given in [Circuit bounds](circuit_bounds.md#construction-inputs-and-finite-depth-feasibility). Equations (20)–(24a), with the explicit depth schedule, give the finite-size upper statement.

The lower bounds are proved in [Circuit bounds](circuit_bounds.md). Since these states have $`F_{ij}=1`$, they serve as upper examples for every fixed target $`0\lt c\le1`$. Their entropy scaling does not establish an optimal coefficient as $`c\to0`$.

## 7. Masks that suppress general local charged correlations

### 7.1 Why ordinary pair correlations alone are insufficient

A pairwise-independent Hadamard mask kills each $`Z_iZ_j`$ expectation but can retain higher products. On a block with labels $`0,1,2,3`$, for example,

```math
0+1+2+3=0\quad\text{over }\mathbb F_2^2.
```

The four-$`Z`$ product is unaffected by the mask. It can be written as the product of a charged one-site $`Z`$ operator and a charged three-site $`Z`$ operator. Thus the narrow $`C=I`$ construction must not by itself be advertised as eliminating ordinary order in every fixed-support charged observable.

The following repair leaves the asymptotic entropy and depth costs unchanged. It is a spatially constrained small-sample-space construction, not a new claim about classical Hadamard codes.

For a Pauli string $`P`$, let

```math
D(P)=\{i:P_i\in\{Y,Z\}\}.
```

Conjugating by a mask gives

```math
X(Ay)P X(Ay)=(-1)^{(\sum_{i\in D(P)}a_i)\cdot y}P.
\tag{26}
```

The string is odd under $`Q`$ exactly when $`|D(P)|`$ is odd. For two strings on disjoint physical supports, their product has the union of their $`Y/Z`$ supports, without cancellation. This disjoint-support condition is essential.

### 7.2 Shared-seed repair on growing balls

Fix a family of at most $`N`$ lattice balls, one per possible center, each containing at most $`b`$ sites. Include smaller local supports by containment. Independently sample each label $`a_i`$ uniformly in $`\mathbb F_2^r`$. For every pair of balls and every pair of **disjoint odd nonempty** $`Y/Z`$ supports $`A,B`$ contained in them, require

```math
\sum_{i\in A\cup B}a_i\ne0.
\tag{27}
```

The containing balls may overlap; only the actual supports must be disjoint. There are at most $`N^2 2^{2b}`$ constraints. Each involves a nonempty set of independently sampled labels, so its zero-XOR probability is exactly $`2^{-r}`$. The union bound shows a valid fixed label table exists when, for example,

```math
r\ge \left\lceil 1+2\log_2N+2b\right\rceil.
\tag{28}
```

At that choice the failure probability is at most $`1/2`$. Once a valid table has been found, only the uniform seed $`y`$ is randomized during use; the table is fixed control information.

The mask average kills every product of two disjoint charged Pauli strings in the chosen balls, by (26)–(27). By Pauli expansion it kills the correlation of any two disjoint local operators $`O_A,O_B`$ satisfying $`QO_AQ=-O_A`$ and $`QO_BQ=-O_B`$. The boundary twirls commute with the mask channel, so the statement holds for the final state (13). Strong symmetry already makes both one-point expectations zero.

Taking $`b=\lfloor\log_2N\rfloor`$ keeps $`r=O(\log N)`$, so

```math
S\le K-1+r=O(K+\log N).
\tag{29}
```

On a fixed-dimensional lattice, balls of radius proportional to $`(\log N)^{1/d}`$ satisfy this size condition. Their radius diverges, so every fixed-radius local charged operator is eventually covered. The entropy scaling of the shared construction is therefore retained while removing hidden ordinary charged order at every fixed local scale.

The label table uses $`O(N\log N)`$ classical bits. For $`b=O(\log N)`$, the finite constraint family in the union bound has polynomial size; enumerating and checking it gives a finite classical preprocessing procedure with expected at most two independent table draws at the stated slack. This preprocessing is distinct from quantum circuit depth and from unknown-input loading.

### 7.3 Strict-product repair inside growing blocks

Use independent seeds and independent fixed label tables in different blocks. A slightly stronger within-block constraint makes the proof work even when local operators straddle block boundaries.

For a block $`B_b`$, consider the intersections with all lattice balls of radius $`R`$ that meet it. Let their number be $`M_b`$, and suppose every ball has at most $`b_*`$ sites. For every nonempty set $`D`$ contained in the union of two such intersections, require

```math
\sum_{i\in D}a_i^{(b)}\ne0.
\tag{30}
```

No parity condition is imposed in (30). There are at most $`M_b^2 2^{2b_*}`$ constraints. Independent random labels in $`\mathbb F_2^{r_b}`$ satisfy them with positive probability if

```math
r_b\ge\left\lceil1+2\log_2M_b+2b_*\right\rceil.
\tag{31}
```

For bounded-aspect-ratio blocks and $`R`$ no larger than a fixed multiple of their side, $`M_b=O_d(m_b)`$. Choose $`b_*=O(\log m_b)`$, uniformly using the minimum block size for a balanced partition. Then $`r_b=O_d(\log m_b)`$. The stream protocol of Section 4 distributes these seeds in $`O_d(\ell)`$ depth with constant active workspace, and (14) gives

```math
S\le K-1+\sum_b r_b
=O_d(K\log(\ell+1)).
\tag{32}
```

To prove the charged-correlation claim, take disjoint charged Pauli strings $`P_A,P_B`$ in two radius-$`R`$ balls. Their product has a nonempty $`Y/Z`$ support. In some block, its intersection $`D_b`$ is nonempty and lies in the union of the two ball intersections. The independent seed in that block kills the product by (26) and (30). This argument allows both operators to cross block boundaries and does not assume that their containing balls are disjoint. Pauli expansion again gives arbitrary charged local operators.

For small blocks one may instead use a fully independent mask bit on every site of the block. This supplies the required constraints directly and costs at most a fixed number of bits/gates per site when those blocks have bounded size. For growing balanced blocks, one can take $`R`$ proportional to $`(\log m_b)^{1/d}`$, which diverges while retaining the stated asymptotic cost. At bounded block size, any two supports meeting disjoint sets of blocks already have zero charged correlation: an odd total charge in one support leaves at least one block with an odd block charge, whose expectation vanishes in each block-cat projector.

The repair may increase the finite entropy coefficient, and the exact rank $`q`$ of its label map need not equal the number of seed bits. Its role is an upper construction with the same asymptotic scale and a stronger local ordinary-order guarantee. It does not change the converse assumptions silently.

## 8. Attribution and scope

The low-entropy sign masks are classical constructions. Pairwise-independent balanced bits from Hadamard matrices, their logarithmic seed size, and the corresponding entropy lower bounds are established antecedents. A convenient primary reference is:

- D. Gavinsky and P. Pudlák, *On the joint entropy of $`d`$-wise-independent variables*, Commentationes Mathematicae Universitatis Carolinae **57** (2016), 333–343, especially Theorem 3.2, Corollary 3.3, and Section 4 / Theorem 4.1. [Primary PDF](https://dml.cz/bitstream/handle/10338.dmlcz/145838/CommentatMathUnivCarolRetro_57-2016-3_7.pdf), [arXiv:1503.08154](https://arxiv.org/abs/1503.08154), DOI [10.14712/1213-7243.2015.169](https://doi.org/10.14712/1213-7243.2015.169).
- L. Babai, *Entropy Versus Pairwise Independence* (2013), for the earlier entropy and near-independence perspective. [Author manuscript](https://people.cs.uchicago.edu/~laci/papers/13augEntropy.pdf). The inherited static quantum-information ingredients are identified in [Entropy bounds](entropy_bounds.md).

The boundary incidence rank, Clifford/Pauli GHZ preparation, pipelined tree broadcast, and probabilistic zero-XOR avoidance are also standard tools. The contribution here is the model-matched preparation and its exact retained-state entropy, including how initial classical coordination changes the optimal scaling. A new classical code, a new general entropy inequality, or a free thermodynamic reset is not claimed.

These are local-channel circuit upper bounds. Exact finite-time dephasing is permitted as a CPTP gate or as coupling to a local meter followed by discarding it. A bounded finite-rate system-only Lindbladian does not perform exact complete dephasing at a finite time. Therefore these constructions must not be transferred unchanged to that narrower continuous-time model.

## 9. Finite-instance verification record

The accompanying script [`constructions_check.py`](../verification/constructions_check.py) builds the **final masked states** by the local GHZ-growth circuit, explicit streamed/local mask trajectories, and boundary phase coins. It independently builds the cat-sector mixture (13), compares the two density matrices, and checks spectra, entropy, charge, ordinary Gram matrices, root fidelities, and local charged Pauli correlations. It also includes negative controls that remove a boundary twirl or expose the higher-product correlations of an un-repaired Hadamard mask.

The [verification guide](../verification/README.md) gives reproduction commands and numerical conventions. The output file [`constructions_check.json`](../verification/constructions_check.json) records actual numerical residuals, conventions, checked cases, and environment metadata. It is a finite arithmetic and implementation audit. The general rank, entropy, locality, and growing-support statements are proved above; no extrapolation from small systems is used.

All 11 recorded cases passed their stated assertions. The three state representations agree within Frobenius error $`6.3\times10^{-16}`$. For two unequal blocks on seven sites, the strict and shared constructions have entropies five and three bits, respectively. The repaired eight-site cases suppress every tested disjoint charged Pauli pair on index-chain intervals of at most three sites. An unrepaired six-site example retains a charged one-site/three-site correlation of magnitude one, while the two controls separately expose the effects of removing masks and boundary twirls. The finite support family and numerical null-space cutoff are specified in the verification guide.
