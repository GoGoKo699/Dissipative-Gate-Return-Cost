# Model, result map, and physical interpretation

The question is whether an accurate gate must pay for restoring the controller that helped produce it. We compare several return requirements under the same deterministic Hermitian-jump dynamics. The target unitary is fixed in advance, the data input is unknown, and the output guarantee includes arbitrary initial data-reference entanglement.

The scientific claim is the combination of a universal return bound, matching constructions where stated, and explicit faster protocols when the supplied controller may change. Neither Zeno gates nor the general connection between speed and dissipation is new; the [primary-source comparison](../references/RELATED_WORK.md) identifies the inherited mechanisms and the additional operational statement.

## The control resource

The joint system $`SC`$ is finite dimensional, starts in $`\rho_S\otimes\beta_C`$, and follows

```math
\mathcal L_t(X)=-\frac12\sum_j[L_j(t),[L_j(t),X]],
\qquad L_j(t)=L_j(t)^\dagger,
\qquad
A=\frac12\int_0^T\|\mathcal L_t\|_{2\to2}\,dt.
```

The controller includes every supplied helper degree of freedom. Its dimension may depend on the requested accuracy unless explicitly held fixed. The schedule is chosen before the input is supplied. All bath outcomes are averaged over, and the terminal time is fixed. No additional Hamiltonian, observed measurement record, adaptive stopping, coherent decoder, reset, or injected pure state is available during the evolution.

The action uses the induced Hilbert–Schmidt norm, which is the largest singular value of the generator matrix in an orthonormal operator basis. It is not that matrix's Frobenius norm. The generator is negative and self-adjoint in this operator space. Real identity shifts of a Hermitian jump do not change it, and the norm does not depend on how the same generator is decomposed into jumps. An inert reference leaves the induced norm unchanged. These facts make the action suitable for complete-channel bounds.

For a single jump with spectral endpoints $`\ell_{\min}`$ and $`\ell_{\max}`$,

```math
\frac12\|\mathcal D[L]\|_{2\to2}
=\frac{(\ell_{\max}-\ell_{\min})^2}{4}.
```

Every construction here uses one active jump with eigenvalues $`\pm\sqrt\gamma`$, possibly also zero. A stage of duration $`T`$ therefore costs exactly $`\gamma T`$. If a laboratory bounds the action rate by $`\alpha_{\max}`$, then $`T\ge A/\alpha_{\max}`$; the action lower bounds immediately imply time lower bounds under that additional rate constraint.

The model supplies the target-dependent jump and the ability to address its controller levels. For a large many-body $`U`$, this may be a demanding control resource. Encoding $`D`$ levels in $`\lceil\log_2D\rceil`$ qubits does not by itself make a level-selective transition local or easy to compile.

## The return contracts are different operational tasks

For the target displacement and channel error, use half-diamond distances. In particular,

```math
s(U)=\frac12\|\operatorname{Ad}_U-\mathrm{id}\|_\diamond.
```

A pure controller with approximate joint return is scored against the complete target $`\rho\mapsto U\rho U^\dagger\otimes|0\rangle\langle0|`$. This controls the gate error, the controller defect, and their correlations at once. The [pure-return theorem](return-law.md) and [one-qubit construction](pure-helper.md) show

```math
\frac{(s(U)-\epsilon)^2}{\epsilon}
\le A_{\min}(\epsilon;U)
\le\frac{\pi^2+\pi}{\epsilon},
\qquad 0<\epsilon<s(U).
```

An arbitrary mixed controller with exact marginal return obeys the same lower bound while allowing final correlations. The [mixed-return theorem](mixed-controllers.md) uses only return on the maximally mixed data input. Purity monotonicity forces that input's entire joint state to remain stationary, so every jump commutes with $`I_S\otimes\beta`$. A weighted norm then removes the factor that ordinary purity would introduce through $`\operatorname{Tr}\beta^2`$. A qubit controller in $`I/2`$ gives a matching inverse-action construction for the fixed target $`Z`$.

