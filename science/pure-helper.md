# A complete-channel construction with one helper qubit

For every unitary $`U`$ on a finite-dimensional data system and every action $`A\gt 0`$, a deterministic two-stage Hermitian-jump protocol with one initially pure helper qubit achieves

```math
\frac12\|\mathcal N_A-\mathcal T_U\|_\diamond
\le\min\left\{1,\frac{\pi^2+\pi}{A}\right\},
\qquad
\mathcal T_U(\rho)=U\rho U^\dagger\otimes|0\rangle\langle0|_C.
```

The error concerns the complete data-plus-helper output and holds for inputs entangled with an arbitrary inert reference. Combined with the [return-law converse](return-law.md), it establishes the inverse-accuracy action order for every fixed nontrivial target.

The laboratory evolution has zero Hamiltonian, unobserved bath outcomes, and a predetermined terminal time. The helper starts independently in $`|0\rangle`$. No measurement record is used, and the helper undergoes no reset or coherent endpoint decoding. The supplied controls are the target-dependent Hermitian jumps displayed below. Their generator norm is the charged resource; synthesizing those operators is a separate implementation requirement.

## A family of Hermitian reflections

Write $`X,Y,Z`$ for the helper Pauli operators and $`P_b=|b\rangle\langle b|`$ for $`b=0,1`$. Define

```math
B_U=U\otimes|1\rangle\langle0|
+U^\dagger\otimes|0\rangle\langle1|,
\qquad
R_U(\theta)=\cos(2\theta)I_S\otimes Z+\sin(2\theta)B_U.
```

The operator $`B_U`$ is Hermitian, satisfies $`B_U^2=I_{SC}`$, and anticommutes with $`I_S\otimes Z`$. Consequently,

```math
R_U(\theta)^\dagger=R_U(\theta),
\qquad R_U(\theta)^2=I_{SC}.
```

Both eigenvalues $`+1`$ and $`-1`$ occur, each with multiplicity $`\dim S`$. The rate-one dissipator is therefore

```math
\mathcal D[R_U(\theta)](Q)
=R_U(\theta)QR_U(\theta)-Q,
\qquad
\|\mathcal D[R_U(\theta)]\|_{2\to2}=2.
```

The last equality follows either from the single-jump spectral formula in the return law or from the decomposition of $`Q`$ into blocks between the two eigenspaces. The dissipator has eigenvalue zero on equal-sign blocks and eigenvalue $`-2`$ on opposite-sign blocks. We normalize the jump rate to one, fixing the time unit. A stage of duration $`T`$ then has action exactly $`T`$.

For the solution, introduce the constant unitary

```math
W_U=I_S\otimes P_0+U\otimes P_1
```

and the helper reflection

```math
r(\theta)=\cos(2\theta)Z+\sin(2\theta)X.
```

Direct multiplication gives

```math
R_U(\theta)=W_U[I_S\otimes r(\theta)]W_U^\dagger.
```

This identity is a change of coordinates used in the proof. The physical protocol applies only the dissipators $`\mathcal D[R_U(\theta)]`$; it does not apply $`W_U`$ as a coherent gate. Moreover, $`W_U`$ acts as the identity on the initial helper-zero subspace.

## Stage one: carry the data unitary into the helper-one subspace

Fix a stage duration $`T\gt 0`$ and set

```math
\theta(t)=\frac{\pi t}{2T},\qquad 0\le t\le T.
```

During stage one, use the single jump $`R_U(\theta(t))`$. Let $`\mathcal E_T`$ be the channel on a helper qubit generated over the same interval by $`\mathcal D[r(\theta(t))]`$, and write

```math
\tau_t=\mathcal E_{t,0}(P_0),
\qquad
\dot\tau_t=r(\theta(t))\tau_t r(\theta(t))-\tau_t,
\qquad \tau_0=P_0.
```

Covariance of the dissipator under the constant conjugation $`W_U`$ gives the exact first-stage channel

```math
\Phi_{1,T}(\rho)=W_U(\rho\otimes\tau_T)W_U^\dagger.
```

To verify it, conjugate the joint equation by $`W_U^\dagger`$. The generator then acts only on the helper, and the initial state remains $`\rho\otimes P_0`$. Uniqueness of the linear evolution gives the displayed expression. The calculation is unchanged when $`\rho`$ includes an inert reference entangled with the data.

The desired intermediate channel is

```math
\mathcal J_1(\rho)
=U\rho U^\dagger\otimes P_1
=W_U(\rho\otimes P_1)W_U^\dagger.
```

Unitary invariance of the trace norm and its multiplicativity on tensor products imply

```math
\frac12\|\Phi_{1,T}-\mathcal J_1\|_\diamond
=\frac12\|\tau_T-P_1\|_1
=: \delta_T.
```

For example, on any data-reference density operator, conjugation by $`W_U`$ leaves the norm of the output difference equal to $`\|\rho_{SR}\otimes(\tau_T-P_1)\|_1=\|\tau_T-P_1\|_1`$. Thus the reduction to a single-qubit error is exact at the complete-channel level.

## A finite-time bound on the rotating dephasing equation

The following estimate holds for every $`T\gt 0`$, without an adiabatic expansion. Let

```math
V(t)=e^{-i\theta(t)Y},
\qquad
r(\theta(t))=V(t)ZV(t)^\dagger,
\qquad
\widetilde\tau_t=V(t)^\dagger\tau_tV(t).
```

Differentiating gives the rotating-coordinate equation

```math
\dot{\widetilde\tau}_t
=Z\widetilde\tau_tZ-\widetilde\tau_t
+i\dot\theta(t)[Y,\widetilde\tau_t].
```

