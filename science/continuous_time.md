# Continuous-time preparation bounds

Both entropy frontiers extend to evolution under finite-range, bounded local generators. The product-input bound retains its logarithmic enhancement because the proof tracks one small auxiliary register per spatial box. An initially shared classical seed permits the smaller causal-volume bound.

The [model](model.md) defines the physical target and resource classes. The [entropy bounds](entropy_bounds.md) and [circuit bounds](circuit_bounds.md) give the common information-theoretic arguments, while the [constructions](constructions.md) give the exact output spectra. This page proves the continuous-time propagation step and states its apparatus assumptions. Source comparisons are collected in [related work](../references/related_work.md).

## 1. Result and scope

Let $`N=L^d`$ retained qubits occupy the open cubic lattice $`\Lambda_L=\{1,\ldots,L\}^d`$. Set

```math
C_{ij}=\mathrm{Tr}(\rho Z_iZ_j),\qquad
f_{ij}=F(\rho,Z_iZ_j\rho Z_iZ_j),
```

where throughout this note

```math
F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1
```

is **root fidelity**, and every entropy and logarithm is in bits. In particular,

```math
f_{ij}=\|\sqrt\rho Z_iZ_j\sqrt\rho\|_1.
```

Fix $`c\in(0,1]`$, $`\kappa\ge1`$, and define

```math
h(c)=h_2\!\left(\frac{1+c}{2}\right),\qquad
w(c)=1-h(c)\gt 0.
\qquad\text{(1)}
```

Assume the actual output obeys

```math
C\preceq\kappa I_N,\qquad f_{ij}\ge c\quad(i\ne j).
\qquad\text{(2)}
```

The Gram condition is stronger than merely saying that individual ordinary correlations vanish at large separation. It is explicit and essential. It follows, for example, from the uniform summability condition $`\sup_i\sum_j|C_{ij}|\le\kappa`$. It holds with $`\kappa=1`$ when all distinct ordinary $`ZZ`$ correlations are zero. The counterexample in Section 9 shows why qualitative clustering cannot replace it.

For evolution from resources that are initially product across spatial sites, under the finite-range bounded-generator assumptions of Section 2, the lower bound is

```math
S(\rho(T))\ge
A_{c,\kappa,d,a,\nu}\,
\frac{N}{\eta^d}\log_2(\eta+1)-B_{c,\kappa},
\qquad
\eta=\min\{L,1+vT\},
\qquad\text{(3)}
```

where $`v=e\mathcal ZJ`$, and all constants are independent of $`N,T`$, apparatus dimension, and the dimension of the discarded environment. Explicit nonoptimal choices are given below. In microscopic units with the interaction bounds fixed, this is the strict-product frontier

```math
S_{\min}(N,T;c,\kappa)
=\Theta_{c,\kappa}\!\left[
\frac{N}{\min\{L,T+1\}^{d}}
\log_2\!\bigl(\min\{L,T+1\}+1\bigr)
\right],
\qquad\text{(4)}
```

for times above a fixed local-gate time. The upper bound in (4) is attained by bounded local Hamiltonians with initially product local apparatus and a final local discard. A fully explicit safe implementation uses $`O(\log(\ell+1))`$ auxiliary qubits per lattice site when its block size is $`\ell`$; the generator strength and spatial range remain constant. Equation (4) is not asserted here for a model that simultaneously demands fixed on-site dimension, no fresh local apparatus, and system-only Markovian dynamics.

The lower bound does not need a symmetry assumption once (2) holds. The matching preparation stays in the exact strong sector $`Q\rho=\rho`$, $`Q=\prod_iX_i`$, and its elementary system interactions commute with $`Q`$. Thus it applies to the intended finite-system mixed-state order setting without using strong symmetry as an unproved step in the converse.

## 2. Precise dynamical assumptions

Use the $`\ell_\infty`$ lattice metric. At each spatial site there is a retained qubit and arbitrary finite-dimensional local apparatus. The local dimension may depend on $`N`$. The combined initial state is

```math
\varrho(0)=\bigotimes_{x\in\Lambda_L}\varrho_x.
\qquad\text{(5)}
```

Local mixedness is allowed. Initially shared random seeds, entangled resources, spatially correlated baths, postselection, and instantaneous remote outcome-dependent controls are not included. A deterministic common control schedule and site-dependent deterministic instructions are allowed.

The combined system and apparatus evolves under

```math
\frac{d\varrho}{dt}=\mathcal L(t)(\varrho),\qquad
\mathcal L(t)=\sum_{X\in\mathcal E}\mathcal L_X(t).
\qquad\text{(6)}
```

The spatial support family $`\mathcal E`$ is fixed; time dependence may switch individual terms on and off. Each summand is itself a valid local Lindblad generator, including a Hamiltonian commutator as a special case. This condition ensures that deleting terms leaves a valid completely positive, trace-preserving evolution. Merely decomposing a globally valid generator into arbitrary signed local superoperators would not suffice.

Fix constants $`a\in\mathbb N`$, $`a\ge1`$, $`\nu\in\mathbb N`$, and $`J\gt 0`$, independent of system size, with

```math
\mathrm{diam}_{\infty}(X)\le a,\quad
|\{X\in\mathcal E:x\in X\}|\le\nu,\quad
\sup_{t,X}\|\mathcal L_X^*(t)\|_{\infty\to\infty}\le J.
\qquad\text{(7)}
```

