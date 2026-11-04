# Inverse action law for a returned pure helper

A nontrivial unitary gate implemented by deterministic, unobserved Hermitian-jump dynamics has an inverse-accuracy action cost when its initially pure helper must be returned as part of the output. The lower bound permits arbitrary finite helper dimension and arbitrary time dependence. It follows from a relation between displacement and purity loss, with the action defined directly from the generator.

The [two-stage construction with one helper qubit](pure-helper.md) attains the same inverse-accuracy order for every finite-dimensional target unitary.

## Model and error convention

Let $`S`$ be a finite-dimensional data system and $`C`$ a finite-dimensional helper. The helper starts in $`|0\rangle\langle0|_C`$, independently of the data and of any reference entangled with the data. The joint state evolves according to

```math
\frac{d\sigma_t}{dt}=\mathcal L_t(\sigma_t),
\qquad
\mathcal L_t(X)
=\sum_j\left(L_j(t)XL_j(t)-\frac12\{L_j(t)^2,X\}\right)
=-\frac12\sum_j[L_j(t),[L_j(t),X]],
\qquad L_j(t)=L_j(t)^\dagger.
```

The laboratory generator has zero Hamiltonian term. The jump schedule is predetermined and independent of the input. Bath outcomes are unobserved, and the protocol has a fixed terminal time. The model supplies the chosen time-dependent Hermitian jumps; it includes no intermediate reset, fresh ancillary state injected during the evolution, postselection, or free coherent encoding or endpoint decoder. All helper systems used by the protocol belong to $`C`$ at the initial time.

For almost every time, the generator has a finite Hermitian-jump representation of the displayed form. We assume that $`\mathcal L_t`$ is measurable and has integrable norm. In finite dimension these conditions give an absolutely continuous propagator, and the differential identities below hold almost everywhere.

For operators, use the Hilbert–Schmidt norm $`\|X\|_2=(\mathrm{Tr}X^\dagger X)^{1/2}`$. The action is

```math
A=\frac12\int_0^T\|\mathcal L_t\|_{2\to2}\,dt,
\qquad
\|\mathcal L_t\|_{2\to2}
=\sup_{X\ne0}\frac{\|\mathcal L_t(X)\|_2}{\|X\|_2}.
```

Let $`\mathcal E_{T,0}`$ denote the propagator on $`SC`$. The channel from the data input to the joint output and the desired channel are

```math
\mathcal N(\rho)
=\mathcal E_{T,0}\bigl(\rho\otimes|0\rangle\langle0|_C\bigr),
\qquad
\mathcal T_U(\rho)
=U\rho U^\dagger\otimes|0\rangle\langle0|_C.
```

Throughout, the two dimensionless distances are

```math
\varepsilon=\frac12\|\mathcal N-\mathcal T_U\|_\diamond,
\qquad
s=s(U)=\frac12\|\mathrm{Ad}_U-\mathrm{id}_S\|_\diamond,
\qquad
\mathrm{Ad}_U(\rho)=U\rho U^\dagger.
```

Both lie in $`[0,1]`$. A nontrivial target means $`s>0`$, equivalently that $`U`$ is not a scalar multiple of the identity. The error $`\varepsilon`$ is a joint error: it compares the data, the helper, and their correlations to the required product output. Its diamond norm also includes arbitrary initial entanglement between the data and an inert reference. The helper is approximately returned under this one joint criterion.

For a difference of channels, the diamond distance has the operational expression

```math
\frac12\|\mathcal M-\mathcal Q\|_\diamond
=\max_{\rho_{SR}}\frac12
\left\|\bigl[(\mathcal M-\mathcal Q)\otimes\mathrm{id}_R\bigr](\rho_{SR})\right\|_1,
\qquad \dim R=\dim S.
```

The maximum can be taken over pure states by convexity. This expression fixes the convention for every channel distance used below.

## Generator action and representation accounting

Equip operator space with the inner product $`\langle X,Y\rangle_2=\mathrm{Tr}X^\dagger Y`$. Hermiticity of the jumps implies

