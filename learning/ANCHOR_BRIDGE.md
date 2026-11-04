# From unread measurements to the controller return law

Begin with the task of applying a phase flip to an unknown qubit using dephasing controls. A controller may help produce the gate, but its required final state changes the action needed for an accurate result. This bridge develops the measurement and open-system language behind that distinction, then supplies the steps that connect it to the repository's channel bounds and constructions.

The explanations are self-contained at the level needed to follow the scientific account. The [30-milestone map](MILESTONES.md) organizes the same material by understanding targets; the linked files in `science/` contain the canonical statements and complete proofs.

## The educational anchor

The single educational anchor is **Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control*, Cambridge University Press, first published 2010**, ISBN 978-0-521-80442-4. The [official publisher frontmatter](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf) verifies the publication information and the section map below.

Only that frontmatter and table of contents were inspected for this bridge. The section references are navigation pointers, not evidence that a particular textbook theorem or equation proves a project claim. The calculations below are supplied explicitly, with research-level statements linked to their project proofs.

| Anchor locations | Printed starting pages | Connection to this bridge |
|---|---|---|
| Sections 1.1–1.4 | 1, 8, 27, 32 | Probabilities, measurement outcomes, and general measurement maps. |
| Sections 3.6–3.10 | 119, 121, 124, 130, 136 | Lindblad dynamics, decoherence, and ensemble descriptions. |
| Sections 4.1–4.2 and 4.6 | 148, 149; 172 | Quantum trajectories and qubit geometry. |
| Appendix A.1–A.2 | 398, 404 | States, composite systems, and entanglement. |

These are printed book page numbers, not page indices in the linked PDF. The selected sections provide a route into the subject; the project does not require the entire book as a prerequisite. In particular, the channel-error convention, generator action, return arguments, and flag constructions are developed here rather than inferred from the contents page.

## A phase flip and an unread measurement

A qubit state is represented by a positive matrix of trace one. In the computational basis it has the form

```math
\rho=\begin{pmatrix}p&c\\c^*&1-p\end{pmatrix}.
```

The diagonal entries give the probabilities of the two basis outcomes. The off-diagonal entry $`c`$ records coherence between them. A phase flip is the unitary

```math
Z=|0\rangle\langle0|-|1\rangle\langle1|,
\qquad
Z\rho Z=\begin{pmatrix}p&-c\\-c^*&1-p\end{pmatrix}.
```

It preserves the basis probabilities and reverses the sign of the coherence. An unread projective measurement in the same basis has a different effect. With $`P_b=|b\rangle\langle b|`$,

```math
\mathcal P_Z(\rho)=P_0\rho P_0+P_1\rho P_1
=\begin{pmatrix}p&0\\0&1-p\end{pmatrix}.
```

Summing over the unobserved outcomes removes the coherence. The distinction is visible on $`|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2`$: the phase gate sends $`|+\rangle`$ to $`|-\rangle`$, whereas the unread measurement sends its density matrix to $`I/2`$. Measuring $`X`$ after the operation gives the outcome $`-1`$ with probability one for the ideal gate and probability one-half after the unread measurement.

This example identifies a specific input and an observable that reveal an error. A gate guarantee must cover every input. Even a perfect transfer of $`|+\rangle`$ to $`|-\rangle`$ does not identify the implemented gate: the Pauli operators $`Y`$ and $`Z`$ both accomplish that transfer up to an irrelevant phase, but they act differently on $`|0\rangle`$. The next step is therefore to compare operations, not only selected output states.

## States channels and reference systems

A quantum channel is a linear, completely positive, trace-preserving map. Trace preservation keeps total probability equal to one. Complete positivity ensures that applying the map to one part of a larger system still produces a valid joint state.

The data system is $`S`$. A controller $`C`$ starts in a supplied state $`\beta_C`$, independently of the input. A reference $`R`$ represents another system with which the data may already be entangled. The reference is not a controller resource and is never driven. Thus the allowed initial states have the form

```math
\rho_{SR}\otimes\beta_C.
```

If $`\Phi_T`$ is the joint evolution on $`SC`$, the reduced data channel is