The norm in (7) is the induced operator norm on the full algebra after extending the local map by the identity. One may instead impose the stronger local completely bounded norm condition. A familiar dimension-independent sufficient condition for a term with Hamiltonian $`H_X`$ and jump operators $`L_{X,\alpha}`$ is

```math
2\|H_X(t)\|+2\sum_\alpha\|L_{X,\alpha}(t)\|^2\le J.
\qquad\text{(8)}
```

Bounded piecewise continuous time dependence is sufficient. Define the overlap coordination

```math
\mathcal Z=\max_{X\in\mathcal E}
|\{Y\in\mathcal E:Y\cap X\ne\varnothing\}|,
\qquad v=e\mathcal ZJ.
\qquad\text{(9)}
```

It is bounded in terms of the spatial assumptions, for instance by $`\nu(a+1)^d`$. Group terms with the same spatial support if convenient, while preserving (7). A bound on each term with an unbounded number of overlapping terms would not satisfy this model.

At time $`T`$, discard local apparatus and retain the qubits to obtain $`\rho(T)`$. Local discard contracts all trace distances used below. Intermediate local operations can be represented on the enlarged local apparatus, provided their implementation respects (6)–(8). No assumption that the reduced retained-system dynamics is Markovian is needed.

### Lieb–Robinson input and its normalization

Barthel and Kliesch [BK12, Theorem 1, Eq. (12)] give, for an observable $`O_Y`$ on any region $`Y`$, and a local generator $`K_X`$,

```math
\|K_X\tau(s,T)(O_Y)\|
\le V_{X,Y}\|K_X\|\,\|O_Y\|
e^{v(T-s)-\mathrm{dist}(X,Y)/a}.
\qquad\text{(10)}
```

Here $`\tau`$ is the Heisenberg propagator. Their prefactor is controlled by the smaller interaction neighborhood of $`X`$ and $`Y`$. In particular, for one support $`X\in\mathcal E`$, the safe weakened bound $`V_{X,Y}\le\mathcal Z`$ is sufficient for this note. It is independent of $`|Y|`$, even when $`Y`$ is disconnected and contains a macroscopic fraction of the lattice.

For completeness, the safe estimate follows from their written $`V_{X,Y}\le\mathrm{Vol}(\bar X)/\mathcal Z`$: the interaction neighborhood $`\bar X`$ is a union of at most $`\mathcal Z`$ supports intersecting $`X`$. Every nonempty interaction support contained in that union intersects at least one of those supports, so $`\mathrm{Vol}(\bar X)\le\mathcal Z^2`$. The paper also uses a sharper unit prefactor for individual generator terms; no such improvement is needed here.

## 3. Shell-cut trace factorization

**Lemma 1.** Let $`B`$ be a cube of $`\ell`$ sites on a side, and let $`F`$ be any region satisfying

```math
\mathrm{dist}_{\infty}(B,F)\ge2r+2a,
\qquad r\ge2a,
\qquad\text{(11)}
```

where $`r`$ is an integer. Suppose the $`r`$-site expansion $`U`$ of $`B`$ lies inside the lattice. There are states $`\sigma_B,\sigma_F`$ such that

```math
\frac12\|\rho_{BF}(T)-\sigma_B\otimes\sigma_F\|_1
\le\epsilon_{\ell,r,T},
\qquad\text{(12)}
```

with the explicit bound

```math
\epsilon_{\ell,r,T}
=ad\nu(\ell+2r)^{d-1}(e^{vT}-1)e^{-r/a}.
\qquad\text{(13)}
```

The product state in (12) need not be the product of the actual marginals. The bound does not depend on $`|F|`$.

**Proof.** Delete every interaction term that intersects both $`U`$ and $`U^c`$. The cut generator is a sum of a generator on $`U`$ and one on $`U^c`$. Equation (5) therefore makes the cut evolution a product across this partition at every time. Its final reduced state on $`B\cup F`$, after discarding apparatus, is $`\sigma_B\otimes\sigma_F`$.

Every removed support contains a site in the inner shell of thickness $`a`$ along the boundary of $`U`$. Hence its number is bounded by

```math
\begin{split}
n_{\rm cut}
&\le\nu\bigl[(\ell+2r)^d-(\ell+2r-2a)^d\bigr]\\
&\le2ad\nu(\ell+2r)^{d-1}.
\end{split}
\qquad\text{(14)}
```

Every removed support has distance at least $`r-a`$ from $`B`$. It lies inside the $`(r+a)`$-expansion of $`B`$, so (11) also puts it at distance at least $`r+a`$ from $`F`$. Thus its distance from $`Y=B\cup F`$ is at least $`r-a`$.

For an arbitrary norm-one observable $`O_Y`$, Duhamel's identity gives

```math
(\tau(0,T)-\tau_{\rm cut}(0,T))O_Y
=\int_0^T\tau_{\rm cut}(0,s)
\sum_{X\,\text{cut}}\mathcal L_X^*(s)
\tau(s,T)O_Y\,ds.
\qquad\text{(15)}
```

The cut Heisenberg propagator is a contraction. Applying (10) with the safe prefactor $`\mathcal Z`$ yields

```math
\begin{split}
\|(\tau-\tau_{\rm cut})O_Y\|
&\le n_{\rm cut}\mathcal ZJ
\frac{e^{vT}-1}{v}
e^{-(r-a)/a}\\
&=n_{\rm cut}(e^{vT}-1)e^{-r/a}.
\end{split}
\qquad\text{(16)}
```

