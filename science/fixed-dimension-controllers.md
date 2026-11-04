# Consumed controllers of fixed dimension

A controller of fixed dimension can already improve the action dependence of the complete data-channel error when its initial state need not be restored. For every target unitary and every integer $`m\ge1`$, the construction below uses a controller of dimension $`m+1`$ and achieves error of order $`A^{-m}`$. In particular, a qutrit achieves quadratic inverse-action error. Thus growing controller dimension is unnecessary for a qualitative separation from the inverse-action law for [approximate clean joint return](return-law.md).

These are achievable rates. They do not determine the optimal exponent at fixed dimension, and they do not resolve whether some fixed-dimensional consumed controller permits exponentially small error. The exponential construction in [Consuming a pure controller](consumed-controllers.md) supplies a separate upper bound with growing dimension.

## Model and statement

Let $`S`$ be a finite-dimensional data system, $`U`$ its target unitary, and $`C`$ a controller with basis $`|0\rangle,\ldots,|m\rangle`$. Initially $`C`$ is in $`|0\rangle`$, independently of the data and any reference. The laboratory Hamiltonian is zero. The evolution uses predetermined Hermitian jumps, with no monitoring, postselection, feedback, reset, or additional initialized system supplied during the protocol. At the end, only the data channel is required to approximate the target.

Write

```math
\mathcal D[L](X)=LXL-\frac12\{L^2,X\},
\qquad L=L^\dagger,
\qquad
A=\frac12\int_0^T\|\mathcal L_t\|_{2\to2}\,dt,
\qquad
s(U)=\frac12\|\operatorname{Ad}_U-\mathrm{id}_S\|_\diamond.
```

The action uses the induced Hilbert–Schmidt norm of the actual generator, as in the [return law](return-law.md). It is invariant under a change of jump representation. The value $`s(U)`$ is positive precisely when $`U`$ is nontrivial as a channel.

**Achievability statement.** Choose positive stage actions $`a_1,\ldots,a_m`$. There is a protocol with total action $`A=\sum_j a_j`$ whose reduced channel is exactly

```math
\mathcal E_m
=Q_m\,\mathrm{id}_S+(1-Q_m)\operatorname{Ad}_U,
\qquad
Q_m=\prod_{j=1}^m q(a_j).
\tag{1}
```

The stage failure function satisfies

```math
0\le q(a)\le\min\left\{1,\frac{\pi^2}{4a}\right\},
\qquad
q(a)=\frac{\pi^2}{4a}+O(a^{-2})
\quad(a\to\infty).
\tag{2}
```

For equal stage actions $`a_j=A/m`$, the exact half-diamond error and its consequences are

```math
\begin{aligned}
\epsilon_m
&:=\frac12\|\mathcal E_m-\operatorname{Ad}_U\|_\diamond
=s(U)\,q(A/m)^m,\\
\epsilon_m
&\le s(U)\min\left\{1,
  \left(\frac{\pi^2m}{4A}\right)^m\right\},\\
\epsilon_m
&=s(U)\left(\frac{\pi^2m}{4}\right)^m A^{-m}
  \left[1+O_m(A^{-1})\right]
\quad\text{for fixed }m.
\end{aligned}
\tag{3}
```

The proof below gives the complete joint channel, including the flag coherences that are absent in the fixed-exchange construction.

## One rotating-dephasing stage

During stage $`j`$, take a duration $`T_j>0`$, a constant rate $`\gamma_j=a_j/T_j`$, and local time $`s=t/T_j\in[0,1]`$. Apply the single jump

```math
\begin{aligned}
L_j(s)=\sqrt{\gamma_j}\Bigl[&
 \cos(\pi s)I_S\otimes
   (|0\rangle\langle0|-|j\rangle\langle j|)\\
 &+\sin(\pi s)
   \bigl(U\otimes|j\rangle\langle0|
        +U^\dagger\otimes|0\rangle\langle j|\bigr)
\Bigr].
\end{aligned}
\tag{4}
```

It acts as zero on all other flag subspaces. If $`P_j=I_S\otimes(|0\rangle\langle0|+|j\rangle\langle j|)`$, then