```math
\mathcal E(\rho_S)
=\mathrm{Tr}_C\Phi_T(\rho_S\otimes\beta_C).
```

The partial trace removes the controller from the reported output. It does not remove correlations between the data and $`R`$ from the error criterion.

For two states, their trace distance is

```math
D(\rho,\omega)=\frac12\|\rho-\omega\|_1,
\qquad
\|X\|_1=\mathrm{Tr}\sqrt{X^\dagger X}.
```

This distance equals the largest difference in the probability of a measurement event. To compare two channels $`\mathcal E`$ and $`\mathcal Q`$, first set $`\Delta=\mathcal E-\mathcal Q`$. Their half-diamond distance is

```math
\begin{aligned}
d_\diamond(\mathcal E,\mathcal Q)
&=\frac12\|\mathcal E-\mathcal Q\|_\diamond\\
&=\max_{\rho_{SR}}\frac12
  \| (\Delta\otimes\mathrm{id}_R)(\rho_{SR})\|_1.
\end{aligned}
```

A reference of dimension $`\dim S`$ suffices, and the maximum can be taken over pure joint inputs. The reference makes the criterion suitable for using a gate inside a larger quantum computation, where its input may carry entanglement. Throughout the project, “complete-channel error” means this reference-inclusive criterion.

The output space also matters. A data-only channel is scored after tracing out $`C`$. Approximate joint return of a pure controller instead compares the channel to

```math
\mathcal T_U(\rho)
=U\rho U^\dagger\otimes|0\rangle\langle0|_C.
```

This single comparison controls the gate, the returned controller, and their residual correlations. Exact return of a mixed controller marginal is a different requirement, developed below.

A normalized Choi state is the output obtained by applying a channel to one half of a maximally entangled state. It encodes the channel as a linear map, which makes it useful for verification. Its trace distance is nevertheless one particular input's distinguishability, not automatically the diamond supremum. The [verification guide](../verification/README.md) separates this diagnostic from the analytical complete-channel guarantees.

## From measurement updates to Hermitian generators

For a measurement described by resolved outcome operators $`M_r`$,

```math
\sum_r M_r^\dagger M_r=I,
\qquad
p_r=\mathrm{Tr}(M_r\rho M_r^\dagger).
```

When outcome $`r`$ is recorded and has nonzero probability, the conditional state is $`M_r\rho M_r^\dagger/p_r`$. When the outcome is unread, the state is the probability-weighted average

```math
\rho\longmapsto\sum_r M_r\rho M_r^\dagger.
```

This distinction connects the measurement description to an unconditional master equation. For a Hermitian operator $`L`$, consider a short interval $`dt`$ with

```math
M_0=\sqrt{I-dt\,L^2},
\qquad M_1=\sqrt{dt}\,L.
```

For sufficiently small $`dt`$, the square root exists and these operators satisfy the completeness relation exactly. Expanding their unread update to first order gives

```math
\begin{aligned}
\rho(t+dt)
&=\rho(t)+dt\,\mathcal D[L](\rho(t))+O(dt^2),\\
\mathcal D[L](X)
&=LXL-\frac12\{L^2,X\}\\
&=-\frac12[L,[L,X]].
\end{aligned}
```

The braces denote an anticommutator and the brackets a commutator. Combining several such generators and allowing their operators to change according to a prescribed schedule gives the project's model,

```math
\dot\sigma_t=\mathcal L_t(\sigma_t),
\qquad
\mathcal L_t=-\frac12\sum_j[L_j(t),[L_j(t),\,\cdot\,]],
\qquad L_j(t)=L_j(t)^\dagger.
```

Here $`\sigma_t`$ includes the controller. The laboratory Hamiltonian is zero. All outcomes are averaged over, the schedule is fixed before the unknown input is supplied, and the terminal time is predetermined. All controller degrees of freedom are present initially; the protocol includes no reset, fresh helper injection, or free coherent decoder.

For a fixed $`L=\sqrt\gamma Z`$, the populations are constant and the coherence solves $`\dot c=-2\gamma c`$. The complete channel is