The equality uses $`v=e\mathcal ZJ`$. Duality against all such observables gives a full trace-norm bound, rather than only a product-observable covariance estimate. Dividing by two and using (14) proves (12)–(13). Partial tracing local apparatus can only improve it. The packing below keeps all expanded boxes away from the lattice boundary; no boundary correction is required. $`\square`$

**Why this step matters.** One box must be approximately independent of the entire union of earlier boxes. Summing two-box covariance estimates, or approximating the whole many-body state by a global product, would introduce an unnecessary system-size error. The small-support side of (10), together with a cut whose area depends only on the chosen box, avoids that issue.

## 4. Orbit ensembles and local fingerprint registers

Choose $`K`$ disjoint boxes. Select $`m=2^q`$, $`q\ge1`$, distinct sites in each box, denoting their operators by $`Z_{b,i}`$, $`1\le i\le m`$. Let $`|\Psi\rangle_{SE}`$ be any purification of the retained output $`\rho`$, and for $`\mathbf a\in[m]^K`$ define

```math
U_{\mathbf a}=\prod_{b=1}^K Z_{b,a_b},\qquad
|\Psi_{\mathbf a}\rangle=U_{\mathbf a}|\Psi\rangle,
\qquad
\rho_{\mathbf a}=U_{\mathbf a}\rho U_{\mathbf a}.
\qquad\text{(17)}
```

The uniformly mixed purified orbit is

```math
\Omega_{SE}=m^{-K}\sum_{\mathbf a}
|\Psi_{\mathbf a}\rangle\langle\Psi_{\mathbf a}|.
\qquad\text{(18)}
```

It has the same nonzero spectrum as its normalized Gram matrix

```math
\Gamma_{\mathbf a,\mathbf a'}
=m^{-K}\mathrm{Tr}\rho\,
U_{\mathbf a'}U_{\mathbf a},
\qquad S(\Omega_{SE})=S(\Gamma).
\qquad\text{(19)}
```

There is a useful local-channel representation of $`\Gamma`$. For a simultaneous $`Z`$-measurement outcome $`z_b\in\{\pm1\}^m`$ in box $`b`$, set

```math
|\phi(z_b)\rangle=\frac1{\sqrt m}\sum_{i=1}^m z_{b,i}|i\rangle.
\qquad\text{(20)}
```

Let $`\Phi_b`$ measure the selected $`Z`$'s and prepare the $`m`$-dimensional state $`|\phi(z_b)\rangle`$. Then

```math
\Gamma=(\Phi_1\otimes\cdots\otimes\Phi_K)(\rho_{B_1\cdots B_K}).
\qquad\text{(21)}
```

Indeed, the matrix elements of the right-hand side are the simultaneous moments in (19). This channel representation is a mathematical device for applying trace-distance contraction. No physical implementation of the fingerprint channel is charged to, or required of, the preparation protocol.

The marginal register of box $`b`$ is

```math
\Gamma_b=C_b/m,
\qquad\text{(22)}
```

where $`C_b`$ is the corresponding principal ordinary Gram matrix. Under (2), $`\lambda_{\max}(\Gamma_b)\le\kappa/m`$, so

```math
S(\Gamma_b)\ge q-\log_2\kappa.
\qquad\text{(23)}
```

### The system Holevo bound

The binary Holevo information of two equiprobable states satisfies the inherited inequality

```math
\chi\{\tfrac12,\sigma_0;\tfrac12,\sigma_1\}
\le h_2\!\left(\frac{1+F(\sigma_0,\sigma_1)}2\right).
\qquad\text{(24)}
```

This is Roga–Fannes–Życzkowski [RFZ10, Eq. (26)], expressed with root fidelity and base-two entropy. It also follows by choosing Uhlmann purifications with overlap equal to root fidelity and applying Holevo data processing to their binary pure-state ensemble. The inequality is a prior result, not a new contribution here.

Label $`\mathbf a`$ by $`Kq`$ independent uniform bits and apply the mutual-information chain rule to the system orbit ensemble. At a binary split, fix all earlier bits and pair the two branches by keeping every remaining bit identical. Paired orbit unitaries differ by $`Z_{b,i}Z_{b,j}`$ for two sites in one box. As all orbit operators commute, the paired system states have fidelity $`f_{ij}\ge c`$. Joint concavity of root fidelity then gives fidelity at least $`c`$ between the two conditional mixed states at that split. Equation (24) bounds each conditional bit contribution by $`h(c)`$. Therefore

```math
\chi_S(\{m^{-K},\rho_{\mathbf a}\})\le Kq\,h(c).
\qquad\text{(25)}
```

Only the relevant pairs inside the boxes are needed in this argument; the all-pairs condition (2) is a convenient sufficient hypothesis.

Every orbit state has entropy $`S(\rho)`$, and its environment marginal equals the original purification marginal. Thus

```math
S(\Omega_S)=S(\rho)+\chi_S,
\qquad S(\Omega_E)=S(\rho).
```

Subadditivity and (19) give the general comparison

```math
2S(\rho)\ge S(\Gamma)-\chi_S.
\qquad\text{(26)}
```

Equations (19)–(26) hold without a preparation or independence assumption. Independence, or approximate independence, is needed only to lower-bound the total fingerprint entropy.

## 5. Conditional entropy continuity has only a $`\log m`$ cost