```math
L_j(s)^\dagger=L_j(s),
\qquad L_j(s)^2=\gamma_j P_j.
```

Its active eigenvalues are $`\pm\sqrt{\gamma_j}`$, with zero eigenvalues on the inactive subspace. A Hermitian jump with eigenvalues $`\lambda_r`$ has dissipator eigenvalues $`-(\lambda_r-\lambda_k)^2/2`$. Consequently,

```math
\|\mathcal D[L_j(s)]\|_{2\to2}=2\gamma_j,
\qquad
\frac12\int_0^{T_j}\|\mathcal D[L_j(t/T_j)]\|_{2\to2}\,dt
=\gamma_jT_j=a_j.
\tag{5}
```

This equality accounts for the full generator, including its action on cross-flag operators. The inactive subspaces do not increase its norm. Also $`\|L_j(s)\|_\infty^2=\gamma_j`$, so the generator action and integrated jump-norm budget agree for this construction.

For the one-stage calculation, use the time-independent change of coordinates

```math
W_j=I_S\otimes\sum_{k\ne j}|k\rangle\langle k|
       +U\otimes|j\rangle\langle j|.
```

On the active pair, $`W_j^\dagger L_j(s)W_j`$ equals $`\sqrt{\gamma_j}I_S\otimes[\cos(\pi s)Z+\sin(\pi s)X]`$. This is an identity used to solve the evolution. No application of $`W_j`$, coherent encoding, or endpoint decoder is included in the physical protocol.

Starting in flag $`0`$, the active joint output is therefore

```math
W_j\bigl(\rho\otimes\tau_a\bigr)W_j^\dagger,
\qquad
\tau_a=
\begin{pmatrix}q(a)&b(a)\\b(a)&1-q(a)\end{pmatrix},
\qquad a=a_j.
\tag{6}
```

To calculate $`\tau_a`$, express its Bloch vector in the frame rotating with the dephasing axis. The two nonzero components satisfy

```math
\frac{d}{ds}
\begin{pmatrix}z_a\\x_a\end{pmatrix}
=\begin{pmatrix}0&\pi\\-\pi&-2a\end{pmatrix}
\begin{pmatrix}z_a\\x_a\end{pmatrix},
\qquad(z_a(0),x_a(0))=(1,0).
\tag{7}
```

At $`s=1`$ the frame has rotated by $`\pi`$. Thus

```math
q(a)=\frac{1-z_a(1)}2,
\qquad b(a)=-\frac{x_a(1)}2,
\qquad
z_a''+2az_a'+\pi^2z_a=0.
\tag{8}
```

For $`a>\pi`$, putting $`\Delta=\sqrt{a^2-\pi^2}`$ gives the explicit formulas

```math
\begin{aligned}
z_a(1)&=e^{-a}\left(\cosh\Delta+\frac{a}{\Delta}\sinh\Delta\right),\\
b(a)&=\frac{\pi e^{-a}}{2\Delta}\sinh\Delta.
\end{aligned}
\tag{9}
```

For $`0\le a<\pi`$, replace $`\Delta`$ by $`i\sqrt{\pi^2-a^2}`$, so the expressions are real trigonometric functions. At $`a=\pi`$, take the continuous limit: $`z_a(1)=e^{-\pi}(1+\pi)`$ and $`b(a)=\pi e^{-\pi}/2`$. At zero action, $`q(0)=1`$.

For a finite-action bound, (7) implies

```math
\frac{d}{ds}(z_a^2+x_a^2)=-4ax_a^2\le0,
\qquad |z_a(s)|\le1.
```

Solving the second equation of (7) by an integrating factor and integrating the first gives

```math
1-z_a(1)
=\pi^2\int_0^1du\int_0^u dv\,
   e^{-2a(u-v)}z_a(v)
\le\frac{\pi^2}{2a}.
```

Positivity of the one-qubit output gives $`0\le q(a)\le1`$, proving the bound in (2). Expanding (9) at large $`a`$ gives the stated asymptotic formula. Neither (6) nor the error bound requires an adiabatic approximation.

## Cross-flag autonomy and the complete channel