The commutator in this equation comes from differentiating the coordinate change. The laboratory generator remains the Hermitian-jump dissipator specified above.

Write

```math
\widetilde\tau_t=\frac12[I+x(t)X+y(t)Y+z(t)Z],
\qquad \omega=\frac{\pi}{T}.
```

The Bloch equations and their initial conditions are

```math
\dot x=-2x-\omega z,
\qquad
\dot y=-2y,
\qquad
\dot z=\omega x,
\qquad
(x(0),y(0),z(0))=(0,0,1).
```

Hence $`y(t)=0`$. Since $`\widetilde\tau_t`$ is a density operator, its Bloch vector lies in the unit ball, in particular $`|z(t)|\le1`$. Integrating the first equation gives

```math
x(t)=-\omega\int_0^t e^{-2(t-u)}z(u)\,du,
\qquad
|x(t)|\le\frac{\omega}{2}(1-e^{-2t})\le\frac{\omega}{2}.
```

Integrating the third equation then yields

```math
|1-z(T)|
=\left|\omega\int_0^T x(t)\,dt\right|
\le\frac{\omega^2T}{2}.
```

At the endpoint, $`V(T)P_0V(T)^\dagger=P_1`$. The half-trace distance between qubit states is half the Euclidean distance between their Bloch vectors. Therefore,

```math
\begin{aligned}
\delta_T
&=\frac12\|\widetilde\tau_T-P_0\|_1\\
&=\frac12\sqrt{x(T)^2+[1-z(T)]^2}\\
&\le\frac12\bigl(|x(T)|+|1-z(T)|\bigr)\\
&\le\frac{\omega+\omega^2T}{4}
=\frac{\pi^2+\pi}{4T}.
\end{aligned}
```

The estimate is a direct finite-time bound. Its coefficient is sufficient for the action-order statement; no optimal-coefficient claim is needed.

## Stage two: return the helper

During a second interval of duration $`T`$, use the same rotating helper reflection with $`U=I_S`$. In the local time $`u\in[0,T]`$ of this stage, the jump is

```math
I_S\otimes r\left(\frac{\pi u}{2T}\right).
```

This stage implements $`\mathrm{id}_S\otimes\mathcal E_T`$ on its actual joint input, including any correlations left by the first stage. Its desired action on the ideal intermediate output is to transfer the helper from $`P_1`$ to $`P_0`$ while leaving the data untouched.

Every instantaneous helper generator is unital, so $`\mathcal E_T(I_C)=I_C`$. Since $`P_1=I_C-P_0`$,

```math
\mathcal E_T(P_1)=I_C-\tau_T,
\qquad
\frac12\|\mathcal E_T(P_1)-P_0\|_1
=\frac12\|\tau_T-P_1\|_1
=\delta_T.
```

Let

```math
\mathcal N_T=(\mathrm{id}_S\otimes\mathcal E_T)\circ\Phi_{1,T},
\qquad
\mathcal J_0=\mathcal T_U.
```

Completely positive trace-preserving postprocessing contracts the diamond norm. Inserting the intermediate channel $`\mathcal J_1`$ and applying the triangle inequality gives

```math
\begin{aligned}
\frac12\|\mathcal N_T-\mathcal J_0\|_\diamond
&\le\frac12
\|(\mathrm{id}_S\otimes\mathcal E_T)
\circ(\Phi_{1,T}-\mathcal J_1)\|_\diamond\\
&\quad+\frac12
\|(\mathrm{id}_S\otimes\mathcal E_T)\circ\mathcal J_1
-\mathcal J_0\|_\diamond\\
&\le\delta_T+\delta_T\\
&\le\frac{\pi^2+\pi}{2T}.
\end{aligned}
```

The contraction in the first term is the step that handles arbitrary data-helper correlations in the actual first-stage output. It does not assume that the helper is already in a product state between the stages.

## Complete schedule and action

The laboratory protocol over $`[0,2T]`$ uses one jump at each time:

```math
L(t)=
\begin{cases}
R_U\!\left(\dfrac{\pi t}{2T}\right),&0\le t\le T,\\[6pt]
I_S\otimes r\!\left(\dfrac{\pi(t-T)}{2T}\right),&T\lt t\le2T.
\end{cases}
```

At the join, the jump changes from $`-I_S\otimes Z`$ to $`+I_S\otimes Z`$. These two jumps have exactly the same dissipator. Thus the join introduces no additional operation or coherent pulse. The schedule is fixed in advance and uses no bath record.

Each stage has $`\|\mathcal L_t\|_{2\to2}=2`$, and so the full generator action is exactly

```math
A=\frac12\int_0^{2T}\|\mathcal L_t\|_{2\to2}\,dt=2T.
```

For a prescribed $`A\gt 0`$, take $`T=A/2`$. The complete-channel bound becomes

```math
\varepsilon_A
=\frac12\|\mathcal N_A-\mathcal T_U\|_\diamond
\le\min\left\{1,\frac{\pi^2+\pi}{A}\right\}.
```

In particular, action $`A=(\pi^2+\pi)/\varepsilon`$ suffices for any requested $`0\lt \varepsilon\le1`$. The protocol uses a two-dimensional helper and the standard input embedding $`\rho\mapsto\rho\otimes P_0`$. The unitaries $`W_U`$ and $`V(t)`$ appear only in the proof of the dissipative evolution; no coherent implementation of them is supplied to the protocol. The target dependence is fully present in the prescribed jump $`R_U(\theta)`$.

The resulting guarantee is approximate joint return at error $`\varepsilon_A`$. It simultaneously controls the implemented gate, the returned helper state, and their residual correlations for every data-reference input.