Arrange the boxes in any order and let $`F_b`$ be the union of boxes preceding box $`b`$. Suppose the geometric conditions of Lemma 1 hold between $`B_b`$ and $`F_b`$, with common $`\ell,r`$, and $`\epsilon_{\ell,r,T}\le\epsilon\le1/2`$. Contractivity in (21) yields

```math
\frac12\|\Gamma_{b,\lt b}-\omega_b\otimes\omega_{\lt b}\|_1\le\epsilon
\qquad\text{(27)}
```

for some product state, potentially different at each cut.

Winter [W16, Lemma 2] gives, when the first system has dimension $`m`$,

```math
|S(A|B)_\alpha-S(A|B)_\beta|
\le2\epsilon\log_2m+
(1+\epsilon)h_2\!\left(\frac{\epsilon}{1+\epsilon}\right).
\qquad\text{(28)}
```

The bound does not depend on the dimension of $`B`$. The ordinary marginal entropy continuity bound, recalled in [W16, Lemma 1], gives

```math
|S(\Gamma_b)-S(\omega_b)|\le\epsilon\log_2m+h_2(\epsilon).
\qquad\text{(29)}
```

Since the reference state in (27) is a product, (28)–(29) imply

```math
S(\Gamma_b|\Gamma_{\lt b})\ge S(\Gamma_b)-a(\epsilon,m),
\qquad\text{(30)}
```

where

```math
a(\epsilon,m)=3\epsilon\log_2m+h_2(\epsilon)
+(1+\epsilon)h_2\!\left(\frac{\epsilon}{1+\epsilon}\right).
\qquad\text{(31)}
```

The first box needs no continuity estimate. By the chain rule and (23),

```math
S(\Gamma)\ge K(q-\log_2\kappa)-(K-1)a(\epsilon,m).
\qquad\text{(32)}
```

This is the step that preserves the enhancement. The fingerprint register has dimension $`m`$, although its source box contains $`m`$ physical qubits. The continuity penalty is proportional to $`\log m`$, rather than to $`m`$, and is paid separately in a conditional entropy chain. No approximation in a Hilbert space of dimension $`2^N`$ is invoked.

## 6. Finite-box theorem, constants, packing, and the diameter cap

**Theorem 2 (finite-box continuous-time bound).** Under (5)–(9), let $`K`$ cubes of side $`\ell`$ have mutually separated supports satisfying (11), with each expanded cube inside the lattice. Select $`m=2^q\ge2`$ sites in each cube. Suppose the selected principal Gram matrices satisfy $`C_b\preceq\kappa I_m`$, and the within-box pairs used in the binary labeling have root fidelity at least $`c`$. If (13) is at most $`\epsilon\le1/2`$, then

```math
\boxed{\quad
2S(\rho(T))\ge Kq\,w(c)-K\log_2\kappa
-(K-1)a(\epsilon,m).
\quad}
\qquad\text{(33)}
```

**Proof.** Combine (25), (26), and (32). $`\square`$

No exact factorization of the output, no approximation of its fidelity, and no symmetry-sector projection is used. All hypotheses in (33) refer to the actual retained state.

### One explicit parameter choice

Write $`w=w(c)`$. Choose $`\epsilon_c\in(0,1/2)`$ small enough that

```math
3\epsilon_c+h_2(\epsilon_c)
+(1+\epsilon_c)h_2\!\left(\frac{\epsilon_c}{1+\epsilon_c}\right)
\le w/4.
\qquad\text{(34)}
```

Choose an integer $`q_0\ge1`$ satisfying $`\log_2\kappa\le wq_0/4`$, and an integer $`\ell_0\ge2`$ with $`\lfloor\log_2\ell_0^d\rfloor\ge q_0`$. For example,

```math
q_0=\max\{1,\lceil4\log_2\kappa/w\rceil\},\qquad
\ell_0=\max\{2,\lceil2^{q_0/d}\rceil\}.
\qquad\text{(35)}
```

Choose an integer $`A\ge\max\{2,d+1\}`$ so large that

```math
ad\nu(\ell_0+2Aa)^{d-1}e^{-A}\le\epsilon_c.
\qquad\text{(36)}
```

Such an $`A`$ exists, since the left side is polynomial times exponential in $`A`$. Put

```math
u=vT,\quad z=\lceil1+u\rceil,\quad
\ell=\ell_0z,\quad r=Aaz,\quad
q=\lfloor\log_2\ell^d\rfloor,\quad m=2^q.
\qquad\text{(37)}
```

Then $`u\le z-1`$, and (13) is bounded by

```math
ad\nu(\ell_0+2Aa)^{d-1}
z^{d-1}e^{u-Az}
\le ad\nu(\ell_0+2Aa)^{d-1}e^{-A}
\le\epsilon_c.
\qquad\text{(38)}
```

For the second inequality, $`z^{d-1}e^{-(A-1)z}`$ is decreasing for $`z\ge1`$, and the maximum occurs at $`z=1`$. This also absorbs the boundary-area polynomial without a $`\log N`$ buffer. Equations (34)–(35) ensure

```math
a(\epsilon_c,m)\le wq/4,
\qquad \log_2\kappa\le wq/4.
```

Thus (33) gives the convenient conservative bound

```math
S(\rho(T))\ge\frac w4 Kq.
\qquad\text{(39)}
```

### Spatial packing

Take cubic cells of side

```math
p=\ell+2r+2a,
\qquad\text{(40)}
```