The one-stage output generally contains a coherence between flags $`0`$ and $`j`$. It must be included when composing stages.

During stage $`j`$, decompose the joint operator space using the active Hilbert subspace $`P_j`$ and its orthogonal complement. With block labels $`A`$ and $`B`$, respectively, the jump has the form $`L_j=L_A\oplus0`$ and $`L_A^2=\gamma_jI_A`$. Every joint operator obeys

```math
\begin{aligned}
\dot X_{AA}&=\mathcal D[L_A](X_{AA}),
&\dot X_{BB}&=0,\\
\dot X_{AB}&=-\frac{\gamma_j}{2}X_{AB},
&\dot X_{BA}&=-\frac{\gamma_j}{2}X_{BA}.
\end{aligned}
\tag{10}
```

Thus cross-flag coherences cannot feed the active diagonal blocks. A coherence joining an old success flag to flag $`0`$ is multiplied by $`e^{-a_j/2}`$ during this stage. It is not transferred to the new success flag.

Define

```math
q_j=q(a_j),\qquad b_j=b(a_j),\qquad
Q_0=1,\qquad Q_j=\prod_{k=1}^j q_k,
\qquad
c_j=Q_{j-1}b_j\exp\left(-\frac12\sum_{k=j+1}^m a_k\right).
```

At the start of stage $`j`$, its flag $`j`$ is unoccupied. By (10), its active input block is exactly $`Q_{j-1}\rho\otimes|0\rangle\langle0|`$. Equation (6) transfers weight $`Q_{j-1}(1-q_j)`$ to the new flag and leaves weight $`Q_j`$ in flag $`0`$. Earlier success diagonals stay fixed. The newly generated $`0,j`$ coherence then undergoes the damping in (10) at each later stage. Induction gives the full joint channel

```math
\begin{aligned}
\mathcal F_m(\rho)
={}&Q_m\rho\otimes|0\rangle\langle0|\\
&+\sum_{j=1}^m Q_{j-1}(1-q_j)
     U\rho U^\dagger\otimes|j\rangle\langle j|\\
&+\sum_{j=1}^m\left[
 c_j\rho U^\dagger\otimes|0\rangle\langle j|
 +c_j^*U\rho\otimes|j\rangle\langle0|
 \right].
\end{aligned}
\tag{11}
```

Here $`c_j`$ is real for the chosen path; the conjugation in (11) also makes the Hermitian pairing explicit. There are no coherences between two different success flags. The formula is linear in the input operator, not merely a statement about input populations.

Every step remains valid with an arbitrary inert reference $`R`$: replace $`\rho`$ by an operator on $`RS`$ and $`U`$ by $`I_R\otimes U`$. The cross-block equations are unchanged, and tensoring the generator with the identity on $`R`$ leaves its induced Hilbert–Schmidt norm unchanged. This proves (11) as a complete-channel identity with the same action.

Tracing out $`C`$ removes all cross-flag terms. Since $`\sum_j Q_{j-1}(1-q_j)=1-Q_m`$, equation (11) gives (1). Homogeneity of the diamond norm then gives the exact error in (3). No branch has been selected or discarded before this final partial trace.

## A fixed qutrit

Set $`m=2`$ and give each of the two stages action $`A/2`$. For every target unitary,

```math
\epsilon_2=s(U)\,q(A/2)^2
=s(U)\frac{\pi^4}{4A^2}+O_U(A^{-3}).
\tag{12}
```

For a Pauli $`Z`$ gate, $`s(Z)=1`$, so the leading coefficient is exactly $`\pi^4/4`$. More generally, a fixed controller dimension $`D=m+1`$ achieves $`O_U(A^{-(D-1)})`$. Equivalently, for fixed $`D`$ it suffices to use action $`O_U(\epsilon^{-1/(D-1)})`$ in this family.

The qutrit already separates this consumed-state contract from approximate clean joint return, whose lower bound holds for arbitrary controller dimension. Equation (12) does not establish that the qutrit exponent is optimal.

## Controller entropy with input-dependent coherences

For equal stage actions, write $`q=q(A/m)`$. Equation (11) fixes the final controller's diagonal probabilities for every input:

