# Entropy bounds from fidelity orbits

[Model](model.md) · [Entropy tools](entropy_bounds.md) · [Circuit frontiers](circuit_bounds.md) · [Constructions](constructions.md) · [Scope and robustness](scope_and_robustness.md)

These finite-dimensional inequalities supply the [circuit lower bounds](circuit_bounds.md). All entropies use base-two logarithms. Fidelity is the root convention

```math
F(\alpha,\beta)=\|\sqrt\alpha\sqrt\beta\|_1.
```

For the lattice application, write

```math
C_{ij}=\mathrm{Tr}(\rho Z_iZ_j),\qquad
f_{ij}=\|\sqrt\rho Z_iZ_j\sqrt\rho\|_1,
\qquad w(c)=1-h_2((1+c)/2).
```

No spatial or preparation assumptions enter this page. The orbit bounds do not require symmetry. The commuting-twirl bound is a separate tool used when a measurement entropy can be established from locality and sector information.

## Proposition E1: Binary Holevo information from fidelity

For arbitrary density matrices $`\alpha,\beta`$, the equal-prior Holevo information satisfies

```math
\chi(\alpha,\beta)
:=S((\alpha+\beta)/2)-\tfrac12S(\alpha)-\tfrac12S(\beta)
\le h_2((1+F(\alpha,\beta))/2).
\tag{E1}
```

**Proof.** By Uhlmann's theorem choose purifications with nonnegative overlap $`F(\alpha,\beta)`$. Their equal mixture has eigenvalues $`(1\pm F)/2`$, with any zero eigenvalue omitted, and its Holevo information is the binary entropy on the right. Partial trace cannot increase the Holevo information. This proves (E1). This inequality is inherited; see Roga, Fannes and Zyczkowski, PRL **105**, 040505 (2010), [Eq. (26), primary PDF](https://arxiv.org/pdf/1004.4782).

Root fidelity is jointly concave:

```math
F\left(\sum_a p_a\alpha_a,\sum_a p_a\beta_a\right)
\ge\sum_a p_aF(\alpha_a,\beta_a).
\tag{E2}
```

For completeness, choose pairwise optimal purifications and append an orthogonal flag $`a`$. The two flagged superpositions have overlap equal to the right side and purify the two mixtures. Uhlmann's variational characterization proves (E2).

## Proposition E2: Binary-tree Holevo bound

Let $`\{\sigma_a:a\in\{0,1\}^q\}`$ be an equally weighted ensemble, and let $`0\le c_j\le1`$. Suppose

```math
F(\sigma_a,\sigma_{a\oplus e_j})\ge c_j
\quad\text{for every hypercube edge in direction }j.
\tag{E3}
```

Then

```math
\chi(\{2^{-q},\sigma_a\})
\le\sum_{j=1}^q h_2((1+c_j)/2).
\tag{E4}
```

**Proof.** Reveal the label bits in order. At a fixed prefix and the next bit $`j`$, pair the left and right suffixes identically. Each paired state is an edge in direction $`j`$, so joint concavity gives fidelity at least $`c_j`$ between the two child-average states. Their equal-prior Holevo information is at most the corresponding term of (E4). The exact decomposition

```math
\chi(\text{parent ensemble})
=\chi(\text{two child averages})
+\tfrac12\chi(\text{left ensemble})
+\tfrac12\chi(\text{right ensemble})
```

telescopes down the tree. The prefix weights at each level sum to one, yielding (E4). No claim about fidelities between labels differing in several bits is needed.

## Theorem E3: Unitary-orbit entropy bound

Let $`\rho`$ be any finite-dimensional state and let $`U_a`$, indexed by $`a\in\{0,1\}^q`$, be unitaries. Put

```math
\sigma_a=U_a\rho U_a^\dagger,
\qquad G_{ab}=\mathrm{Tr}(\rho U_a^\dagger U_b).
```

If the ensemble satisfies (E3), then

```math
2S(\rho)\ge S(G/2^q)
-\sum_{j=1}^q h_2((1+c_j)/2).
\tag{E5}
```

**Proof.** Choose any purification $`|\psi\rangle_{SE}`$ of $`\rho`$, and set $`|\psi_a\rangle=(U_a\otimes I_E)|\psi\rangle`$. The nonzero spectra of the uniform mixture

```math
\omega_{SE}=2^{-q}\sum_a|\psi_a\rangle\langle\psi_a|
```

and of $`G/2^q`$ coincide: write the matrix with columns $`2^{-q/2}|\psi_a\rangle`$, whose two Gram products are these operators. Thus $`S(\omega_{SE})=S(G/2^q)`$. Every $`E`$ marginal is the same state, of entropy $`S(\rho)`$. Every $`S`$ marginal $`\sigma_a`$ also has entropy $`S(\rho)`$, whence

```math
S(\omega_S)=S(\rho)+\chi(\{\sigma_a\}).
```

Subadditivity and Proposition E2 give

```math
S(G/2^q)=S(\omega_{SE})
\le S(\omega_S)+S(\omega_E)
\le2S(\rho)+\sum_jh_2((1+c_j)/2).
```

This proves (E5). The auxiliary purification need not be locally preparable; no such assumption enters the proof.

## Corollary E4: Global logarithmic floor

Choose $`M=2^q\le N`$ sites, and suppose their ordinary principal Gram matrix obeys $`C_A\preceq\kappa_A I_M`$ and all their pair root fidelities are at least $`c`$. Then