and place a selected box centrally in each complete cell, leaving a margin $`r+a`$. Adjacent selected boxes then have distance at least $`2r+2a+1`$, and each expanded cube is inside its cell. We can use

```math
K=\lfloor L/p\rfloor^d.
\qquad\text{(41)}
```

Let $`P=\ell_0+2Aa+2a`$. With $`x=1+vT`$, we have $`z\le2x`$ and $`p\le Pz\le2Px`$. If $`L\ge2p`$, then

```math
K\ge\frac{N}{(4Px)^d}.
\qquad\text{(42)}
```

Also $`q\ge1+\lfloor\log_2z\rfloor\ge\log_2(z+1)\ge\log_2(x+1)`$, because $`z`$ is an integer and $`\ell_0\ge2`$. Consequently

```math
S(\rho(T))\ge
\frac{w}{4(4P)^d}\frac{N}{(1+vT)^d}\log_2(2+vT)
\quad(L\ge2p).
\qquad\text{(43)}
```

### Large times and small numbers of boxes

If the packing is too large for the lattice, a one-box orbit construction on $`M=2^{\lfloor\log_2N\rfloor}`$ selected sites needs no locality estimate. Equations (23)–(26) directly give the inherited static floor

```math
2S(\rho)\ge w\lfloor\log_2N\rfloor-\log_2\kappa.
\qquad\text{(44)}
```

This is an information-theoretic application of the binary Holevo inequality and purification, not an independent novelty claim.

If $`L\lt 2p`$, then $`1+vT\gt L/(4P)`$. For $`L\ge2`$, putting $`\eta=\min\{L,1+vT\}`$ gives

```math
\frac{N}{\eta^d}\log_2(\eta+1)
\le(4P)^d\log_2(L+1),
```

while (44) implies

```math
S(\rho)\ge\frac{wd}{4}\log_2(L+1)
-\frac{w+\log_2\kappa}{2}.
\qquad\text{(45)}
```

Combining (43) and (45) proves (3), for example with

```math
A_{c,\kappa,d,a,\nu}=\frac{w}{4(4P)^d},\qquad
B_{c,\kappa}=1+\frac{w+\log_2\kappa}{2}.
\qquad\text{(46)}
```

The extra unit in $`B`$ also makes the degenerate $`L=1`$ case harmless. Constants are deliberately nonoptimal. For sufficiently large $`N`$, the additive constant can be absorbed to obtain the asymptotic lower frontier. At $`T=0`$, the estimate is conditional on the output satisfying (2); it does not assert that a qualifying state is preparable at zero time.

If the fidelity plateau is assumed only for distances above a fixed microscopic $`\xi_0`$, one can select a fixed-spacing sublattice inside each box. This changes the constants and the static floor by fixed factors/additive terms. A system-size-dependent plateau onset requires a separate statement; it must not be hidden in the constants.

## 7. Matching bounded Hamiltonian preparation

The [local constructions](constructions.md) prove the exact spectrum of the masked block-cat state. For balanced blocks of linear size at most $`\ell`$, with $`K`$ blocks and $`n_b`$ sites in block $`b`$, their strict-product output has

```math
Q\rho=\rho,\quad C=I_N,\quad f_{ij}=1,
\qquad S(\rho)=K-1+\sum_{b=1}^K\lceil\log_2n_b\rceil.
\qquad\text{(47)}
```

Here is a realization by bounded local Hamiltonians, with all auxiliary systems retained until a final local discard. This supplies a continuous-time upper in the same spatial-product resource class as the lower bound.

Start the retained qubits in $`|+\rangle^{\otimes N}`$. Grow a cat along a rooted bounded-degree tree in each block using

```math
V_{pj}=e^{i\pi Z_pY_j/4}.
\qquad\text{(48)}
```

This sends $`|0\rangle_p|+\rangle_j`$ to $`|00\rangle`$ and $`|1\rangle_p|+\rangle_j`$ to $`|11\rangle`$. Its generator commutes with physical $`Q`$. A breadth-first schedule and a bounded edge coloring give time $`O_d(\ell/J)`$.

For each block, use

```math
r_b=\lceil\log_2n_b\rceil
\qquad\text{(49)}
```

local seed qubits at its root, initially in independent $`|+\rangle`$ states. All other copy registers begin in $`|0\rangle`$, independently across sites. Assign the distinct binary labels $`0,\ldots,n_b-1`$ to the sites. Coherently copy the computational-basis seed bits down the block tree by local CNOTs, and apply each site's controlled $`X`$ mask according to its label. The initial full state is still spatially product.

A pipelined broadcast takes the tree height plus the number of seed bits, up to a constant edge-color factor. In each macrostep every edge transmits the next available bit. A bit received at one tree depth is forwarded in the next macrostep; different edge colors keep the number of simultaneous incident operations bounded. Thus

```math
T_{\rm broadcast}\le C_d\frac{h_b+r_b+1}{J},
\qquad h_b=O_d(\ell).
\qquad\text{(50)}
```

The direct coherent implementation stores one copy of each bit at every site, with

```math
n_{{\rm apparatus},j}\le r_b+O_d(1)
=O_d(\log(\ell+1))
\qquad\text{(51)}
```

auxiliary qubits per site. It copies orthogonal computational-basis values; it does not clone arbitrary unknown states. Tracing the seeds and their copies implements the same independent block-mask mixture as in the circuit construction. Site labels and the timing schedule are fixed deterministic controls, rather than an initially shared random resource.