```math
\begin{aligned}
\mathcal E_t
&=q_t\,\mathrm{id}+(1-q_t)\mathrm{Ad}_Z,\\
q_t&=\frac{1+e^{-2\gamma t}}2,
\qquad \mathrm{Ad}_Z(\rho)=Z\rho Z.
\end{aligned}
```

Its half-diamond error from the desired $`Z`$ gate is $`q_t\ge1/2`$. Stronger static dephasing approaches the unread projective measurement; it does not turn that measurement into an accurate phase gate. The constructions later in the bridge change the joint dephasing operator and use controller subspaces to carry the gate.

The short-time operators above also describe one possible monitored jump record. For $`L=\sqrt\gamma Z`$, the jump rate is $`\gamma`$ independently of the input. Observing the first jump and stopping would apply $`Z`$ exactly, with mean waiting time $`1/\gamma`$. That procedure uses a record and a random terminal time. The project concerns the unconditional channel at a fixed terminal time. A master equation describes the average evolution; choosing a detector record or using it for feedback adds information and control that the average equation alone does not provide.

## Notation and the generator action

The following notation separates a measurement update, an instantaneous generator, and a completed operation. It is the convention used in this repository, not an asserted transcription of the textbook's notation.

| Object | Project notation | Meaning |
|---|---|---|
| Data input | $`\rho_S`$ | An arbitrary state, possibly correlated with a reference. |
| Initial controller | $`\beta_C`$ | A supplied state independent of the input and reference. |
| Joint state | $`\sigma_t`$ | The state on data and controller during the evolution. |
| Outcome operator | $`M_r`$ | A single measurement update before averaging outcomes. |
| Jump operator | $`L_j(t)`$ | A rate-scaled operator in the master equation. |
| Generator | $`\mathcal L_t`$ | The linear map determining the instantaneous derivative. |
| Joint propagator | $`\Phi_T`$ | The channel obtained by integrating the generator. |
| Target channel | $`\mathcal U=\mathrm{Ad}_U`$ | The desired unitary action on the data. |

A rate may be written outside a dissipator as $`\gamma\mathcal D[c]`$. Here it is absorbed into $`L=\sqrt\gamma\,c`$, so $`\mathcal D[L]=\gamma\mathcal D[c]`$. This square root is necessary when translating a physical decay rate into the action convention.

The proof uses the Hilbert–Schmidt norm $`\|X\|_2^2=\mathrm{Tr}(X^\dagger X)`$. The norm of a generator is induced by that operator norm:

```math
\|\mathcal L_t\|_{2\to2}
=\sup_{X\ne0}\frac{\|\mathcal L_t(X)\|_2}{\|X\|_2},
\qquad
A=\frac12\int_0^T\|\mathcal L_t\|_{2\to2}\,dt.
```

In an orthonormal operator basis, this is the largest singular value of the generator matrix. It is not the Frobenius norm of that matrix. The Frobenius norm takes the square root of the sum of the squared entry magnitudes. Trace and diamond distances score the physical error; Hilbert–Schmidt geometry supplies the proof; $`\|L\|_\infty`$, the largest singular value of a jump, measures its operator amplitude. These are distinct norms with distinct roles.

The factor one-half in $`A`$ can be checked directly. If $`L|a\rangle=\lambda_a|a\rangle`$, then

```math
\mathcal D[L](|a\rangle\langle b|)
=-\frac12(\lambda_a-\lambda_b)^2|a\rangle\langle b|.
```

Hence

```math
\frac12\|\mathcal D[L]\|_{2\to2}
=\frac{(\lambda_{\max}-\lambda_{\min})^2}{4}.
```

For $`L=\sqrt\gamma Z`$, the eigenvalue separation is $`2\sqrt\gamma`$, so a duration $`T`$ costs exactly $`A=\gamma T`$. Every construction in this project has the same single-stage normalization, with possible additional zero eigenvalues on unused controller levels.

The action is defined from the generator itself. Real identity shifts of a Hermitian jump leave its dissipator unchanged, and a different jump representation of the same generator leaves $`A`$ unchanged. For an arbitrary supplied list,

```math
A\le\int_0^T\sum_j\|L_j(t)\|_\infty^2\,dt.
```