```math
2S(\rho)\ge S(C_A/M)-q\,h_2((1+c)/2)
\ge q w(c)-\log\kappa_A.
\tag{E6}
```

In particular, the ordinary-Gram and pair-fidelity promises in the [model](model.md) imply

```math
S(\rho)\ge\tfrac12[\lfloor\log N\rfloor w(c)-\log\kappa]_+.
\tag{E7}
```

**Proof.** Label the selected sites by $`q`$ bits and choose $`U_a=Z_a`$. Unitary invariance of fidelity gives

```math
F(Z_i\rho Z_i,Z_j\rho Z_j)=f_{ij}(\rho).
```

The orbit Gram is $`C_A`$. Since $`C_A/M`$ is a density matrix with largest eigenvalue at most $`\kappa_A/M`$, its entropy is at least $`\log M-\log\kappa_A`$. Apply Theorem E3. Nonnegativity of entropy supplies the positive part.

This theorem does not use strong symmetry, spatial locality, or a preparation assumption.

## Proposition E5: Commuting binary twirls

For commuting Hermitian involutions $`V_1,\ldots,V_k`$, let $`P`$ be their joint projective measurement law on $`\rho`$, and put $`g_j=F(\rho,V_j\rho V_j)`$. Then

```math
S(\rho)\ge H(P)-\sum_{j=1}^kh_2((1+g_j)/2).
\tag{E8}
```

**Proof.** Apply $`\mathcal D_j(\sigma)=(\sigma+V_j\sigma V_j)/2`$ successively. Each entropy increase is the equal-prior Holevo information of two unitarily related states. Earlier twirls commute with conjugation by $`V_j`$, so fidelity data processing gives

```math
F(\mathcal D_{\lt j}\rho,V_j\mathcal D_{\lt j}\rho V_j)\ge g_j.
```

The function $`h_2((1+g)/2)`$ decreases on $`[0,1]`$; Proposition E1 bounds the $`j`$-th increase by the corresponding term of (E8). The final state is block diagonal in the joint eigenspaces of the $`V_j`$. Its entropy is $`H(P)`$ plus a nonnegative average within-block entropy. Telescoping proves the claim. Linear dependencies among the involutions cause no problem because $`P`$ is the actual joint outcome law.

## Proposition E6: Maximal-fidelity endpoint

Suppose $`f_{ij}=1`$ for every distinct pair and $`C\preceq\kappa I`$. Then

```math
S(\rho)\ge[\log N-\log\kappa]_+.
\tag{E9}
```

**Proof.** Unit root fidelity means equality of the two states, so $`\rho`$ commutes with every $`Z_iZ_j`$. Their common eigenspaces are the parity sectors $`\mathrm{span}\{|s\rangle,|-s\rangle\}`$, where $`s\in\{\pm1\}^N`$ and one representative is chosen from each pair $`s,-s`$. Write their weights as $`p_s`$. Block diagonality gives $`S(\rho)\ge H(p)`$. On a parity sector, $`Z_iZ_j`$ has the scalar value $`s_is_j`$, hence

```math
C=\sum_s p_s\,s s^{\mathsf T}.
```

Each positive summand is bounded above by $`C`$. Since $`\|s\|^2=N`$, the bound $`C\preceq\kappa I`$ implies $`p_sN\le\kappa`$. Therefore every nonzero probability is at most $`\kappa/N`$, and $`H(p)\ge\log N-\log\kappa`$. Nonnegativity supplies the positive part.

If $`Q\rho=\rho`$ as well, each occupied parity sector contributes only its even cat $`(|s\rangle+|-s\rangle)/\sqrt2`$, so $`S(\rho)=H(p)`$. For $`C=I`$, the $`N-1`$ relative parities to a fixed site are pairwise-independent balanced bits. The endpoint entropy bound is the inherited classical orthogonal-matrix argument; see [Gavinsky--Pudlak](https://arxiv.org/abs/1503.08154). It is not a separate novelty claim.

For $`N`$ a power of two, the [single-block Hadamard construction](constructions.md#proposition-c3-shared-classical-masks) has entropy exactly $`\log N`$ and attains this endpoint at $`\kappa=1`$. For arbitrary $`N`$, the unrestricted strong-sector state optimization lies between $`\log N`$ and $`\lceil\log N\rceil`$; the same construction supplies the upper bound. Local preparation of that single block still requires the depth stated in the construction account.

## Attribution and use

The binary Holevo--fidelity inequality, Uhlmann's theorem, fidelity data processing, and entropy subadditivity are established ingredients. The proof organization here is useful for the preparation problem; these ingredients are not claimed as new. The static logarithmic scale also follows from an almost-independent-subset theorem and the parity-information bound: see [Babai's manuscript](https://people.cs.uchicago.edu/~laci/papers/13augEntropy.pdf) and [Gavinsky--Pudlak](https://arxiv.org/abs/1503.08154).

The physical claim is the [matched preparation frontier](circuit_bounds.md#theorem-b7-matched-circuit-frontiers), including the different power of initially shared classical coordination. The [related-work account](../references/related_work.md) credits the environmental interpretation of fidelity order and the classical masking constructions. The [scope page](scope_and_robustness.md) explains why the ordinary Gram promise cannot be replaced by qualitative correlation decay.