Exact marginal return of a mixed state does not preserve an arbitrary inaccessible purification of that state. It also does not imply that the controller is independent of earlier outputs and freely reusable in every later task. Conversely, exact return of an initially pure state is stronger than approximate joint return: the rigidity argument makes its support invariant throughout. The approximate-return construction should not be read as an exact pure-return construction.

## A controller that may change can retain unsuccessful branches

In the [exchange-flag construction](consumed-controllers.md), the controller starts in level zero. Stage $`j`$ couples levels zero and $`j`$ with a Hermitian operator that applies $`U`$ on the forward transition. Earlier completed levels are untouched. The unobserved evolution gives the exact channel

```math
\mathcal E_m=q^m\,\mathrm{id}+(1-q^m)\operatorname{Ad}_U,
\qquad q=\frac{1+e^{-2a}}2,
\qquad A=ma.
```

The channel formula is an operator identity, so its error is exactly $`s(U)q^m`$ even with a reference. No flag is measured and no outcome is selected. The controller has $`m+1`$ levels and ends in a known geometric distribution, substantially different from its initial state. At fixed stage action its entropy remains bounded as the support dimension grows.

The [fixed-dimension construction](fixed-dimension-controllers.md) uses a rotating dephasing transfer in each active pair. Its one-stage failure probability is $`q(a)=\pi^2/(4a)+O(a^{-2})`$. The same block structure multiplies the failure probabilities, giving

```math
\mathcal E=Q\,\mathrm{id}+(1-Q)\operatorname{Ad}_U,
\qquad Q=\prod_{j=1}^{m}q(a_j),
\qquad \sum_j a_j=A.
```

At equal allocation and fixed $`m`$, the error is $`O_U(A^{-m})`$ with controller dimension $`m+1`$. Inter-flag coherences can be present, but they never feed the active diagonal blocks and disappear on tracing the controller. A qutrit already attains $`O(A^{-2})`$, so a fixed-size controller can improve the exponent when return is removed.

This controller may end close to a pure success state, with entropy tending to zero. It still has a large defect relative to the supplied level-zero state. The separation therefore does not require a fixed nonzero entropy increase at the endpoint. It requires an initially nonuniform controller and permission to leave its state changed. The maximally mixed-controller corollary excludes the same advantage from a uniform initial resource even if it is discarded.

## Why monitored control is outside the theorem

A bath record can change the task. For example, a Hermitian Pauli jump $`L=\sqrt\gamma Z`$ has a state-independent jump rate. If the first jump is observed and the evolution is stopped immediately, the conditioned operation is exactly $`Z`$, with finite mean waiting action. That protocol uses both a record and a random stopping time. The present results concern the unconditioned channel at a predetermined terminal time. The distinction is part of the model, rather than an experimental approximation to the theorem.

Likewise, adding Hamiltonian control can directly enact a unitary while preserving purity. A commutator term created by changing coordinates in a proof is harmless, but a physically supplied Hamiltonian changes the allowed operations. The [related-work discussion](../references/RELATED_WORK.md) compares non-Hermitian dissipative constructions whose canonical decomposition contains such a coherent contribution.

## Established scope and remaining questions

The pure joint-return action order is optimal for every fixed nontrivial finite-dimensional target. The exact mixed-return lower bound is uniform in controller dimension and spectrum, with an explicit matching order for $`Z`$. The consumed-controller protocols establish attainable error powers and an exponential construction under stated dimension scaling.

Several questions remain outside these results: the optimal coefficients for returned controllers, attainability for general targets under exact mixed marginal return, a dimension-uniform bound for approximately returned arbitrary mixed states, the optimal accuracy at fixed disposable-controller dimension, and an unrestricted converse for disposable controllers. The failed shortcut of treating every no-jump trajectory as an identity branch is explained in the [consumed-controller note](consumed-controllers.md). None of these unresolved questions is used as a premise for the proved separation.

For the executable checks and their limits, see [verification](../verification/README.md). Each universal statement is justified analytically; finite numerical cases corroborate the equations and channel identities.
