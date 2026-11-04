# Related work and the scope of the contribution

The contribution is a return-sensitive action law within deterministic, unmonitored Hermitian-jump control. It combines a dimension-independent converse for approximately returned pure controllers, a weighted converse for exactly returned mixed marginals, matching constructions where stated, and explicit faster gates with controllers that may change. The proofs do not introduce Zeno gates, catalytic correlations, or dissipative completion flags as new concepts.

The comparisons below concern the stated models and the inspected results. They are not an exhaustive priority certification. The bibliography is in [references.bib](references.bib); the full model and limits are in the [scientific overview](../science/README.md).

## Zeno gates and measurement-driven state transfer

**Burgarth, Facchi, Giovannetti, Nakazato, Pascazio, and Yuasa (2013)** derive unitary holonomies from quantum Zeno dynamics. Their “Zeno gate by dissipation” section, equations (25)–(30), explicitly uses time-dependent Hermitian dephasing without reading measurement outcomes; the zero-Hamiltonian case is included. Thus unobserved dephasing can generate a gate through moving subspaces, and the rotating-frame interpretation is established background. [Primary full text](https://arxiv.org/html/1305.6433v2); [journal article](https://doi.org/10.1103/PhysRevA.88.042107).

The present pure-controller upper bound is an explicit finite-action realization of this mechanism. Its role is to match a converse that holds for arbitrary paths and helper dimensions, including nonadiabatic protocols. The fixed-dimension flag construction assembles rotating transfers so that completed diagonal blocks remain untouched; the resulting product formula gives an attainable dimension-dependent error power. It should not be interpreted as a new principle of gate generation by dephasing.

**Pechen, Il'in, Shuang, and Rabitz (2006)** solve a nonselective projective-measurement state-control problem, including optimal qubit population transfer for a finite number of measurements. This is an earlier exact state-transfer baseline. Its resource is measurement count, and its objective is a specified input state and observable. The present task requires an unknown-input unitary channel, including references, and charges the continuous generator action while distinguishing controller return requirements. [Primary record](https://arxiv.org/abs/quant-ph/0606187v2); [journal article](https://doi.org/10.1103/PhysRevA.74.052102).

**Lanka, Garcia-Nila, and Brun**, arXiv:2510.06725v2 (2026 revision), give continuous measurement-based holonomic computation, success-time analysis, and outcome-dependent corrections for rotated stabilizer codes. Their unmonitored master equation also supplies a relevant Hermitian-jump baseline. A protocol that changes its path using the measurement record has a resource absent here. The current converse covers predetermined unobserved protocols rather than ruling out those adaptive methods. [Primary full text](https://arxiv.org/html/2510.06725v2).

**Lewalle, Zhang, and Whaley (2024)** treat the rotating Hermitian qubit dephaser at finite strength, including its averaged evolution without unitary assistance. Section 5.3 and Appendix A give a direct predecessor for the single-stage equation used here. Their Hamiltonian-assisted shortcut changes the allowed controls. The action law in this repository uses independently derived finite-time bounds on that established motion. [Primary full text](https://arxiv.org/html/2311.01631v2); [journal article](https://doi.org/10.1103/PRXQuantum.5.020366).

**Santos, Kamenev, and Gefen (2025)** analyze purity loss in adiabatic dissipative state manipulation. Inverse driving-time corrections are therefore not by themselves a new scaling observation. Their dark-subspace perturbative analysis and the present exact trajectory inequality have different scopes: the latter assumes neither slow driving nor a gap and controls a complete returned-controller gate. The upper bound here is obtained from an exact two-dimensional equation with a finite-time estimate. [Primary full text](https://arxiv.org/html/2406.02286v2); [journal article](https://doi.org/10.1103/PhysRevLett.134.190402).

**Zhang, Sarlette, Lewalle, Karmakar, Scharnhorst, and Whaley (2026)** analyze multichannel Zeno dragging, including unconditional Hermitian-projector dynamics without Hamiltonian control. Their Theorem 2 gives sufficient bounds for transporting population in a common kernel, and Section 4 optimizes subspace fidelity or time to solution. This is a genuine overlap in generator class. Subspace population does not specify the logical unitary, however, and those inspected results give neither a returned-controller gate converse nor the fixed-dimensional flag-channel construction. [Primary publisher text](https://quantum-journal.org/papers/q-2026-07-20-2167/pdf/); [journal record](https://doi.org/10.22331/q-2026-07-20-2167).

## Fidelity, entropy production, and purity geometry

**Vu, Kuwahara, and Saito (2024)** prove fidelity–dissipation relations at arbitrary operation times. Appendix A, equations (22)–(24), gives $`(1-F_\phi)^2\le\gamma_\phi\Sigma_\phi/2`$, with $`\gamma_\phi=\int\sum_j\operatorname{Var}_\phi(L_j)dt`$ in the zero-Hamiltonian Hermitian case. Their model includes this generator class. [Primary full text](https://arxiv.org/html/2311.15762v3); [journal article](https://doi.org/10.1103/PhysRevResearch.6.033225).

Applying that result to the present pure joint-return task gives the following deduction. With total dimension $`n=d_SD_C`$, small error $`0<\epsilon\le1-1/n`$, and natural-log binary entropy $`h`$,

```math
\gamma_\phi\le\int\|\mathcal L_t\|_{2\to2}dt=2A,
\qquad
A\ge\frac{(s(U)^2-\epsilon)_+^2}
{h(\epsilon)+\epsilon\ln(n-1)}.
```

Here a pure unentangled input attains $`s(U)`$, the identity-reference infidelity is at least $`(s(U)^2-\epsilon)_+`$, and the final entropy obeys the displayed continuity bound. This implication has a logarithmic error factor and dimension dependence. The purity-based return law removes both. The factor $`\gamma_\phi\le2A`$ is required by the generator-norm convention; $`\gamma_\phi\le A`$ need not hold for multiple jumps. No claim is made that the cited work states this controller-return deduction.

**Nakajima and Utsumi (2022)** give trace-distance speed limits involving entropy production and dynamical activity. **Brody and Longstaff (2019)** relate open-system evolution speed and purity change through operator-space geometry. These are direct methodological predecessors to connecting motion with dissipative loss. The present proof uses positivity and self-adjointness of $`-\mathcal L_t`$ to obtain the integrated displacement–purity inequality, then converts it into an operational return constraint. [Nakajima–Utsumi primary text](https://arxiv.org/html/2204.02884v4); [Brody–Longstaff primary text](https://arxiv.org/abs/1906.04766); [Brody–Longstaff journal article](https://doi.org/10.1103/PhysRevResearch.1.033127).

## Mixed catalytic controllers

**Lie and Jeong (2021)** provide a structural predecessor for marginally returned catalysts: Proposition 5 and the proof of Theorem 8 connect compatible unitary transformations, maximally mixed inputs, and the catalyst's spectral structure. The [mixed-controller proof](../science/mixed-controllers.md) credits this antecedent. Its additional step is a stationary-product implication for the whole Hermitian-jump trajectory, followed by a weighted norm that yields a spectrum-independent action bound. [Primary article](https://doi.org/10.1103/PhysRevResearch.3.043089).

The operational promise matters. Exact local return can coexist with correlations, so it is weaker than restoration of a purification or independence from past outputs. The lower bound established here permits such correlations. It does not extend, without further work, to arbitrary approximately returned mixed controllers whose spectra and dimensions vary with accuracy.

## Dissipative flags and monitored retries

**Gautier, Mirrahimi, and Sarlette (2023)** already obtain exponentially improving gate accuracy through an initialized auxiliary and a non-Hermitian absorbing jump, in Section VIII and equations (33)–(35). The [consumed-controller proof](../science/consumed-controllers.md) gives the detailed comparison. Its purpose here is a realization using Hermitian exchanges, with every flag level counted, under the same control restriction as the return converse. [Primary article](https://doi.org/10.1103/PRXQuantum.4.040316).

**Oi (2014)** gives unitary holonomies using direct degenerate projections, with repeated attempts and outcome-dependent choice of the next projection. Its observed record and stopping logic are essential resources. Such a protocol is a close antecedent for completion and retry logic, but simply forgetting that record does not produce the prescribed unmonitored channel. The flag schedules here are fixed in advance and their exact channel formulas include every outcome. [Author manuscript](https://strathprints.strath.ac.uk/47925/1/OiDKL_ProjectiveHolonomies_PRA2014_postprint.pdf); [journal article](https://doi.org/10.1103/PhysRevA.89.050102).

The fixed-dimension construction is presented as a proved synthesis of known rotating-dephasing primitives with protected completion subspaces. Its qutrit example answers a resource question about the separation: improving the inverse-action error power does not require a growing controller. The inspected antecedents do not supply an unrestricted fixed-dimension converse, and neither does this repository. In particular, the possibility of exponential accuracy at fixed disposable-controller dimension remains open here.

A direct inference from Pechen's transfer primitive also clarifies this scope. Embedding its $`O(N^{-1})`$ failure into each of $`m`$ protected flag pairs gives $`O(N^{-m})`$ error in ideal measurement count. Approximating each pinching by finite Hermitian dephasing of action $`O(\log N)`$ makes the accumulated approximation error smaller than that transfer error. At fixed $`m`$, the resulting action scaling is $`O((\log A/A)^m)`$ for the error. This is an inference using the flag assembly, not a theorem attributed to Pechen. The continuous rotating construction gives the exact channel and removes that logarithmic overhead.

## General dissipative simulation uses a broader generator class

**Shang and França**, arXiv:2604.18533v2 (2026), approximate Hamiltonian dynamics with non-Hermitian, nontraceless jumps. For their basic form $`F=I-i\delta H`$,

```math
\mathcal D[F](\rho)
=-i\delta[H,\rho]+\delta^2\mathcal D[H](\rho).
```

The identity component induces a coherent term in a canonical decomposition. This construction does not obey the Hermitian-jump restriction used by the return law. Their time-independent simulation converse also concerns a different optimization problem. The phrase “zero explicit Hamiltonian” alone is therefore insufficient to equate the models; Hermiticity and the actual generator must be checked. [Primary full text](https://arxiv.org/html/2604.18533v2).

## Related repository results

The earlier [Dephasing-Control-Geometry](https://github.com/GoGoKo699/Dephasing-Control-Geometry/tree/53a84e2e8dc51e32add4925b2828ce0f6c344f09) account already distinguishes returning a pure workspace from retaining a syndrome and uses purity to derive a return obstruction. Those ideas are explicit antecedents. Its model has fixed commuting data-noise labels, bounded Hamiltonian mixing, and label-preserving auxiliary noise. Its syndrome construction improves specified population errors while a phase error remains at the leading order. The moving Hermitian generators here need not preserve those labels. The present result concerns the complete quantum channel, a generator-action budget, and an exact mixed-marginal converse under that different model.

[Borrowed-Ancilla-Cost](https://github.com/GoGoKo699/Borrowed-Ancilla-Cost/tree/2b1e332c2fb7b394a31ed5808faa121535038a5e) treats unknown borrowed states, excitation-conserving unitary circuits, and width obstructions. [Routing-Bandwidth](https://github.com/GoGoKo699/Routing-Bandwidth/tree/03435de579e4a051907775300a486e1c39b317fd) charges Hamiltonian contact resources and uses a stronger restoration promise involving a controller purification. [Dephasing-Threshold](https://github.com/GoGoKo699/Dephasing-Threshold/tree/340b97e5e82cabcf79b25030ae2289fca485d039) studies simulation of prescribed autonomous dynamics and query resources. These results do not directly imply the stated Hermitian-action law, and their resource meanings should not be interchanged with it.

## Comparison limits

The review used the primary statements and load-bearing derivations cited above, with literature checked through November 4, 2026. The newer bosonic extension by Garcia-Nila, Lanka, and Brun, arXiv:2608.11369, was located at the abstract level; its full text was not available during this comparison. No theorem-level exclusion of that source is claimed. [Primary record](https://arxiv.org/abs/2608.11369).

The supported scientific statement rests on the proofs and explicit channel identities, not on an assertion that every related paper has been excluded. Optimal coefficients, arbitrary approximate mixed return, optimal fixed-dimension disposable scaling, and an unrestricted disposable-controller lower bound remain outside the established claims.