```math
\langle X,-\mathcal L_t(X)\rangle_2
=\frac12\sum_j\|[L_j(t),X]\|_2^2.
```

Thus $`K_t=-\mathcal L_t`$ is positive semidefinite and self-adjoint on Hilbert–Schmidt operator space. The action is the integrated norm of this actual generator. It is unchanged by a different jump representation of the same generator.

In particular, real identity shifts satisfy $`\mathcal D[L-cI]=\mathcal D[L]`$ for Hermitian $`L`$, where $`\mathcal D[L](X)=-[L,[L,X]]/2`$. To relate the action to a supplied list of jumps, diagonalize a single Hermitian $`L`$. On the matrix unit between eigenvalues $`\lambda_a`$ and $`\lambda_b`$, its dissipator has eigenvalue $`-(\lambda_a-\lambda_b)^2/2`$. Consequently,

```math
\frac12\|\mathcal D[L]\|_{2\to2}
=\frac{(\lambda_{\max}(L)-\lambda_{\min}(L))^2}{4}
=\min_{c\in\mathbb R}\|L-cI\|_\infty^2.
```

The triangle inequality therefore gives, for any supplied Hermitian-jump representation,

```math
A\le
\int_0^T\sum_j\min_{c_j\in\mathbb R}
\|L_j(t)-c_jI\|_\infty^2\,dt
\le
\int_0^T\sum_j\|L_j(t)\|_\infty^2\,dt.
```

Equality with a sum of jump costs is not assumed. A larger representation-dependent budget also satisfies the lower bound, but the generator action avoids charging arbitrary identity shifts or redundant representations. This norm budget does not measure the difficulty of synthesizing a chosen bath coupling or its target-dependent operator content.

An inert reference does not change the action. Indeed, Hilbert–Schmidt operator space factorizes as a Hilbert-space tensor product, and hence

```math
\|\mathcal L_t\otimes\mathrm{id}_R\|_{2\to2}
=\|\mathcal L_t\|_{2\to2}.
```

The same positive self-adjoint generator structure holds after this amplification. All trajectory estimates below therefore apply with the same $`A`$ to a state on $`SCR`$, for any finite reference $`R`$.

## Displacement requires purity loss

**Trajectory lemma.** For any initial density operator and any evolution in the model,

```math
\|\sigma_T-\sigma_0\|_2^2
\le A\left(\mathrm{Tr}\sigma_0^2-
\mathrm{Tr}\sigma_T^2\right).
```

**Proof.** Write $`P(t)=\mathrm{Tr}\sigma_t^2`$. The equation of motion and positivity of $`K_t`$ give

```math
-P'(t)=2\langle\sigma_t,K_t\sigma_t\rangle_2
=\sum_j\|[L_j(t),\sigma_t]\|_2^2\ge0.
```

The spectral inequality $`K_t^2\le\|K_t\|_{2\to2}K_t`$ then yields

```math
\|\dot\sigma_t\|_2^2
=\langle\sigma_t,K_t^2\sigma_t\rangle_2
\le\frac12\|\mathcal L_t\|_{2\to2}\,[-P'(t)].
```

Set $`a(t)=\|\mathcal L_t\|_{2\to2}/2`$. Absolute continuity, the triangle inequality, and Cauchy–Schwarz in time imply

```math
\begin{aligned}
\|\sigma_T-\sigma_0\|_2
&\le\int_0^T\|\dot\sigma_t\|_2\,dt\\
&\le\int_0^T\sqrt{a(t)}\sqrt{-P'(t)}\,dt\\
&\le\sqrt{\int_0^T a(t)\,dt}\,
\sqrt{\int_0^T[-P'(t)]\,dt}\\
&=\sqrt{A\,[P(0)-P(T)]}.
\end{aligned}
```

Squaring proves the lemma. No spectral-gap condition, adiabatic approximation, or restriction on the path of the state enters the argument.

## Finite-action return bound

**Theorem.** Every protocol in the model obeys

```math
(s-\varepsilon)_+^2\le A\varepsilon,
\qquad (x)_+=\max\{x,0\}.
```

More precisely, the same proof gives