```math
p_0=q^m,\qquad
p_j=(1-q)q^{j-1}\quad(1\le j\le m).
\tag{13}
```

Its off-diagonal entries need not vanish: for example, the $`0,j`$ entry is $`c_j\operatorname{Tr}(\rho U^\dagger)`$. The controller marginal is therefore generally input dependent, and (13) alone is not its density matrix.

Nevertheless, pinching in the flag basis cannot decrease von Neumann entropy. Define entropy in bits by $`S_2(\beta)=-\operatorname{Tr}(\beta\log_2\beta)`$ and binary entropy by $`h_2(q)=-q\log_2q-(1-q)\log_2(1-q)`$. For the actual controller marginal $`\beta_C`$ and $`0<q<1`$,

```math
\begin{aligned}
S_2(\beta_C)
&\le H(p_0,\ldots,p_m)\\
&=h_2(q)\sum_{k=0}^{m-1}q^k
=\frac{1-q^m}{1-q}h_2(q)
\le\frac{h_2(q)}{1-q}.
\end{aligned}
\tag{14}
```

The identity for the classical entropy follows by resolving the first stage: $`H_m=h_2(q)+qH_{m-1}`$, with $`H_0=0`$. The pinching bound holds uniformly over data inputs, including those entangled with a reference. It does not assert equality for the actual marginal.

At fixed $`m`$ and large $`A`$, $`q=O_m(A^{-1})`$, so (14) gives $`S_2(\beta_C)=O_m((\log A)/A)`$. Meanwhile, measuring whether the controller is in flag $`0`$ gives

```math
\frac12\|\beta_C-|0\rangle\langle0|\|_1\ge1-q^m.
```

Thus the controller's entropy can vanish while its distance from the supplied state tends to one. Consumption here means that the supplied controller state need not be restored. It does not require a nonzero limiting entropy increase. Restoring that physical state is an additional task, and the displayed action includes no such restoration. No heat or work cost follows from (14).

## Scope and relation to established mechanisms

Rotating the monitored observable is established Zeno dragging. Lewalle, Zhang, and Whaley study this mechanism and its control optimization in [*Optimal Zeno Dragging for Quantum Control: A Shortcut to Zeno with Action-Based Scheduling Optimization*, PRX Quantum **5**, 020366 (2024)](https://doi.org/10.1103/PRXQuantum.5.020366). The single-stage qubit motion used here belongs to that family; no priority is claimed for that mechanism or for implementing gates by moving dissipative subspaces.

Ancillary records of gate completion also precede this construction. Section VIII of Gautier, Mirrahimi, and Sarlette's [*Designing High-Fidelity Zeno Gates for Dissipative Cat Qubits*, PRX Quantum **4**, 040316 (2023)](https://doi.org/10.1103/PRXQuantum.4.040316) uses a dissipative auxiliary to obtain exponentially improving gate accuracy. Its absorbing transition uses a non-Hermitian jump. In (4), each active transfer instead uses a Hermitian jump, and an earlier completion flag remains dark because the predetermined later stages do not address it. The finite-dimensional calculation combines these familiar ideas to account for the full channel, flag coherences, controller dimension, and the common generator action in the return comparison.

The jump in (4) contains the target operator $`U`$ and requires selective coupling to each addressed flag. The action does not charge the synthesis or locality of that coupling, the cost of preparing the initial pure controller, or an external clock implementing the schedule. All controller levels used by the protocol are included from the start; there is no resetting of a smaller controller hidden in the stage notation. The result concerns this supplied-control model and does not establish an advantage in compiled gate complexity.

The optimal achievable accuracy at a given fixed controller dimension remains open here. In particular, these polynomial upper bounds neither establish nor exclude exponential accuracy at fixed dimension.

## Verification

[`verification/fixed_dimension.py`](../verification/fixed_dimension.py) integrates the complete data–reference–controller master equation and compares its output with (11), as well as the reduced channel (1). The checks include noncommuting target matrix entries, unequal stage actions, the qutrit coefficient, the generator-action normalization, and the entropy upper bound with controller coherences retained. They provide numerical checks of the formulas; the reference-preserving block argument above proves the complete-channel statement.