Finally, on one boundary bond per edge of a bounded-degree tree of neighboring blocks, use a local meter $`|0\rangle_e`$ and

```math
U_{ije}=e^{-i(\pi/4)Z_iZ_j\otimes Y_e}.
\qquad\text{(52)}
```

Discarding the meter exactly implements $`\rho\mapsto(\rho+Z_iZ_j\rho Z_iZ_j)/2`$. The boundary operations take constant time after edge coloring and commute with physical $`Q`$. Together with the masks, their spectrum and invariance properties are precisely those proved in [constructions](constructions.md).

Every gate above has a bounded Hermitian generator. Rescale its duration so that its Heisenberg generator obeys (7). Multiple seed-bit operations on one spatial bond are sequential time dependence of a single bond term, not an unbounded simultaneous sum. The total preparation time is

```math
T_{\rm prep}\le\frac{C_d}{J}
\bigl[\ell+\max_b r_b+1\bigr]
\le\frac{C'_d}{J}(\ell+1).
\qquad\text{(53)}
```

For balanced rectangular blocks, $`K=O_d(N/\ell^d)`$ and $`r_b\le\lceil d\log_2\ell\rceil`$. Hence

```math
S(\rho)\le O_d\!\left[
\frac{N}{\ell^d}\log_2(\ell+1)
\right].
\qquad\text{(54)}
```

Given a time budget above a fixed local implementation time, choose $`\ell`$ proportional to $`JT`$, capped at $`L`$, and idle after completion if needed. This matches (3) up to constants for fixed microscopic parameters. At $`\ell=L`$, one block has entropy $`\lceil\log_2N\rceil`$.

The CPTP circuit construction can stream the mask with bounded active workspace by using local resets. The fully unitary implementation above instead keeps $`O(\log\ell)`$ local ancillary qubits until the final trace. These are distinct memory statements. No fixed-on-site-dimension Hamiltonian implementation or exact finite-time system-only Markovian dephasing is claimed here.

## 8. Shared-classical continuous-time lower bound

The weaker causal-volume term also extends to continuous time when an initially shared classical variable $`R`$ is allowed. Conditioned on $`R=\lambda`$, assume the complete input is spatially product and the time-dependent generator satisfies the same fixed bounds (7)–(9), uniformly in $`\lambda`$. Inputs and deterministic controls may depend on $`\lambda`$. Write the actual unconditional output as

```math
\rho=\sum_\lambda\pi_\lambda\rho_\lambda,
\qquad Q\rho=\rho,
\qquad\text{(55)}
```

with the evident integral formulation for a continuous seed. No branch fidelity or branch Gram condition is assumed. The target promises apply to $`\rho`$.

### Strong symmetry balances each branch

Put $`\Pi_-=(I-Q)/2`$. Positivity gives $`\mathrm{Tr}(\Pi_-\rho_\lambda)=0`$ in every positive-weight branch, since these nonnegative quantities average to zero. Hence $`Q\rho_\lambda=\rho_\lambda`$. The anticommutation $`QZ_iQ=-Z_i`$ makes each branch's single-site $`Z_i`$ outcome exactly balanced. This implication requires support in one strong sector; weak invariance under conjugation by $`Q`$ alone does not suffice.

### Conditional cut factorization for single-site outcomes

Choose $`M`$ retained sites, mutually separated by at least $`2r+2a`$, with the radius-$`r`$ expanded single-site cubes inside the lattice. Lemma 1 with $`\ell=1`$ applies in every branch, between a selected site and the entire union of previous selected sites. If

```math
ad\nu(1+2r)^{d-1}(e^{vT}-1)e^{-r/a}\le\epsilon\le1/2,
\qquad\text{(56)}
```

then the corresponding classical joint outcome law is within total-variation distance $`\epsilon`$ of some product law. The same marginal and conditional entropy continuity argument as (28)–(31), now with a two-dimensional first register, gives

```math
H(Z_i\mid Z_{\lt i},R=\lambda)\ge1-\alpha(\epsilon),
\quad
\alpha(\epsilon)=3\epsilon+h_2(\epsilon)
+(1+\epsilon)h_2\!\left(\frac{\epsilon}{1+\epsilon}\right).
\qquad\text{(57)}
```

The first selected bit has entropy exactly one without a continuity correction. Therefore

```math
H(Z_1,\ldots,Z_M)
\ge H(Z_1,\ldots,Z_M\mid R)
\ge M-(M-1)\alpha(\epsilon).
\qquad\text{(58)}
```

The distant collection may be disconnected or extensive. Its size never enters the continuity bound, whose first alphabet has size two.

### Convert outcome entropy into retained-state entropy

For the commuting involutions $`G_i=Z_1Z_i`$, $`2\le i\le M`$, let $`P`$ be their joint outcome law on the unconditional state. The map from $`Z`$ outcomes to these reference parities forgets at most one bit, so $`H(P)\ge H(Z)-1`$.

Successively twirl by the $`G_i`$. Earlier twirls commute with later pair conjugations, so fidelity data processing guarantees that the fidelity at the $`i`$-th step is at least the original unconditional $`f_{1i}`$. Equation (24) bounds that step's entropy increase by $`h_2((1+f_{1i})/2)`$. The final fully twirled state has entropy at least $`H(P)`$, because it is block diagonal in the joint eigenspaces. Thus

