# Consuming a pure controller

A controller that may change its state enables exponentially small gate error with increasing Hermitian dissipative action. The construction below implements the complete channel

```math
\mathcal E_m=q^m\,\mathrm{id}+(1-q^m)\mathcal U,
\qquad
q=\frac{1+e^{-2a}}2,
\qquad A=ma,
```

using a controller of dimension $`m+1`$ initially in a pure state. At fixed stage action $`a\gt 0`$, the error is exponentially small in $`A`$. The full joint output is also close to the target gate tensored with a known changed controller state.

This is an achievability result. It establishes no universal logarithmic-action lower bound for arbitrary protocols with discardable controllers. Its comparison with returned controllers relies on the dimension-independent converse, not on an asserted optimal cost for every disposable implementation.

A [separate rotating-flag construction](fixed-dimension-controllers.md) holds the controller dimension fixed at $`m+1`$ and achieves reduced data-channel error $`O_U(A^{-m})`$. Its qutrit case already improves the inverse-action error power. The growing dimension in the construction below is therefore relevant to the demonstrated exponential rate, rather than necessary for every qualitative advantage.

## Model and resource accounting

The data system $`S`$ is finite dimensional, and $`U`$ is a fixed target unitary with channel $`\mathcal U(\rho)=U\rho U^\dagger`$. There is no Hamiltonian term. The allowed generators have Hermitian jumps and are scheduled in advance, without monitoring, feedback, postselection, or intermediate controller resets:

```math
\mathcal D[L](X)=LXL^\dagger-\frac12\{L^\dagger L,X\},
\qquad L=L^\dagger.
```

The charged action is the induced Hilbert–Schmidt generator norm

```math
A=\frac12\int\|\mathcal L_t\|_{2\to2}\,dt.
```

The norm is induced on operators equipped with $`\|X\|_2^2=\mathrm{Tr}(X^\dagger X)`$. It is not the Frobenius norm of a superoperator matrix. The [mixed-controller note](mixed-controllers.md) gives the general model and the relation to the sum-of-jump-norm budget. These two action conventions agree for the jumps used below.

The controller has an orthonormal basis $`|0\rangle,|1\rangle,\ldots,|m\rangle`$ and starts in $`|0\rangle`$. The basis state $`|0\rangle`$ records the branch on which the gate has not yet been applied; $`|j\rangle`$ records the branch on which stage $`j`$ applied it. These are labels for the unconditioned quantum channel. No flag is measured during the protocol.

## 1. One Hermitian stage

During stage $`j`$, apply only the jump

**(1)**

```math
L_j=\sqrt\gamma\left(
 U\otimes|j\rangle\langle0|
 +U^\dagger\otimes|0\rangle\langle j|
 \right)
```

for time $`\tau=a/\gamma`$, where $`\gamma\gt 0`$ and $`a\gt 0`$. It satisfies

```math
L_j^\dagger=L_j,
\qquad
L_j^2=\gamma I_S\otimes
 (|0\rangle\langle0|+|j\rangle\langle j|).
```

Its spectrum on the active subspace consists of $`+\sqrt\gamma`$ and $`-\sqrt\gamma`$; all other flag subspaces have eigenvalue zero. Since the eigenvalues of $`\mathcal D[L_j]`$ are $`-(\ell_r-\ell_s)^2/2`$ in an eigenoperator basis of $`L_j`$,

```math
\|\mathcal D[L_j]\|_{2\to2}=2\gamma.
```

The stage action is therefore exactly $`a`$, and its jump norm also gives $`\tau\|L_j\|_\infty^2=a`$.

Starting from a data operator $`\rho`$ in flag $`0`$, the evolution remains in the two-block form

```math
p_0(t)\,\rho\otimes|0\rangle\langle0|
+p_j(t)\,U\rho U^\dagger\otimes|j\rangle\langle j|.
```

The scalar coefficients obey

```math
\frac{d}{dt}
\begin{pmatrix}p_0\\p_j\end{pmatrix}
=\gamma
\begin{pmatrix}-1&1\\1&-1\end{pmatrix}
\begin{pmatrix}p_0\\p_j\end{pmatrix},
\qquad(p_0(0),p_j(0))=(1,0).
```

At the end of the stage,

**(2)**

```math
p_0(\tau)=q:=\frac{1+e^{-2a}}2,
\qquad p_j(\tau)=1-q.
```

The jump is a symmetric exchange, so a single stage has backflow and cannot become a one-way absorbing transition. The subsequent schedule protects the completed branch by never addressing its flag again: for $`k\notin\{0,j\}`$, $`L_j`$ and $`L_j^2`$ annihilate the entire flag-$`k`$ subspace.