The two budgets coincide for the explicit single-jump stages, but need not coincide for general generators. The action is dimensionless and does not include the cost of synthesizing the target-dependent coupling or addressing a chosen controller level.

An inert reference preserves this norm exactly:

```math
\|\mathcal L_t\otimes\mathrm{id}_R\|_{2\to2}
=\|\mathcal L_t\|_{2\to2}.
```

Hilbert–Schmidt operator space is a Hilbert-space tensor product, and the identity map on the reference factor has induced norm one. This is why the same action can enter a proof on data entangled with a reference.

## Displacement and purity loss

Purity is $`P(t)=\mathrm{Tr}\sigma_t^2`$. A density operator has purity one exactly when it is pure. Hermitian-jump evolution obeys

```math
-P'(t)=\sum_j\|[L_j(t),\sigma_t]\|_2^2\ge0.
```

The commutators quantify the parts of the state that the current dephasing directions change. If every commutator vanishes, the instantaneous state derivative also vanishes. More generally, moving the state and losing purity are linked quantitatively.

Let $`K_t=-\mathcal L_t`$. For every operator $`X`$,

```math
\langle X,K_tX\rangle_2
=\frac12\sum_j\|[L_j(t),X]\|_2^2,
\qquad
\langle X,Y\rangle_2=\mathrm{Tr}(X^\dagger Y).
```

Thus $`K_t`$ is positive and self-adjoint on operator space. Its eigenvalues lie between zero and $`\|K_t\|_{2\to2}`$, so $`K_t^2\le\|K_t\|_{2\to2}K_t`$. Applied to the moving state, this gives

```math
\begin{aligned}
\|\dot\sigma_t\|_2^2
&=\langle\sigma_t,K_t^2\sigma_t\rangle_2\\
&\le\frac12\|\mathcal L_t\|_{2\to2}\,[-P'(t)].
\end{aligned}
```

Integrating the speed and using Cauchy–Schwarz in time yields the trajectory inequality

```math
\begin{aligned}
\|\sigma_T-\sigma_0\|_2
&\le\int_0^T\|\dot\sigma_t\|_2\,dt\\
&\le\sqrt{A\,[P(0)-P(T)]}.
\end{aligned}
```