```math
S(\rho)\ge H(P)-\sum_{i=2}^M
h_2\!\left(\frac{1+f_{1i}}2\right).
\qquad\text{(59)}
```

Combining with (58), if the actual reference-pair fidelities obey $`f_{1i}\ge c`$, gives the explicit shared-classical continuous-time bound

```math
\boxed{\quad S(\rho(T))\ge(M-1)[w(c)-\alpha(\epsilon)].\quad}
\qquad\text{(60)}
```

No ordinary-Gram assumption was used in (60). No assertion that the conditional states have large fidelity was used either.

### Packing and matching shared frontier

Choose $`\epsilon_s\in(0,1/2)`$ with $`\alpha(\epsilon_s)\le w/2`$. Choose an integer $`A_s\ge\max\{2,d+1\}`$ satisfying

```math
ad\nu(1+2A_sa)^{d-1}e^{-A_s}\le\epsilon_s.
\qquad\text{(61)}
```

Set $`r=A_sa\lceil1+vT\rceil`$, use one selected site in each cell of side $`p_s=1+2r+2a`$, and put $`P_s=1+2A_sa+2a`$. The calculation in (38) verifies (56). If $`L\ge2p_s`$, the number of sites obeys $`M\ge N/[4P_s(1+vT)]^d`$. Equation (60) yields

```math
S(\rho(T))\ge
\frac{w}{2(4P_s)^d}\frac{N}{(1+vT)^d}-\frac w2.
\qquad\text{(62)}
```

If $`L\lt 2p_s`$, a single site gives the zero bound. In this case $`\eta=\min\{L,1+vT\}\gt L/(4P_s)`$, so nonnegativity supplies the capped version of (62):

```math
S(\rho(T))\ge A_s'\frac{N}{\eta^d}-\frac w2,
\qquad A_s'=\frac{w}{2(4P_s)^d}.
\qquad\text{(63)}
```

When the unconditional state also has $`C\preceq\kappa I`$ and all-pair fidelity at least $`c`$, the preparation-independent floor (44) applies. The maximum of (44)/2 and (63) is a valid explicit finite lower bound. For example their half-sum gives

```math
S(\rho(T))\ge
\frac{A_s'}2\frac{N}{\eta^d}
+\frac w4\log_2N
-\frac{2w+\log_2\kappa}{4}.
\qquad\text{(64)}
```

For the matching upper, prepare the coherent blocks and the boundary meters of Section 7, but replace independent in-block seeds by an initially shared classical seed specifying distinct binary labels for all $`N`$ sites. The mask is then a layer of local controlled $`X`$ operations, while the charged Hamiltonian preparation time remains $`O(\ell/J)`$. Its output obeys $`C=I`$, $`f_{ij}=1`$, strong parity, and $`S\le K-1+\lceil\log_2N\rceil`$. Hence the shared-classical frontier in the same Hamiltonian-apparatus setting is

```math
S_{\min}^{\rm sh}(N,T;c,\kappa)
=\Theta_{c,\kappa}\!\left[
\frac{N}{\min\{L,T+1\}^d}+\log_2N
\right]
\qquad\text{(65)}
```

with fixed microscopic interaction units and the same finite-size/implementation-threshold qualifications as above. At arbitrarily short times the shared class also has the separable zero-time baseline $`(I+Q)/2^N`$, initialized using an even-parity shared string of local $`X`$ eigenvalues. This supplies the extensive end of the upper bound without a minimum positive time assumption for that model.

### Optional actual-state sector-leakage correction

If instead $`p=\mathrm{Tr}(\Pi_-\rho)`$ is nonzero, let $`p_\lambda`$ be the branch leakage. Anticommutation gives $`|\langle Z_i\rangle_\lambda|^2\le4p_\lambda(1-p_\lambda)`$, and $`h_2((1+x)/2)\ge1-x^2`$ gives a single-bit entropy at least $`1-4p_\lambda(1-p_\lambda)`$. Apply the same cut and chain argument, then use concavity of $`p(1-p)`$. The actual-state bound becomes

```math
S(\rho(T))\ge(M-1)[w(c)-\alpha(\epsilon)]
-4Mp(1-p).
\qquad\text{(66)}
```

This is a finite quantitative corollary. It does not require a nonlocal sector projection or multiply an error by the full Hilbert-space dimension. The static floor remains available when the actual Gram and fidelity promises still hold.

## 9. Scope and counterexamples

1. **Initially shared classical randomness changes the frontier.** An initially available uniform seed of $`O(\log N)`$ bits can specify a pairwise-independent mask across the whole lattice. Applying it to the $`K`$-block cat/sign construction gives $`C=I`$, $`f_{ij}=1`$, and entropy at most $`K-1+O(\log N)`$, in time $`O(\ell)`$. This can be parametrically smaller than $`K\log\ell`$. Conditional cut factorization for each seed does not imply the unconditional product reference state (27). The strict-product assumption must therefore remain visible.