```math
2(s-\varepsilon)_+^2\le A(2\varepsilon-\varepsilon^2).
```

In particular, the first inequality implies the explicit finite-action lower bound

```math
\varepsilon\ge
\frac{A+2s-\sqrt{A^2+4As}}{2}.
```

**Proof.** Choose a pure data-reference input $`|\psi\rangle_{SR}`$ attaining the diamond distance between $`\mathrm{Ad}_U`$ and the identity. Let the pure initial and desired final joint states be

```math
\sigma_0=|\psi\rangle\langle\psi|_{SR}\otimes|0\rangle\langle0|_C,
\qquad
\omega=(U\otimes I_R)|\psi\rangle\langle\psi|
(U^\dagger\otimes I_R)\otimes|0\rangle\langle0|_C.
```

Tensor factors can be placed in the fixed order $`SCR`$ throughout. Because both states are pure and their half-trace distance is $`s`$,

```math
\|\omega-\sigma_0\|_2=\sqrt2\,s.
```

Let $`\sigma_T`$ be the actual output for this input. The definition of the joint channel error gives $`\|\sigma_T-\omega\|_1/2\le\varepsilon`$. For any traceless Hermitian $`X`$, its positive and negative parts have the same trace, so

```math
\|X\|_2^2
=\mathrm{Tr}X_+^2+\mathrm{Tr}X_-^2
\le(\mathrm{Tr}X_+)^2+(\mathrm{Tr}X_-)^2
=\frac12\|X\|_1^2.
```

Applied to $`X=\sigma_T-\omega`$, this implies $`\|\sigma_T-\omega\|_2\le\sqrt2\,\varepsilon`$. The reverse triangle inequality therefore gives

```math
\|\sigma_T-\sigma_0\|_2\ge\sqrt2\,(s-\varepsilon)_+.
```

The final purity is also controlled by the same error. Measuring the rank-one projector $`\omega`$ yields

```math
p=\mathrm{Tr}(\omega\sigma_T)\ge1-\varepsilon.
```

Hilbert–Schmidt Cauchy–Schwarz and $`\mathrm{Tr}\omega^2=1`$ imply

```math
\mathrm{Tr}\sigma_T^2\ge p^2\ge(1-\varepsilon)^2.
```

The initial purity is one. Apply the trajectory lemma on the joint system including the inert reference to obtain

```math
2(s-\varepsilon)_+^2
\le\|\sigma_T-\sigma_0\|_2^2
\le A\left(1-\mathrm{Tr}\sigma_T^2\right)
\le A(2\varepsilon-\varepsilon^2).
```

Dropping the nonpositive term $`-A\varepsilon^2`$ and dividing by two proves the stated bound. For $`\varepsilon<s`$, solve the resulting quadratic inequality in $`\varepsilon`$. For $`\varepsilon\ge s`$, the displayed root is already no greater than $`s`$, so the same explicit lower bound holds. This includes $`A=0`$, when it reduces to $`\varepsilon\ge s`$. The proof also applies when $`\varepsilon\in[0,1]`$ is an upper bound on the actual joint channel error.

## Optimal inverse-accuracy order

Let $`A_{\min}(\varepsilon;U)`$ be the infimum of the action over all allowed protocols and all finite pure helpers achieving joint channel error at most $`\varepsilon`$. For $`0<\varepsilon<s`$, the theorem gives

```math
A_{\min}(\varepsilon;U)\ge\frac{(s-\varepsilon)^2}{\varepsilon}.
```

The [explicit one-qubit helper construction](pure-helper.md) gives

```math
A_{\min}(\varepsilon;U)\le\frac{\pi^2+\pi}{\varepsilon}.
```

Thus, for every fixed target with $`s(U)>0`$,

```math
A_{\min}(\varepsilon;U)=\Theta_U(\varepsilon^{-1})
\qquad\text{as }\varepsilon\downarrow0.
```

The order is optimal; these bounds do not identify the optimal coefficient. For a nontrivial target, zero joint error is impossible at finite action. The lower bound is uniform in helper dimension and in the control schedule, while the matching construction needs only a helper qubit.
