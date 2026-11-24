# Block masks with a shared seed budget

[Educational anchor](anchor.md) · [Milestone map](milestones.md) · [General constructions](../science/constructions.md)

Four neighboring spins show what a single shared bit changes. Two explicit states have the same ordinary pair correlations and maximal pair fidelity. The product preparation leaves **three bits** of entropy, and one preshared bit lowers the retained entropy to **two bits**. An [eight-spin example](#eight-spins-with-zero-one-or-two-shared-bits) then gives an intermediate budget between independent masks and fully shared masks.

This is a complete finite example of the construction. The [circuit bounds](../science/circuit_bounds.md) establish the general optimal scaling; the example alone does not prove a one-bit lower bound at a particular four-spin depth.

## The physical system and two observables

Label the spins $`1,2,3,4`$ and divide them into neighboring blocks $`A=\{1,2\}`$ and $`B=\{3,4\}`$. The computational basis is $`|z_1z_2z_3z_4\rangle`$. The Pauli operator $`X_i`$ flips bit $`z_i`$, while $`Z_i`$ multiplies the basis vector by $`(-1)^{z_i}`$. Define

```math
Q=X_1X_2X_3X_4.
```

We require $`Q\rho=\rho`$: the entire state occupies the plus eigenspace of $`Q`$. We compare two diagnostics:

```math
C_{ij}=\mathrm{Tr}(\rho Z_iZ_j),
\qquad
f_{ij}=F(\rho,Z_iZ_j\rho Z_iZ_j),
\qquad
F(\alpha,\beta)=\|\sqrt\alpha\sqrt\beta\|_1.
```

The first is an ordinary expectation. The second asks how much the **whole density matrix** changes under a pair of $`Z`$ operations. Fidelity uses the root convention, as in [Watrous, Section 3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

## One block has two labels

For bits $`a,s\in\{0,1\}`$, define the four Bell states

```math
|\beta_{a,s}\rangle
=\frac{|0,a\rangle+(-1)^s|1,1\oplus a\rangle}{\sqrt2}.
```

The symbol $`\oplus`$ means addition modulo two. The bit $`a`$ specifies whether the two computational bits agree; $`s`$ specifies their relative phase. Directly,

```math
(Z\otimes Z)|\beta_{a,s}\rangle=(-1)^a|\beta_{a,s}\rangle,
\qquad
(X\otimes X)|\beta_{a,s}\rangle=(-1)^s|\beta_{a,s}\rangle.
```

Different pairs $`(a,s)`$ label orthogonal states. Every individual spin of every Bell state has reduced density matrix $`I/2`$, so every one-spin $`Z`$ expectation vanishes.

Starting from $`|\beta_{0,0}\rangle=(|00\rangle+|11\rangle)/\sqrt2`$, applying $`X`$ to the second spin changes $`a`$. Applying $`Z`$ to either spin changes $`s`$, possibly with an irrelevant overall sign.

## The two preparations

All retained spins begin in $`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$. The following three channel layers prepare the example.

**Layer 1: form the two coherent blocks.** Apply $`V_{12}`$ and $`V_{34}`$ in parallel, where

```math
V_{ij}=\exp(i\pi Z_iY_j/4),\qquad Y=iXZ.
```

Substitution shows that $`V_{ij}|+,+\rangle=|\beta_{0,0}\rangle`$. Also $`[V_{ij},X_iX_j]=0`$, so this step preserves the charge. The output is the pure product of two Bell states.

**Layer 2: apply the masks.** Apply $`X_2^aX_4^b`$ and discard the mask records.

- In the **product-resource preparation**, $`a`$ and $`b`$ are independent fair bits generated at their respective sites.
- In the **shared-classical preparation**, set $`a=b=y`$ for one fair bit $`y`$ preloaded at both control sites before the charged run. Conditional on $`y`$, the controls act locally. Their correlation is an explicit input resource.

The product model's two-spin block needs no internal broadcast because its mask acts on only one spin. For larger blocks, the general construction charges the actual propagation of seed bits.

**Layer 3: mix the relative charge signs.** On the neighboring boundary spins $`2,3`$, apply

```math
\mathcal D_{23}(\sigma)
=\frac{\sigma+Z_2Z_3\sigma Z_2Z_3}{2}.
```

This is one local channel, realized by an independent fair coin $`s`$ followed by discarding that coin. It changes the Bell phase in both blocks together. The local block charges become $`(-1)^s`$ and $`(-1)^s`$, while their product remains plus.

Every branch of every layer commutes with $`Q`$. All records are discarded, and no measurement outcome is selected. The shared protocol does not generate its common mask bit instantaneously during layer 2; it uses the allowed initial correlation. Producing and distributing that bit after a product-resource run starts would require local signal propagation.

## Exact final states and entropies

Write

```math
|\psi_{a,b,s}\rangle
=|\beta_{a,s}\rangle_{12}\otimes|\beta_{b,s}\rangle_{34}.
```

The boundary operation produces these vectors up to an overall sign, which disappears from their projectors. The actual retained states are

```math
\rho_{\mathrm{prod}}
=\frac18\sum_{a,b,s=0}^1
|\psi_{a,b,s}\rangle\langle\psi_{a,b,s}|,
```

```math
\rho_{\mathrm{sh}}
=\frac14\sum_{y,s=0}^1
|\psi_{y,y,s}\rangle\langle\psi_{y,y,s}|.
```

All eight vectors in the first sum are orthonormal. The second sum contains four of them. The nonzero eigenvalues are therefore $`1/8`$ and $`1/4`$, respectively. Applying $`S(\rho)=-\sum_k\lambda_k\log_2\lambda_k`$ gives

```math
S(\rho_{\mathrm{prod}})=3,\qquad
S(\rho_{\mathrm{sh}})=2.
```

This is a spectral calculation of the final states. Counting random bits gives the same answer here because the chosen labels identify orthogonal states; seed length would not determine entropy for a general preparation.

An equivalent matrix description makes the supports visible. Let $`P=Z_1Z_2Z_3Z_4`$. Since $`Q`$ and $`P`$ commute,

```math
\rho_{\mathrm{prod}}=\frac{I+Q}{16},
\qquad
\rho_{\mathrm{sh}}=\frac{(I+Q)(I+P)}{16}.
```

The first state is uniform on the eight-dimensional $`Q=+1`$ sector. The shared state also has $`P=+1`$, so it is uniform on a four-dimensional joint sector.

| Quantity | Independent masks | Shared mask |
|---|---:|---:|
| Mask bits | Two independent bits $`a,b`$ | One bit $`y`$ used twice |
| Independent boundary coin | One | One |
| Number of occupied orthogonal states | 8 | 4 |
| Final von Neumann entropy | 3 bits | 2 bits |
| Global charge | $`Q=+1`$ | $`Q=+1`$ |

## What the two diagnostics say

For spins in the same block, the ordinary pair expectations are the averages of $`(-1)^a`$ and $`(-1)^b`$. They vanish because each mask bit is fair, whether or not the bits are independent.

For spins in different blocks, each pure branch is a product across the blocks, and each one-spin $`Z`$ expectation is zero. The cross-block expectations therefore vanish before averaging. Consequently both states have

```math
C_{ij}=\delta_{ij}.
```

Now consider $`Z_iZ_j`$ with $`i\ne j`$. It commutes with $`Q`$ because it flips two charge signs. It also commutes with $`P`$. The matrix formulas above therefore give

```math
Z_iZ_j\rho Z_iZ_j=\rho,
\qquad f_{ij}=F(\rho,\rho)=1
```

for either state and every pair. The branch picture gives the same result: a within-block pair changes only an irrelevant phase, while a cross-block pair exchanges the equally likely $`s=0`$ and $`s=1`$ sectors.

A single $`Z_i`$ instead takes either state into the orthogonal $`Q=-1`$ sector. Its root fidelity with the original state is zero. Thus zero ordinary pair correlation, unit pair fidelity, and zero single-operator fidelity are compatible.

## Measurements expose different kinds of randomness

A joint measurement of the commuting observables $`Z_1Z_2,X_1X_2,Z_3Z_4,X_3X_4`$ identifies the Bell labels. Its outcomes are the eight equally likely triples $`(a,b,s)`$ for the product preparation or the four equally likely pairs $`(y,s)`$ for the shared preparation. This measurement distinguishes the orthogonal states used in the entropy calculation.

Measuring all four spins individually in the computational basis gives a different distribution. For $`\rho_{\mathrm{prod}}`$, all 16 strings are equally likely, with classical entropy four bits. For $`\rho_{\mathrm{sh}}`$, the eight even-parity strings are equally likely, with classical entropy three bits. These exceed the respective von Neumann entropies: a chosen measurement's outcome entropy is not generally the quantum state's entropy.

The shared state retains the higher correlation

```math
\mathrm{Tr}(\rho_{\mathrm{sh}}Z_1Z_2Z_3Z_4)=1.
```

It can be written as a correlation between the charged operators $`Z_1`$ and $`Z_2Z_3Z_4`$. Hence $`C=I`$ alone does not eliminate all higher charged correlations. The [stronger-mask construction](../science/constructions.md#7-masks-that-suppress-general-local-charged-correlations) addresses this additional requirement without changing the asymptotic entropy scale.

## What the example establishes

The shared mask ties two within-block labels together without changing any of the required pair diagnostics. That removes one independent label from the final orthogonal mixture. The saved entropy is a property of the retained spins, not a conditional entropy obtained by keeping the seed.

For $`K`$ equal blocks of a power-of-two size $`m`$, the general baseline construction replaces each block's one-bit mask by $`\log_2m`$ bits. Its exact entropies become

```math
S_{\mathrm{prod}}=K-1+K\log_2m,
\qquad
S_{\mathrm{sh}}=K-1+\log_2m.
```

Local propagation determines which block sizes are available within a depth budget. The matching converse is what turns this family of examples into the two optimal scaling laws.

The four-spin shared state also reaches the preparation-independent maximal-fidelity floor $`\log_2 4=2`$ from [Proposition E6](../science/entropy_bounds.md#proposition-e6-maximal-fidelity-endpoint). The value three in the explicit product preparation is not a claim of finite-depth optimality. Indeed, after the first Bell-preparation layer, a single boundary channel that independently randomizes $`X_2X_3`$ and $`Z_2Z_3`$ prepares the same two-bit state using only product initial resources. The $`X_2X_3`$ operation toggles both block mask labels locally, up to an irrelevant phase. This special four-spin alternative does not extend to free coordination among arbitrarily distant blocks. The general converse and charged propagation, rather than this example alone, establish the asymptotic resource separation.

## Eight spins with zero, one, or two shared bits

Use two adjacent blocks of four spins. Give the sites in each block the labels $`00,10,01,11`$, with $`00`$ at the anchor. Grow a plus GHZ state in each block. For a two-bit seed $`a=(a_1,a_2)`$, apply $`X`$ at the sites where the dot product with $`a`$ is one. The resulting mask pattern in the first block is $`u(a)=(0,a_1,a_2,a_1\oplus a_2)`$. The second block uses its own seed $`b`$ in the same table. Reading the two basis-vector labels of a canonical pattern determines its seed.

For $`s=0,1,2`$, share the first $`s`$ coordinates of $`a`$ and $`b`$ before the run. Generate the remaining $`2-s`$ bits independently in each block, and propagate them within the block as needed. Apply a fair boundary channel to a neighboring pair across the blocks, as in the four-spin example. Its independent coin sets the same cat phase $`\epsilon`$ in both blocks.

Let $`|u;\epsilon\rangle=(|u\rangle+(-1)^\epsilon|u\oplus 1111\rangle)/\sqrt2`$. If $`a_{1:s}=b_{1:s}`$ denotes agreement on the shared prefix, the exact retained state is

```math
\rho_s=
2^{-(5-s)}
\sum_{\substack{a,b\in\mathbb F_2^2\\a_{1:s}=b_{1:s}}}
\sum_{\epsilon=0}^1
\bigl(|u(a);\epsilon\rangle\langle u(a);\epsilon|\bigr)
\otimes
\bigl(|u(b);\epsilon\rangle\langle u(b);\epsilon|\bigr).
```

The terms are orthogonal because different canonical masks or different phase signs distinguish the underlying cat states. All allowed labels have the same probability. The phase contributes one bit regardless of how the masks are generated.

| Shared entropy used | Seed arrangement | Rank | Each nonzero eigenvalue | $`S(\rho_s)`$ |
|---:|---|---:|---:|---:|
| 0 bits | Both coordinates generated independently in each block | 32 | $`1/32`$ | 5 bits |
| 1 bit | One common coordinate and one new coordinate per block | 16 | $`1/16`$ | 4 bits |
| 2 bits | Both coordinates common to the two blocks | 8 | $`1/8`$ | 3 bits |

For every budget in the table, the seed within either block is uniform. Different site labels in one block therefore give mean pair sign zero. Across blocks, every pure cat branch has a zero single-spin $`Z`$ mean, so the cross-block correlation vanishes as well. The same phase bit in both blocks keeps the total charge positive. A cross-block $`Z_iZ_j`$ toggles both phases and preserves the equally weighted mixture, and a within-block pair preserves each projector. Thus all three states have $`C=I_8`$ and all pair fidelities equal to one.

In $`K`$ equal blocks with $`2^r`$ sites each, the same construction has $`K-1`$ boundary phase bits, $`s`$ common mask bits and $`K(r-s)`$ independent mask bits for any integer $`0\le s\le r`$. Each additional common bit replaces $`K`$ independent mask bits by one, reducing the entropy of this construction by $`K-1`$ bits. The [seed-budget theorem](../science/shared_seed_budget.md) bounds all local protocols with $`H(R)\le h`$, including a biased shared seed and seed-dependent local controls. Its asymptotic law is separate from finite-size optimality of the examples above.