2. **Uniformly small ordinary pairs are insufficient.** Let $`s^{(1)},\ldots,s^{(M)}\in\{\pm1\}^N`$ be independently chosen sign patterns and mix their positive-parity cat states. Every $`Z_iZ_j`$ acts as a scalar on each cat, so $`f_{ij}=1`$ exactly, and $`Q\rho=\rho`$. For each distinct pair, $`C_{ij}=M^{-1}\sum_\alpha s_i^{(\alpha)}s_j^{(\alpha)}`$. Hoeffding's bound and a union bound give existence with $`\max_{i\ne j}|C_{ij}|\le\zeta`$ for $`M=O(\zeta^{-2}\log N)`$, while $`S(\rho)\le\log_2M`$. Taking $`\zeta_N=(\log N)^{-1/4}`$ gives uniformly vanishing pairs and entropy $`O(\log\log N)`$. There is no contradiction: $`C`$ has rank at most $`M`$, trace $`N`$, and hence $`\|C\|\ge N/M`$, far from a fixed $`\kappa`$.

3. **Ordinary order cannot be omitted.** A pure GHZ state has $`f_{ij}=1`$ and entropy zero, but $`C`$ is the all-ones matrix with norm $`N`$. It violates (2), as required.

4. **Preexisting nonlocal resources cannot be free.** A prepared low-entropy cat-code mixture supplied at time zero need not satisfy the lower scaling. Its preparation time or initial correlation resource must be included. Spatially correlated reservoirs, instantaneous global feedback, and global postselection likewise fall outside (5)–(8).

5. **Locality includes total strength and coordination.** Long-range terms, an unbounded number of overlapping bounded terms, or strength growing with $`N`$ invalidate the fixed $`v`$ statement. Arbitrary local apparatus dimension alone does not: the proof uses the norm and spatial support of the generator, not on-site Hilbert-space dimension.

6. **Root fidelity and fixed parameters matter.** If a source uses squared fidelity, its plateau must be square-rooted before inserting it into $`w(c)`$. If $`c`$ shrinks or $`\kappa`$ grows with $`N`$, (33) remains the useful quantitative statement, but a uniform fixed-parameter frontier does not follow.

7. **The upper is Hamiltonian with local apparatus, not exact finite-time system-only dephasing.** A bounded time-dependent generator on a finite-dimensional system has an invertible finite-time propagator as a linear map; complete dephasing is singular. The boundary dephasing channel is instead realized exactly by (52) and local discard. The lower bound applies to system-only local Markovian dynamics, but this page does not establish a matching exact upper within that narrower class.

8. **Pair diagnostics do not establish all aspects of a phase.** The explicit mask proves zero ordinary single-site $`ZZ`$ correlations and maximal pair-fidelity order. Pairwise-independent columns can leave correlations of composite charged operators. The stronger masks in [constructions](constructions.md) suppress every fixed-support charged correlator with the same asymptotic entropy and preparation scales. The converse here still has its stated finite-system Gram and fidelity assumptions; it does not settle infinite-volume strong-symmetry definitions.

9. **Entropy is retained-system mixedness.** Neither (3) nor (54) is a heat, work, Landauer cost, or irreversible thermodynamic entropy-production theorem. Discarded apparatus entropy and the implementation's thermodynamic accounting are separate quantities.

## 10. Attribution

The local-generator Lieb–Robinson estimate is from [BK12], the binary Holevo/fidelity inequality is from [RFZ10], and the entropy-continuity estimates are from [W16]. Purification/Gram spectral identities and entropy subadditivity are standard ingredients. In particular the one-box logarithmic entropy floor is an application of information theory, rather than a new stand-alone information theorem.

The continuous-time argument combines shell-cut factorization against an arbitrarily large distant region with the local fingerprint Gram representation and a conditional entropy chain. Its finite bounds are (33) for strict product resources and (60), together with (44), for shared classical resources. The propagation constants, diameter cap, and Hamiltonian-apparatus realization above state the physical assumptions under which the two frontiers match.

## References

**[BK12]** Thomas Barthel and Martin Kliesch, “Quasi-locality and efficient simulation of Markovian quantum dynamics,” *Physical Review Letters* **108**, 230504 (2012). DOI: [10.1103/PhysRevLett.108.230504](https://doi.org/10.1103/PhysRevLett.108.230504). Primary version inspected: [arXiv:1111.4210v2](https://arxiv.org/abs/1111.4210v2), 9 August 2012; [PDF](https://arxiv.org/pdf/1111.4210). Relevant material: Section II, Eqs. (1)–(10), Theorem 1/Eq. (12), and the Duhamel argument preceding Eq. (11).

**[RFZ10]** Wojciech Roga, Mark Fannes, and Karol Życzkowski, “Universal bounds for the Holevo quantity, coherent information, and the Jensen–Shannon divergence,” *Physical Review Letters* **105**, 040505 (2010). DOI: [10.1103/PhysRevLett.105.040505](https://doi.org/10.1103/PhysRevLett.105.040505). Primary version inspected: [arXiv:1004.4782v1](https://arxiv.org/abs/1004.4782v1), 27 April 2010; [PDF](https://arxiv.org/pdf/1004.4782). Their Eq. (26) uses squared fidelity and natural logarithms; (24) converts both conventions.

**[W16]** Andreas Winter, “Tight uniform continuity bounds for quantum entropies: conditional entropy, relative entropy distance and energy constraints,” *Communications in Mathematical Physics* **347**, 291–313 (2016). DOI: [10.1007/s00220-016-2609-8](https://doi.org/10.1007/s00220-016-2609-8). Primary version inspected: [arXiv:1507.07775v6](https://arxiv.org/abs/1507.07775v6), 12 January 2016; [HTML](https://arxiv.org/html/1507.07775v6). Lemma 1 gives the marginal entropy bound, with attribution there to Audenaert and Petz; Lemma 2 gives the conditional bound used in (28).