This is the mathematical step that turns a rate convention into an endpoint constraint. It covers arbitrary time dependence and does not assume a slowly moving dephasing basis. A physically supplied Hamiltonian could move a pure state without changing its purity, which is why the zero-Hamiltonian restriction is part of the theorem. The complete argument is in the [trajectory lemma](../science/return-law.md#displacement-requires-purity-loss).

## Approximate pure joint return

Suppose the controller starts in $`|0\rangle`$ and the final joint channel is within half-diamond error $`\epsilon`$ of $`\mathcal T_U`$. Define the target's displacement from the identity channel by

```math
s(U)=\frac12\|\mathrm{Ad}_U-\mathrm{id}\|_\diamond.
```

For this particular comparison, a pure input without a reference can attain $`s(U)`$. A reference-assisted pure input has overlap $`\mathrm{Tr}(\eta U)`$ with its image. In an eigenbasis of $`U`$, that overlap is a convex combination of its eigenvalues, and the same combination is realized by a pure superposition with those eigenbasis probabilities. This simplification is specific to a unitary compared with the identity; generic channel-error distances still require the reference-inclusive definition.

Choose an input attaining $`s(U)`$. Its initial joint state $`\sigma_0`$ and the desired output $`\omega`$ are both pure, with

```math
\|\omega-\sigma_0\|_2=\sqrt2\,s(U).
```

The actual output has $`D(\sigma_T,\omega)\le\epsilon`$. For a traceless Hermitian operator, $`\|X\|_2\le\|X\|_1/\sqrt2`$, since its positive and negative eigenvalues have equal total magnitude. The triangle inequality therefore gives

```math
\|\sigma_T-\sigma_0\|_2
\ge\sqrt2\,(s(U)-\epsilon)_+.
```

Closeness to the pure target also limits the available purity loss. Measuring the projector $`\omega`$ gives $`\mathrm{Tr}(\omega\sigma_T)\ge1-\epsilon`$, so

```math
P(T)\ge(1-\epsilon)^2,
\qquad P(0)-P(T)\le2\epsilon-\epsilon^2.
```

Combining the displacement and purity estimates with the trajectory inequality proves

```math
2(s(U)-\epsilon)_+^2
\le A(2\epsilon-\epsilon^2),
```

and in particular

```math
\boxed{(s(U)-\epsilon)_+^2\le A\epsilon.}
```

For $`0\lt \epsilon\lt s(U)`$, the required action is at least $`(s(U)-\epsilon)^2/\epsilon`$. The bound is uniform in controller dimension and control path.

For the concrete $`Z`$ gate, $`|+\rangle`$ and $`Z|+\rangle=|-\rangle`$ are orthogonal, so $`s(Z)=1`$. Joint error at most $`0.01`$ therefore requires $`A\ge98.01`$. This is a lower bound over all allowed pure-controller protocols, not an estimate for a particular trajectory. The [return-law proof](../science/return-law.md#finite-action-return-bound) gives the exact assumptions and finite-action forms.

## A two-stage helper construction

The matching upper bound uses one helper qubit and a moving joint dephasing operator. Define

```math
B_U=U\otimes|1\rangle\langle0|
    +U^\dagger\otimes|0\rangle\langle1|,
```

```math
R_U(\theta)=\cos(2\theta)I_S\otimes Z_C
           +\sin(2\theta)B_U.
```

The operators $`I_S\otimes Z_C`$ and $`B_U`$ anticommute and each squares to the identity, so $`R_U(\theta)`$ is a Hermitian reflection. A jump $`\sqrt\gamma R_U(\theta)`$ has action rate $`\gamma`$. In the $`Z`$ example this becomes the explicit two-qubit operator

```math
R_Z(\theta)=\cos(2\theta)I_S\otimes Z_C
           +\sin(2\theta)Z_S\otimes X_C.
```

To understand the operation for an arbitrary input, define

```math
W_U=I_S\otimes|0\rangle\langle0|
    +U\otimes|1\rangle\langle1|.
```

Conjugating the generator by this constant operator turns it into a dephasing generator acting only on the helper. Since $`W_U`$ fixes the helper-zero input subspace, the exact first-stage output is

```math
\rho\longmapsto W_U(\rho\otimes\tau_a)W_U^\dagger,
```

where $`a=\gamma T`$ is the stage action. The identity remains true when $`\rho`$ is entangled with a reference. The supplied coupling contains $`U`$; $`W_U`$ is used only to solve the equation and is not physically applied as a gate.

Choose the uniform schedule $`\theta(u)=\pi u/2`$ in normalized time $`u=t/T\in[0,1]`$. The dephasing axis then rotates through angle $`\pi`$, and the helper's rotating Bloch coordinates obey

```math
x'=-2ax-\pi z,
\qquad z'=\pi x,
\qquad (x(0),z(0))=(0,1).
```

An integrating factor gives $`|x(u)|\le\pi/(2a)`$, and integrating $`z'`$ gives $`|1-z(1)|\le\pi^2/(2a)`$. Since the frame has rotated by $`\pi`$, the desired physical helper output is $`|1\rangle`$. Its trace-distance error satisfies

```math
\delta_a
=\frac12\|\tau_a-|1\rangle\langle1|\|_1
\le\frac{\pi^2+\pi}{4a}.
```

The factorized expression with $`W_U`$ makes $`\delta_a`$ the exact first-stage complete-channel error, including references. The ideal intermediate output is $`U\rho U^\dagger\otimes|1\rangle\langle1|`$.

A second stage uses the same helper rotation with $`U=I_S`$. Its unital channel transfers the helper from $`|1\rangle`$ back toward $`|0\rangle`$ with the same error bound. Channel contractivity propagates the first-stage error through the second stage, including any actual intermediate correlations. The two stage actions add to $`A=2a`$, giving

```math
\epsilon\le\min\left\{1,\frac{\pi^2+\pi}{A}\right\}.
```

Together with the lower bound, this proves $`A_{\min}(\epsilon;U)=\Theta_U(\epsilon^{-1})`$ for every fixed nontrivial target. The return is approximate and joint. The [construction proof](../science/pure-helper.md) supplies the exact laboratory schedule and the channel-composition argument.

## Exact mixed marginal return

Now let the controller start in an arbitrary mixed state $`\beta`$, and require its final marginal to equal $`\beta`$ exactly. Data-controller correlations are allowed. The target joint output is no longer required to be a pure state, so the preceding endpoint-purity argument cannot simply be reused. Purifying $`\beta`$ would add a return requirement for a preparation reference that this task does not impose.

The project supplies a different starting point. Consider only the maximally mixed data input,

```math
\tau=\frac{I_S}{d}\otimes\beta,
\qquad \omega_t=\Phi_t(\tau).
```

Exact controller return on this input makes the cross term vanish in the identity

```math
\mathrm{Tr}\omega_T^2
=\frac{\mathrm{Tr}\beta^2}{d}
 +\|\omega_T-\tau\|_2^2.
```

The first term is the initial purity. Purity cannot increase, so the second term must be zero. Moreover, the integrated sum of commutator squares must vanish. The entire trajectory is stationary and every jump obeys

```math
[L_j(t),I_S\otimes\beta]=0
\quad\text{almost everywhere}.
```

Thus an endpoint marginal requirement has restricted the whole allowed trajectory. This conclusion needs exact return; an arbitrary approximate mixed-return promise does not imply these commutators vanish.

On the support of $`\beta`$, introduce the weighted norm

```math
\|X\|_\beta^2
=\mathrm{Tr}\left[
 X^\dagger(I_S\otimes\beta^{-1})X\right].
```

Commutation with $`\beta`$ makes its support invariant. If $`\beta`$ has zero eigenvalues, all operators are first restricted to that support. The map $`X\mapsto(I_S\otimes\beta^{-1/2})X`$ is an isometry to ordinary Hilbert–Schmidt space and commutes with the generator. The same speed–purity proof therefore holds with the same action:

```math
\|\sigma_T-\sigma_0\|_\beta^2
\le A\,[P_\beta(0)-P_\beta(T)],
\qquad P_\beta(t)=\|\sigma_t\|_\beta^2.
```

This weighting normalizes the initial purity of a pure data state:

```math
\|\rho\otimes\beta\|_\beta^2=1
\quad\text{when }\rho\text{ is pure}.
```

It also makes $`X\mapsto\mathrm{Tr}_C(X)\otimes\beta`$ an orthogonal projection. Consequently,

```math
\|\mathrm{Tr}_C X\|_2\le\|X\|_\beta,
\qquad
P_\beta(T)\ge\mathrm{Tr}[\mathcal E(\rho)^2].
```

If the data output is within error $`\epsilon`$ of the pure state $`U\rho U^\dagger`$, the final expression is at least $`(1-\epsilon)^2`$. The earlier displacement argument now applies to the data in this weighted calculation and gives the same law,

```math
(s(U)-\epsilon)_+^2\le A\epsilon.
```

For a pure initial controller, the invariant support is $`S\otimes|0\rangle`$ throughout. Exact pure return therefore excludes the helper excursions used in the two-stage construction, whose guarantee is approximate joint return.

No controller dimension or smallest positive eigenvalue appears in the bound. The [weighted proof](../science/mixed-controllers.md) explains the support restriction and projection in full detail.

If $`\beta=I_C/D_C`$, the particular input $`\tau`$ is globally maximally mixed and is stationary automatically under every unital generator. The lower bound therefore applies even if the controller is discarded. This uses only the maximally mixed data input; unitality alone does not keep the controller marginal fixed for every other data input.

The explicit mixed-controller $`Z`$ construction has the stronger property that its controller stays in $`I_C/2`$ for every input. Its separate block calculation gives $`\epsilon\le\pi^2/(4A)`$, with correlations permitted. Thus the inverse-action order is attained for $`Z`$ under exact mixed marginal return. An all-target upper bound under that exact-return promise is not established here.

## Consumed flags

A controller allowed to change can store the part of an unconditioned evolution on which the gate has already been completed. Let its levels be $`0,1,\ldots,m`$, initially in level zero, and write $`P_j=|j\rangle\langle j|`$ for their projectors. Stage $`j`$ uses the fixed Hermitian jump

```math
L_j=\sqrt\gamma\left(
 U\otimes|j\rangle\langle0|
 +U^\dagger\otimes|0\rangle\langle j|
 \right)
```

for action $`a=\gamma T`$. On its active pair the failure and success probabilities obey a symmetric exchange equation,

```math
\dot p_0=\gamma(p_j-p_0),
\qquad \dot p_j=\gamma(p_0-p_j),
\qquad(p_0(0),p_j(0))=(1,0).
```

The failure probability after one stage is

```math
q_{\rm ex}(a)=\frac{1+e^{-2a}}2.
```

Earlier success levels are dark for subsequent jumps: neither the jump nor its square acts on them. Therefore failure probabilities multiply while completed branches remain unchanged. Writing $`q=q_{\rm ex}(a)`$, the exact joint channel is

```math
\begin{aligned}
\mathcal F_m(\rho)
={}&q^m\rho\otimes P_0\\
&+U\rho U^\dagger\otimes
  \sum_{j=1}^m(1-q)q^{j-1}P_j.
\end{aligned}
```

This is an operator identity for arbitrary inputs and references. After tracing the controller,

```math
\mathcal E_m=q^m\,\mathrm{id}+(1-q^m)\mathrm{Ad}_U,
\qquad
\epsilon_m=s(U)q^m,
\qquad A=ma.
```

The sum includes every branch. No completion flag is read and no outcome is selected. At fixed $`a\gt 0`$, increasing $`m`$ gives achievable action $`O_U(\log(1/\epsilon))`$ with controller dimension $`m+1=O_U(\log(1/\epsilon))`$. This is an upper bound, not an unrestricted optimum over all consumed-controller protocols.

A small complete $`Z`$ example makes the bookkeeping explicit. Take two stages, each with $`a=(\ln3)/2`$, so $`q=2/3`$. The controller is a qutrit, the total action is $`A=\ln3`$, and

```math
\mathcal F_2(\rho)
=\frac49\rho\otimes P_0
 +Z\rho Z\otimes\left(\frac13P_1+\frac29P_2\right).
```

On input $`|+\rangle`$, an $`X`$ measurement of the data yields $`-1`$ with probability $`5/9`$. The ideal probability is one, and the exact channel error is $`4/9`$. The formula gives the same error for the complete channel because $`s(Z)=1`$, not because one measurement alone generally determines a diamond distance.

The final controller marginal is the input-independent state

```math
\beta_m=q^mP_0+\sum_{j=1}^m(1-q)q^{j-1}P_j.
```

Comparing the full output with $`U\rho U^\dagger\otimes\beta_m`$ leaves only the failure block. Its joint half-diamond error is also $`s(U)q^m`$. This is accuracy relative to a specified **changed** controller state. Its distance from the supplied state is

```math
D(\beta_m,P_0)=1-q^m.
```

The controller entropy can stay bounded as $`m`$ grows. In bits, with binary entropy $`h_2`$,

```math
S_2(\beta_m)
=\frac{1-q^m}{1-q}h_2(q)
\le\frac{h_2(q)}{1-q}.
```

A bounded entropy increase therefore does not imply a small return defect. The growing level structure and its initial pure state are supplied resources. Encoding the levels into fewer qubits does not make their selective transitions local automatically. The [consumed-controller proof](../science/consumed-controllers.md) gives the exact action, joint error, entropy, and resource accounting.

## Fixed controller dimension

A fixed qutrit can already improve the error power when return is removed. The change is to use a rotating transfer on each active pair, with

```math
Z_j=I_S\otimes(P_0-P_j),
\qquad
B_j=U\otimes|j\rangle\langle0|
   +U^\dagger\otimes|0\rangle\langle j|,
```

```math
L_j(u)=\sqrt{\gamma_j}
 [\cos(\pi u)Z_j+\sin(\pi u)B_j],
\qquad 0\le u\le1.
```

The one-stage Bloch equation is the equation already used for the helper rotation, now scored only by its failure population. To distinguish it from the fixed exchange above, write

```math
q_{\rm rot}(a)=\frac{1-z_a(1)}2.
```

The finite-action bound and its asymptotic form are

```math
0\le q_{\rm rot}(a)\le\min\left\{1,\frac{\pi^2}{4a}\right\},
\qquad
q_{\rm rot}(a)=\frac{\pi^2}{4a}+O(a^{-2}).
```

The scientific notes use $`q`$ within each separate construction; the subscripts here distinguish their two different failure functions.

A rotating stage creates coherence between its failure and success flags. These coherences must be retained in the joint state. Their effect on subsequent stages is controlled by the operator block structure. On the active pair, $`L_j^2=\gamma_j I`$; on all old success levels the jump is zero. An operator block $`Y`$ connecting an active and an inactive subspace obeys

```math
\dot Y=-\frac{\gamma_j}{2}Y.
```

It decays without feeding the active diagonal blocks. The old success populations remain fixed, and the current failure population can again be transferred independently. For stage actions $`a_1,\ldots,a_m`$,

```math
Q_m=\prod_{j=1}^m q_{\rm rot}(a_j),
\qquad
\mathcal E_m=Q_m\,\mathrm{id}+(1-Q_m)\mathrm{Ad}_U,
\qquad A=\sum_j a_j.
```

Equal allocation $`a_j=A/m`$ gives error $`s(U)q_{\rm rot}(A/m)^m=O_U(A^{-m})`$ at fixed $`m`$. In particular, for a qutrit and the $`Z`$ gate,

```math
\epsilon_2=q_{\rm rot}(A/2)^2
=\frac{\pi^4}{4A^2}+O(A^{-3}).
```

This is a complete **data-channel** guarantee. The controller marginal can have input-dependent off-diagonal entries, so its diagonal probabilities alone are not its density matrix. The [full joint formula](../science/fixed-dimension-controllers.md#cross-flag-autonomy-and-the-complete-channel) records those coherences explicitly.

At fixed $`m`$, pinching the final controller in the flag basis gives an entropy upper bound of order $`(\log A)/A`$. Its entropy can therefore approach zero, even while its distance from the initial level-zero state approaches one. The faster data error does not satisfy the pure joint-return criterion. These are attainable powers, with no claim that the exponent $`m`$ is optimal or that exponential accuracy at fixed controller dimension is impossible.

## What the project adds

The anchor's verified section map locates the measurement, open-system, trajectory, and composite-system foundations. The project supplies the following additional steps explicitly.

| Foundation being connected | Additional step supplied here | Canonical account |
|---|---|---|
| States and measurement probabilities | Unknown-input channel error with an arbitrary inert reference; a distinct joint output space when return is required. | [Model and error convention](../science/return-law.md#model-and-error-convention) |
| Lindblad generators and decay rates | A representation-independent generator action, including its factor one-half and reference stability. | [Action accounting](../science/return-law.md#generator-action-and-representation-accounting) |
| Dephasing and purity decrease | A finite-action displacement inequality and its conversion into an inverse-error return bound. | [Return theorem](../science/return-law.md#finite-action-return-bound) |
| Qubit motion under a changing dephaser | An operator identity valid on every data input, followed by a second stage that returns the helper approximately. | [Pure helper construction](../science/pure-helper.md) |
| Multipartite states and local marginals | Stationarity forced by exact mixed return, invariant support, and a weighted projection proof. | [Mixed controller theorem](../science/mixed-controllers.md) |
| Unobserved branch averages | Protected completion flags, exact channel mixtures, and separate fixed-dimension and growing-dimension rates. | [Consumed flags](../science/consumed-controllers.md) and [fixed dimension](../science/fixed-dimension-controllers.md) |

The difficult universal step is the converse over every allowed schedule and controller dimension. An explicit trajectory or a few successful input states would not establish it. Conversely, the constructions need complete operator identities to show that their error estimates survive arbitrary inputs and references.

Research attribution and comparisons with earlier Zeno control, speed bounds, catalytic structure, and dissipative flags are recorded in [Related work](../references/RELATED_WORK.md). They are separate from the textbook navigation above. The [verification scripts](../verification/README.md) check the explicit formulas on finite cases; the scientific proofs carry the universal statements. The [milestone map](MILESTONES.md) connects these foundations and results into one project-defined reading route.