The calculation is an operator identity. It remains valid when $`\rho`$ is entangled with an inert reference, with $`U`$ replaced by $`U\otimes I_R`$.

## 2. Complete joint channel after all stages

Apply stages $`1,2,\ldots,m`$ in this fixed order. At the start of stage $`j`$, its flag $`j`$ is unoccupied, while every earlier successful flag is dark for the new jump. Induction using (2) gives the exact complete joint channel

**(3)**

```math
\mathcal F_m(\rho)
=q^m\rho\otimes|0\rangle\langle0|
+\sum_{j=1}^m(1-q)q^{j-1}
 U\rho U^\dagger\otimes|j\rangle\langle j|.
```

The coefficients sum to one. Every stage and branch is included; there is no successful-outcome conditioning. The total generator action is

**(4)**

```math
A=ma.
```

Taking the partial trace over the controller yields

**(5)**

```math
\mathcal E_m=q^m\,\mathrm{id}+(1-q^m)\mathcal U.
```

Define the fixed target displacement $`s(U)=\tfrac12\|\mathcal U-\mathrm{id}\|_\diamond`$. Equation (5) gives the exact reduced error

**(6)**

```math
\epsilon_m:=\frac12\|\mathcal E_m-\mathcal U\|_\diamond
=q^m s(U).
```

The controller's final marginal is independent of the input:

**(7)**

```math
\beta_m
=q^m|0\rangle\langle0|
+\sum_{j=1}^m(1-q)q^{j-1}|j\rangle\langle j|.
```

A stronger joint-output statement follows by comparing (3) with $`\mathcal U(\rho)\otimes\beta_m`$. Their difference is supported only on flag $`0`$:

```math
\mathcal F_m(\rho)-\mathcal U(\rho)\otimes\beta_m
=q^m[\rho-U\rho U^\dagger]\otimes|0\rangle\langle0|.
```

Consequently,

**(8)**

```math
\frac12\left\|\mathcal F_m-
 \bigl(\rho\mapsto\mathcal U(\rho)\otimes\beta_m\bigr)
 \right\|_\diamond
=q^m s(U).
```

Equation (8) includes arbitrary data references. The supplied pure controller has nevertheless changed substantially:

**(9)**

```math
\frac12\|\beta_m-|0\rangle\langle0|\|_1=1-q^m.
```

Thus high gate accuracy does not provide approximate return to the initial pure controller. The accurate joint product in (8) contains $`\beta_m`$, not $`|0\rangle\langle0|`$.

## 3. Action, dimension, and locality

For a fixed $`a\gt 0`$, define $`\kappa(a)=-\ln q/a\gt 0`$. Equations (4) and (6) become

```math
\epsilon_m=s(U)e^{-\kappa(a)A}.
```

For $`0\lt \epsilon\lt s(U)`$, one may choose

**(10)**

```math
m=\left\lceil\frac{\ln[s(U)/\epsilon]}{-\ln q}\right\rceil,
\qquad
A=am,
\qquad
D_C=m+1.
```

Hence, for every fixed nontrivial target and fixed stage action,

```math
A=O_U(\ln(1/\epsilon)),
\qquad
D_C=O_U(\ln(1/\epsilon)).
```

If the controller is embedded into a qubit register, its Hilbert-space dimension requires

```math
n_C=\lceil\log_2(m+1)\rceil
=O_U(\log\log(1/\epsilon))
```

qubits. This is a width statement only. The transition $`|j\rangle\langle0|`$ may act on the whole binary-encoded controller, so (10) supplies no fixed-qubit-local implementation or efficient compilation of that transition. A physical controller with $`m+1`$ addressable levels realizes the stated level count directly.

The target $`U`$ is explicitly encoded in the permitted jump (1). The algebraic construction does not supply the cost of engineering this coupling, or a reduction in ordinary coherent gate complexity. Increasing the target's size can make the jump itself a complicated many-body control even though the action accounting remains well defined.

### What is and is not optimal here

For this particular sequential exchange family, one may use unequal stage actions $`a_j`$. The failure probability is then $`\prod_j q(a_j)`$, and

```math
q(a_j)=e^{-a_j}\cosh a_j\ge e^{-a_j},
\qquad
\prod_jq(a_j)\ge e^{-\sum_j a_j}=e^{-A}.
```

Its error therefore satisfies $`\epsilon\ge s(U)e^{-A}`$. The fixed-$`a`$ construction has the optimal logarithmic action order within this exchange family.

There is no corresponding unrestricted discarded-controller converse in this note. In a general Hermitian-jump protocol, the no-jump Kraus operator is a time-ordered product generated by $`-\tfrac12\sum_jL_j(t)^2`$. That product need not preserve the initial data orientation. Treating every no-jump trajectory as an identity branch would therefore not establish a universal error floor. The valid conclusion is an exponential construction and its separation from the returned-controller bound.

## 4. Entropy of the changed controller

The distribution in (7) is a geometric first-completion distribution with a final failure outcome. Let

```math
h_2(q)=-q\log_2q-(1-q)\log_2(1-q).
```

The controller entropy in **bits** is exactly

**(11)**

```math
H_2(\beta_m)
=h_2(q)\sum_{k=0}^{m-1}q^k
=\frac{h_2(q)}{1-q}(1-q^m)
\le\frac{h_2(q)}{1-q}.
```

One way to see (11) is the recursion $`H_m=h_2(q)+qH_{m-1}`$ with $`H_0=0`$: a completed branch terminates the flag distribution, while the remaining branch has weight $`q`$. The von Neumann entropy with natural logarithms is $`S(\beta_m)=(\ln2)H_2(\beta_m)`$. Equation (11) is independent of $`m`$ at fixed $`a`$; for the limiting value $`q\downarrow1/2`$, its infinite-stage upper limit approaches two bits.

The controller dimension grows as accuracy improves, but its final entropy remains bounded. These are distinct resources. Relative to a uniform state on the same $`D_C`$-dimensional space, the nonuniformity in bits changes from $`\log_2D_C`$ initially to $`\log_2D_C-H_2(\beta_m)`$ finally. The amount lost is bounded, while the initially available pure state occupies an increasingly large space. Equation (9) also shows that a bounded entropy increase does not imply return of the initial state.

No reset of $`\beta_m`$ to $`|0\rangle`$ is included. A cyclic implementation must supply and account for that additional process and any correlations used by it. The action $`A`$ is dimensionless generator action, not heat or work; the entropy calculation alone makes no heat or work claim for resetting the controller.

## 5. Three operational contracts

All three rows below use the same deterministic, unmonitored, zero-Hamiltonian Hermitian-jump model and the same generator action. The target is fixed and nontrivial.

| Controller contract | Initial controller | Final accuracy or return requirement | Established action scaling |
|---|---|---|---|
| Approximate clean joint return | Pure $`\lvert0\rangle`$ | The complete output is within error $`\epsilon`$ of $`\mathcal U(\rho)\otimes\lvert0\rangle\langle0\rvert`$, including data references. | $`\Theta_U(\epsilon^{-1})`$; the matching construction uses one controller qubit. |
| Exact mixed marginal return | Arbitrary finite $`\beta`$ | The data gate has error $`\epsilon`$ and the controller marginal equals $`\beta`$ exactly for every input; data–controller correlations are allowed. | $`\Omega_U(\epsilon^{-1})`$ for all targets; matching $`\Theta(\epsilon^{-1})`$ for $`Z`$ with one maximally mixed controller qubit. |
| Consumed pure controller | Pure $`\lvert0\rangle`$ in dimension $`m+1`$ | The data gate has error $`\epsilon`$; the final controller may change. Equation (8) also supplies joint accuracy relative to the changed state $`\beta_m`$. | Achievable $`O_U(\ln(1/\epsilon))`$ with $`D_C=O_U(\ln(1/\epsilon))`$; no unrestricted matching lower bound is asserted. |

The second row's converse actually requires exact return only for the maximally mixed data input. This weaker hypothesis is automatic if the controller starts maximally mixed, since the global maximally mixed state is fixed by every unital evolution. Accordingly, an initially maximally mixed controller obeys the inverse-error lower bound even if its output is discarded. The fast construction above uses an initially pure resource whose marginal changes.

Exact return of a **pure** controller is also stronger than the first row: its support must be invariant throughout, whereas approximate joint return permits the intermediate excursions used in the clean-return construction. The mixed $`Z`$ construction proves the second row with exact marginal return and does not replace that distinction by an exact-pure-return claim.

## Prior dissipative flag constructions

Gautier, Mirrahimi, and Sarlette's *Designing High-Fidelity Zeno Gates for Dissipative Cat Qubits*, PRX Quantum **4**, 040316 (2023), Section VIII, “Discrete jump,” and equations (33)–(35), already uses an ancillary dissipative mechanism to produce a discrete gate with exponentially improving accuracy. Its correlated one-way jump is non-Hermitian and its initialized auxiliary changes state. Flagged dissipative gates and exponential gate accuracy are therefore established prior ideas. [Primary article and DOI](https://doi.org/10.1103/PRXQuantum.4.040316).

The construction here realizes a related completion record using only Hermitian, hence unital, exchange stages, with every flag level counted. Its role is to exhibit a fast protocol within the same generator class in which returning the supplied controller forces inverse-error action. The scientific comparison concerns the return promise and consumable controller nonuniformity under that common restriction.
