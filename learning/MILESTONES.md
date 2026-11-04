# Thirty milestones for dissipative gate return cost

This map follows the project's scientific dependencies, from an unread measurement on a single state to a comparison of complete gates under different controller-return requirements. It contains exactly 30 understanding targets in two phases.

The **11 background/preliminaries milestones** connect measurement averaging, open-system generators, operator geometry, reference systems, and controller resources. These ingredients are needed together to formulate the comparison. The **19 narrative/innovation milestones** develop the two converse arguments and their constructions, then connect consumed flags, controller dimension, entropy, attribution, and the remaining limits. The final milestone of each phase integrates its preceding ideas.

The single educational anchor is Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control* (2010), abbreviated **W&M**. Its verified section numbers and starting pages are recorded in [the anchor bridge](ANCHOR_BRIDGE.md#the-educational-anchor). Section pointers below identify relevant foundations; the bridge supplies additional complete-channel notation and connects those foundations to the project-specific derivations. The canonical claims and proofs remain in [the scientific account](../science/README.md).

Throughout, $`S`$ is the data system, $`C`$ the supplied controller, and $`R`$ an inert reference. The target is the channel $`\operatorname{Ad}_U(\rho)=U\rho U^\dagger`$. The symbols $`A`$, $`\epsilon`$, and $`s(U)`$ retain the conventions of the canonical science pages.

## Background/preliminaries: M01–M11

### M01. States and the target gate

**Phase:** Background/preliminaries.

**Central question:** What does a unitary gate preserve when its input state is unknown?

**Understanding target:** Distinguish a density operator from a particular ensemble representing it, and a unitary channel from a state-preparation procedure. Recognize that the target must act correctly on populations and coherences for every permitted input.

**Dependencies and story role:** None. Establishes the local objects and the gate task before introducing a controller or a bath.

**Conceptual connection:** A phase flip leaves computational-basis populations unchanged, so successful population transfer alone cannot certify the required gate.

**Source pointers:** W&M A.1 and §1.2, through [the phase-flip example](ANCHOR_BRIDGE.md#a-phase-flip-and-an-unread-measurement); [model and error convention](../science/return-law.md#model-and-error-convention).

### M02. Data, controller, and reference

**Phase:** Background/preliminaries.

**Central question:** Which information is retained or lost when a subsystem is traced out?

**Understanding target:** Identify the roles of $`S`$, $`C`$, and $`R`$; distinguish a joint state, its marginals, and its correlations. Understand why an initially independent controller can become correlated with the data while the reference remains dynamically inert.

**Dependencies and story role:** M01. Extends the local state description to the composite systems on which return promises are imposed.

**Conceptual connection:** A statement about the controller's marginal and a statement about the entire output constrain different physical information.

**Source pointers:** W&M A.2, through [states, channels, and reference systems](ANCHOR_BRIDGE.md#states-channels-and-reference-systems); [the different return contracts](../science/README.md#the-return-contracts-are-different-operational-tasks).

### M03. Observed outcomes and unread measurements

**Phase:** Background/preliminaries.

**Central question:** How does averaging measurement outcomes change the operation being described?

**Understanding target:** Distinguish an outcome-conditioned state update from the trace-preserving channel obtained by summing all outcomes. Identify where a measurement record, postselection, or outcome-dependent control would enter a protocol.

**Dependencies and story role:** M01 and M02. Introduces the operational meaning of an unobserved environment before continuous dynamics is specified.

**Conceptual connection:** A favorable trajectory does not establish an accurate deterministic gate; the project evaluates the unconditioned channel.

**Source pointers:** W&M §§1.3–1.4, through [measurement updates and Hermitian generators](ANCHOR_BRIDGE.md#from-measurement-updates-to-hermitian-generators); [why monitored control is outside the theorem](../science/README.md#why-monitored-control-is-outside-the-theorem).

### M04. The allowed Markovian generator

**Phase:** Background/preliminaries.

**Central question:** What restriction does a zero-Hamiltonian Hermitian-jump generator impose?

**Understanding target:** Relate a Lindblad generator to its completely positive, trace-preserving evolution. Recognize the double-commutator form for Hermitian jumps, its unitality, and the distinction between this restricted generator and general dissipative evolution.

**Dependencies and story role:** M03. Converts the measurement description into the differential model used throughout the project.

**Conceptual connection:** The generator class determines which purity identities and resource comparisons remain valid.

**Source pointers:** W&M §3.6, through [measurement updates and Hermitian generators](ANCHOR_BRIDGE.md#from-measurement-updates-to-hermitian-generators); [the control resource](../science/README.md#the-control-resource).

### M05. Dephasing and a moving protected subspace

**Phase:** Background/preliminaries.

**Central question:** How can changing a dephasing basis transport a state?

**Understanding target:** Distinguish decay of coherences relative to a fixed observable from motion induced by changing that observable. Interpret a Bloch-sphere description of rotating dephasing, including the difference between a mathematical rotating frame and a supplied laboratory Hamiltonian.

**Dependencies and story role:** M01 and M04. Introduces the established physical mechanism used by the later upper bounds.

**Conceptual connection:** The protected directions of a dissipator can move even though the laboratory dynamics contains no Hamiltonian term.

**Source pointers:** W&M §§3.7 and 4.6, through [the two-stage helper construction](ANCHOR_BRIDGE.md#a-two-stage-helper-construction); [the rotating dephasing equation](../science/pure-helper.md#a-finite-time-bound-on-the-rotating-dephasing-equation).

### M06. Geometry on operator space

**Phase:** Background/preliminaries.

**Central question:** Why is the negative of a Hermitian dissipator positive on operator space?

**Understanding target:** Distinguish the trace norm of a state difference, the Hilbert–Schmidt norm of an operator, and the induced norm of a superoperator, including its distinction from a matrix Frobenius norm. Understand why $`-\mathcal L_t`$ is positive and self-adjoint on Hilbert–Schmidt space for the allowed generators.

**Dependencies and story role:** M01 and M04. Supplies the geometric vocabulary needed for an action budget and a speed–purity estimate.

**Conceptual connection:** Positivity on operator space turns a dynamical equation into inequalities relating motion to loss of purity.

**Source pointers:** W&M A.1 and §3.6, through [notation and the generator action](ANCHOR_BRIDGE.md#notation-and-the-generator-action); [generator action and representation accounting](../science/return-law.md#generator-action-and-representation-accounting).

### M07. Complete-channel accuracy

**Phase:** Background/preliminaries.

**Central question:** What must a gate-error guarantee protect beyond a chosen input state?

**Understanding target:** Interpret half-diamond distance as a worst-case channel error that includes an inert reference. Distinguish it from a population error, a fidelity for one state, or a trace distance between normalized Choi states. Identify $`s(U)`$ as the target's displacement from the identity channel.

**Dependencies and story role:** M02, M03, and M06. Establishes the operational accuracy criterion before any resource bound is compared.

**Conceptual connection:** A complete-channel statement protects unknown quantum information, including its pre-existing entanglement.

**Source pointers:** W&M A.2 and §1.4, through [states, channels, and reference systems](ANCHOR_BRIDGE.md#states-channels-and-reference-systems); [model and error convention](../science/return-law.md#model-and-error-convention).

### M08. Three controller-return promises

**Phase:** Background/preliminaries.

**Central question:** What exactly is restored when a controller is said to return?

**Understanding target:** Distinguish approximate joint return of an initially pure controller, exact marginal return of a mixed controller, and permission to leave the controller changed. Keep exact pure return and preservation of an external controller purification separate from these promises.

**Dependencies and story role:** M02 and M07. Organizes the output requirements that will define the project's different optimization problems.

**Conceptual connection:** Correlations and the quantifier over data inputs matter as much as the controller's final local density operator.

**Source pointers:** W&M A.2, through [states, channels, and reference systems](ANCHOR_BRIDGE.md#states-channels-and-reference-systems); [the different return contracts](../science/README.md#the-return-contracts-are-different-operational-tasks).

### M09. Purity, entropy, and state restoration

**Phase:** Background/preliminaries.

**Central question:** Why do low entropy and a small return error express different properties?

**Understanding target:** Distinguish purity, von Neumann entropy, controller dimension, and distance from a specified initial state. Recognize that entropy depends on the density operator rather than its chosen ensemble, and that two distinct pure states have the same entropy.

**Dependencies and story role:** M01, M02, and M08. Prepares the interpretation of both purity-based bounds and consumed-controller entropy calculations.

**Conceptual connection:** A controller can retain little entropy while ending far from the physical state supplied at the start.

**Source pointers:** W&M §3.8 and A.1, through [fixed controller dimension](ANCHOR_BRIDGE.md#fixed-controller-dimension); [controller entropy with input-dependent coherences](../science/fixed-dimension-controllers.md#controller-entropy-with-input-dependent-coherences).

### M10. The control schedule and resource boundary

**Phase:** Background/preliminaries.

**Central question:** Which controls and stopping rules belong to the stated task?

**Understanding target:** Identify the predetermined schedule and terminal time, the supplied controller, and the absence of intermediate reset or observed bath records. Separate mathematical coordinate changes from physical operations and distinguish an action budget from a cost of synthesizing the chosen coupling.

**Dependencies and story role:** M03, M04, M05, and M08. Makes the resource boundary explicit before a lower bound or a fast construction is assessed.

**Conceptual connection:** Monitoring a jump and stopping when it occurs changes the available operations, even if the underlying dissipator is unchanged.

**Source pointers:** W&M §4.2, through [the phase-flip example](ANCHOR_BRIDGE.md#a-phase-flip-and-an-unread-measurement); [the control resource](../science/README.md#the-control-resource) and [monitored-control boundary](../science/README.md#why-monitored-control-is-outside-the-theorem).

### M11. The common gate-and-controller problem

**Phase:** Background/preliminaries.

**Central question:** What must remain common for a return-sensitive comparison to be meaningful?

**Understanding target:** Assemble the unknown-input unitary task, complete-channel error, zero-Hamiltonian Hermitian dynamics, controller initialization, and resource boundary into one framework. Identify the return promise as the condition varied between the main comparisons, while keeping initial controller states and dimensions explicit.

**Dependencies and story role:** M05–M10, with their earlier dependencies. Integrates the background phase into the precise problem addressed by the proofs and constructions.

**Conceptual connection:** Measurement theory, composite-system information, and open-system geometry now describe one operational question: the cost of implementing a gate while restoring its controller.

**Source pointers:** W&M §§1.4, 3.6, and A.2, through [what the project adds](ANCHOR_BRIDGE.md#what-the-project-adds); [model, result map, and physical interpretation](../science/README.md).

## Narrative/innovation: M12–M30

### M12. An action attached to the generator

**Phase:** Narrative/innovation.

**Central question:** How can dissipative action be charged without depending on an arbitrary jump representation?

**Understanding target:** Explain the normalization $`A=\tfrac12\int\|\mathcal L_t\|_{2\to2}\,dt`$, its invariance under representation changes, and its behavior under an inert reference. Relate the single-jump spectral-diameter formula to the stage cost $`\gamma T`$ and distinguish it from a general sum of jump costs.

**Dependencies and story role:** M06, M10, and M11. Establishes the common quantitative resource before comparing any protocol families.

**Conceptual connection:** Generator-level accounting prevents identity shifts or redundant jump lists from changing the stated cost of the same dynamics.

**Source pointers:** W&M §3.6 and A.1, through [notation and the generator action](ANCHOR_BRIDGE.md#notation-and-the-generator-action); [generator action and representation accounting](../science/return-law.md#generator-action-and-representation-accounting).

### M13. Displacement paid for by purity loss

**Phase:** Narrative/innovation.

**Central question:** Why does motion under a Hermitian dissipator require loss of purity?

**Understanding target:** Follow the route from the exact purity derivative to the spectral inequality for $`-\mathcal L_t`$, then to the integrated displacement–purity bound. Identify where the generator action enters and why no gap, adiabatic assumption, or bound on controller dimension is needed.

**Dependencies and story role:** M06 and M12. Develops the local-to-trajectory estimate on which the return converse rests.

**Conceptual connection:** The same positive operator governs instantaneous velocity and purity loss, allowing the two to be compared along an arbitrary path.

**Source pointers:** W&M §3.7 and A.1, through [displacement and purity loss](ANCHOR_BRIDGE.md#displacement-and-purity-loss); [the trajectory lemma](../science/return-law.md#displacement-requires-purity-loss).

### M14. The pure joint-return converse

**Phase:** Narrative/innovation.

**Central question:** How does joint return convert the purity estimate into an inverse-error action law?

**Understanding target:** Connect a pure input witnessing $`s(U)`$, a near-pure desired joint output, and the trajectory lemma to $`(s(U)-\epsilon)_+^2\le A\epsilon`$. Track why the error controls correlations as well as marginals and why enlarging the initially pure controller cannot remove the bound.

**Dependencies and story role:** M07, M08, and M13. Converts geometric dissipation into the first operational lower bound.

**Conceptual connection:** A nontrivial gate requires finite displacement, while accurate return to a pure joint target leaves little permitted purity loss.

**Source pointers:** W&M §3.6 and A.2, through [approximate pure joint return](ANCHOR_BRIDGE.md#approximate-pure-joint-return); [finite-action return bound](../science/return-law.md#finite-action-return-bound).

### M15. A single helper transfer as an exact channel

**Phase:** Narrative/innovation.

**Central question:** How does a rotating helper dephaser carry an arbitrary target unitary?

**Understanding target:** Explain the Hermitian reflection containing $`U`$ and its exact reduction, by a constant change of coordinates, to a one-qubit dephasing equation. Relate the helper-state error to the complete first-stage channel error without treating the coordinate change as a free physical gate.

**Dependencies and story role:** M05, M07, M10, and M12. Builds the constructive component that can attain the lower-bound order.

**Conceptual connection:** A solvable local Bloch equation can control an unknown-input gate in any finite data dimension because the reduction is an operator identity.

**Source pointers:** W&M §§3.7 and 4.6, through [the two-stage helper construction](ANCHOR_BRIDGE.md#a-two-stage-helper-construction); [Hermitian reflections](../science/pure-helper.md#a-family-of-hermitian-reflections) and [stage-one channel](../science/pure-helper.md#stage-one-carry-the-data-unitary-into-the-helper-one-subspace).

### M16. Returning the helper and matching the converse

**Phase:** Narrative/innovation.

**Central question:** How does a second dissipative stage restore the helper while controlling residual correlations?

**Understanding target:** Combine the finite-time dephasing estimate, unitality, and complete-channel contraction to obtain the two-stage joint-return upper bound. Compare it with M14 to identify the optimal $`\Theta_U(\epsilon^{-1})`$ action order for every fixed nontrivial target, without asserting an optimal coefficient or exact pure return.

**Dependencies and story role:** M14 and M15. Completes the pure-controller argument by joining a universal converse to an explicit fixed-size construction.

**Conceptual connection:** Controlling the actual correlated intermediate output is essential to proving approximate joint return.

**Source pointers:** W&M §4.6 and A.2, through [the two-stage helper construction](ANCHOR_BRIDGE.md#a-two-stage-helper-construction); [stage two](../science/pure-helper.md#stage-two-return-the-helper) and [optimal inverse-accuracy order](../science/return-law.md#optimal-inverse-accuracy-order).

### M17. Exact marginal return forces stationarity

**Phase:** Narrative/innovation.

**Central question:** How can return on one data input constrain every instantaneous jump?

**Understanding target:** Follow the argument from exact controller return on the maximally mixed data input to stationarity of $`I_S/d\otimes\beta`$ and commutation with every jump. Understand the invariant-support consequence for singular $`\beta`$ and why exact pure return excludes the excursions allowed by approximate return.

**Dependencies and story role:** M08, M11, and M13. Establishes the structural ingredient needed to handle a mixed controller without assuming a product final output.

**Conceptual connection:** An endpoint marginal condition becomes a constraint on the entire Hermitian dissipative trajectory.

**Source pointers:** W&M §3.6 and A.2, through [exact mixed marginal return](ANCHOR_BRIDGE.md#exact-mixed-marginal-return); [stationary-product argument](../science/mixed-controllers.md#1-return-on-the-maximally-mixed-input-forces-a-stationary-product) and [singular controller states](../science/mixed-controllers.md#singular-controller-states).

### M18. The weighted mixed-controller converse

**Phase:** Narrative/innovation.

**Central question:** How can the return bound avoid a factor depending on the controller's spectrum?

**Understanding target:** Explain the $`\beta^{-1}`$-weighted geometry on the invariant support and the orthogonal projection onto data operators tensored with $`\beta`$. Connect these to the same finite-action bound as M14, including the pure-data witness for $`s(U)`$ and the maximally mixed-controller corollary even when its output is discarded.

**Dependencies and story role:** M12, M13, M14, and M17. Extends the action obstruction to exact mixed marginal return while permitting correlations.

**Conceptual connection:** Stationarity makes the spectral weight compatible with the dynamics; the weight removes the dilution of ordinary purity by a mixed controller.

**Source pointers:** W&M §3.6 and A.1, through [exact mixed marginal return](ANCHOR_BRIDGE.md#exact-mixed-marginal-return); [weighted inequality and data projection](../science/mixed-controllers.md) and [maximally mixed-controller consequence](../science/mixed-controllers.md#4-initially-maximally-mixed-controllers-may-be-discarded-and-still-obey-the-bound).

### M19. A matching exactly returned mixed-state example

**Phase:** Narrative/innovation.

**Central question:** How can a maximally mixed helper mediate a phase gate while its marginal remains fixed?

**Understanding target:** Identify why the diagonal data blocks preserve $`I_C/2`$ at every time, while the off-diagonal block follows a rotating two-dimensional equation. Relate its exact channel to the inverse-action error for $`Z`$ and distinguish this matching example from an upper bound for every target unitary.

**Dependencies and story role:** M15, M17, and M18. Completes the mixed-return comparison for a specified nontrivial gate.

**Conceptual connection:** An unchanged local marginal can coexist with correlations that carry the gate's dynamics.

**Source pointers:** W&M §4.6 and A.2, through [exact mixed marginal return](ANCHOR_BRIDGE.md#exact-mixed-marginal-return); [exact two-dimensional equation](../science/mixed-controllers.md#exact-two-dimensional-equation) and [finite-action asymptotics](../science/mixed-controllers.md#finite-action-estimate-and-asymptotics).

### M20. A Hermitian exchange with a completion flag

**Phase:** Narrative/innovation.

**Central question:** What does one unobserved exchange between an unused flag and the initial flag accomplish?

**Understanding target:** Interpret the Hermitian jump that applies $`U`$ on a forward transition and $`U^\dagger`$ on the reverse transition. Obtain the stage's identity-versus-gate mixture and its action, while recognizing the backflow that prevents one fixed exchange from becoming a one-way absorbing transition.

**Dependencies and story role:** M03, M04, M07, and M12. Introduces the local primitive for changing the controller instead of returning it.

**Conceptual connection:** Completion is recorded in an orthogonal controller subspace within an unconditioned channel.

**Source pointers:** W&M §§3.6 and 4.2, through [consumed flags](ANCHOR_BRIDGE.md#consumed-flags); [one Hermitian stage](../science/consumed-controllers.md#1-one-hermitian-stage).

### M21. The exact channel of protected completion flags

**Phase:** Narrative/innovation.

**Central question:** Why do successive unobserved stages multiply the failure probability?

**Understanding target:** Explain the induction in which earlier success flags remain dark and the initial flag alone meets a fresh level. Track the full joint channel, its data–controller correlations, and its reference extension. Distinguish closeness to the gate tensored with a changed controller state from return to the supplied state.

**Dependencies and story role:** M02, M07, M08, and M20. Converts a single exchange into an exact complete-channel construction.

**Conceptual connection:** The schedule protects completed subspaces without measuring a flag or conditioning the next operation on an observed result.

**Source pointers:** W&M §1.4 and A.2, through [consumed flags](ANCHOR_BRIDGE.md#consumed-flags); [complete joint channel after all stages](../science/consumed-controllers.md#2-complete-joint-channel-after-all-stages).

### M22. Exponential accuracy with increasing dimension

**Phase:** Narrative/innovation.

**Central question:** Which resources grow in the exponential-error exchange construction?

**Understanding target:** Relate $`q^m`$ error, total action $`A=ma`$, and controller dimension $`D_C=m+1`$ at fixed stage action. Distinguish level count, encoded qubit width, and the complexity of selective target-dependent couplings. Limit the matching logarithmic-action statement to the specified exchange family.

**Dependencies and story role:** M10, M12, and M21. Turns the exact flag formula into a quantitative resource comparison with returned controllers.

**Conceptual connection:** A growing supply of protected completion levels yields exponential improvement under the same Hermitian-generator restriction.

**Source pointers:** W&M §§3.6 and 4.2, through [consumed flags](ANCHOR_BRIDGE.md#consumed-flags); [action, dimension, and locality](../science/consumed-controllers.md#3-action-dimension-and-locality) and [the stated optimality scope](../science/consumed-controllers.md#what-is-and-is-not-optimal-here).

### M23. Rotating transfer in a fixed flag pair

**Phase:** Narrative/innovation.

**Central question:** How can the failure of one flag transfer decrease with its allocated action?

**Understanding target:** Relate the rotating Hermitian transfer to the exact Bloch equation from M15. Identify its finite-action failure bound, its large-action behavior $`q(a)=\pi^2/(4a)+O(a^{-2})`$, and the flag coherence generated alongside the population transfer.

**Dependencies and story role:** M12, M15, and M20. Replaces the fixed-exchange primitive with a stage whose failure vanishes at large action.

**Conceptual connection:** Established rotating dephasing can be combined with completion flags to explore a different action–dimension tradeoff.

**Source pointers:** W&M §§3.7 and 4.6, through [fixed controller dimension](ANCHOR_BRIDGE.md#fixed-controller-dimension); [one rotating-dephasing stage](../science/fixed-dimension-controllers.md#one-rotating-dephasing-stage).

### M24. Coherences do not feed the active populations

**Phase:** Narrative/innovation.

**Central question:** Why does the product-failure formula survive when the flags have coherences?

**Understanding target:** Use the active/inactive block decomposition to distinguish autonomous diagonal evolution from cross-block damping. Track the exact joint-channel coherences and explain why they cannot alter later active populations. Extend the argument to a reference before taking the final controller trace.

**Dependencies and story role:** M02, M07, M21, and M23. Establishes the complete-channel identity required for the fixed-dimension result.

**Conceptual connection:** An exact block argument replaces an unjustified assumption that every intermediate controller state is a classical mixture.

**Source pointers:** W&M §1.4 and A.2, through [fixed controller dimension](ANCHOR_BRIDGE.md#fixed-controller-dimension); [cross-flag autonomy and the complete channel](../science/fixed-dimension-controllers.md#cross-flag-autonomy-and-the-complete-channel).

### M25. The qutrit separation and achieved error powers

**Phase:** Narrative/innovation.

**Central question:** Does improving the inverse-action exponent require a growing controller?

**Understanding target:** Connect equal action allocation and the exact product formula to the achieved $`O_U(A^{-(D_C-1)})`$ error at fixed dimension. Identify the qutrit coefficient $`s(U)\pi^4/4`$ multiplying $`A^{-2}`$ and compare this with the dimension-independent returned-controller converse. Keep these upper bounds separate from optimality claims.

**Dependencies and story role:** M14, M16, M22, and M24. Establishes a fixed-size separation and distinguishes it from the increasing-dimension exponential construction.

**Conceptual connection:** A three-level controller already changes the best established action–accuracy comparison when restoration of its supplied state is removed.

**Source pointers:** W&M §§3.6 and 4.6, through [fixed controller dimension](ANCHOR_BRIDGE.md#fixed-controller-dimension); [a fixed qutrit](../science/fixed-dimension-controllers.md#a-fixed-qutrit) and [the return converse](../science/return-law.md#finite-action-return-bound).

### M26. Entropy and the meaning of consumption

**Phase:** Narrative/innovation.

**Central question:** What resource distinction survives when the controller's final entropy is small?

**Understanding target:** Distinguish the exact geometric entropy of exchange flags from the pinching upper bound for rotating flags with input-dependent coherences. Relate bounded or vanishing entropy to a large defect from the initial state, and combine this with the maximally mixed-controller obstruction. Keep restoration costs separate from the stated generator action.

**Dependencies and story role:** M09, M18, M22, and M25. Integrates the constructions into a precise interpretation of the controller resource.

**Conceptual connection:** Initial nonuniformity and permission to change the supplied state enable the advantage; endpoint entropy alone does not characterize the return task.

**Source pointers:** W&M §3.8 and A.2, through [consumed flags](ANCHOR_BRIDGE.md#consumed-flags) and [fixed controller dimension](ANCHOR_BRIDGE.md#fixed-controller-dimension); [exchange-flag entropy](../science/consumed-controllers.md#4-entropy-of-the-changed-controller) and [entropy with coherences](../science/fixed-dimension-controllers.md#controller-entropy-with-input-dependent-coherences).

### M27. Analytical guarantees and numerical evidence

**Phase:** Narrative/innovation.

**Central question:** Which parts of the argument are checked numerically, and which require proof?

**Understanding target:** Relate direct master-equation integration to the reduced equations, exact channel identities, action normalization, and asymptotic coefficients. Distinguish numerical Choi-state comparisons from a general diamond-norm computation, and finite examples from universal statements about controller dimension, spectrum, or control schedules.

**Dependencies and story role:** M07, M16, M19, M21, and M24. Connects reproducible evidence to the analytical claims it corroborates.

**Conceptual connection:** Independent calculations can expose normalization or coherence errors while leaving the scope of a universal theorem to its proof.

**Source pointers:** W&M §§3.6 and 4.6, through [what the project adds](ANCHOR_BRIDGE.md#what-the-project-adds); [what is independently checked](../verification/README.md#what-is-independently-checked) and [fixed-dimension verification](../science/fixed-dimension-controllers.md#verification).

### M28. Inherited mechanisms and the additional statement

**Phase:** Narrative/innovation.

**Central question:** Which established ideas are combined, and what operational claim requires the present argument?

**Understanding target:** Separate prior Zeno gate mechanisms, motion–dissipation geometry, catalytic correlations, and completion flags from the return-sensitive complete-channel action comparison. Compare assumptions and objectives before treating two results as equivalent, and distinguish a proved contribution from an exhaustive priority claim.

**Dependencies and story role:** M13, M16, M19, M22, and M25. Places the assembled scientific result in its research context.

**Conceptual connection:** The significance lies in the quantified return promises under a common generator model, with established primitives credited as such.

**Source pointers:** W&M §§3.7 and 4.2, through [what the project adds](ANCHOR_BRIDGE.md#what-the-project-adds); [related work and contribution scope](../references/RELATED_WORK.md).

### M29. Boundaries of the established comparison

**Phase:** Narrative/innovation.

**Central question:** Which changes of promise or resources require a new theorem?

**Understanding target:** Locate the limits concerning approximate mixed return, general-target exact mixed-return upper bounds, fixed-dimension exponential accuracy, and unrestricted disposable converses. Recognize how Hamiltonian assistance, monitored stopping, resets, or uncharged coupling synthesis change the task, and why a generic no-jump branch need not implement the identity.

**Dependencies and story role:** M10, M18, M19, M22, M25, M26, and M28. Defines the boundary around the completed comparison and its remaining scientific questions.

**Conceptual connection:** An attainable scaling, a family-specific optimum, and a universal converse have different quantifiers and cannot be interchanged.

**Source pointers:** W&M §§3.6 and 4.2, through [what the project adds](ANCHOR_BRIDGE.md#what-the-project-adds); [established scope and remaining questions](../science/README.md#established-scope-and-remaining-questions) and [the disposable-converse limitation](../science/consumed-controllers.md#what-is-and-is-not-optimal-here).

### M30. The complete return-sensitive resource picture

**Phase:** Narrative/innovation.

**Central question:** What is established about accurate dissipative gates once the controller contract is specified?

**Understanding target:** Assemble the optimal pure joint-return order for every nontrivial target, the spectrum-independent exact mixed-return bound with a matching $`Z`$ example, and the consumed-controller upper bounds at fixed and increasing dimension. Interpret the comparison through complete-channel guarantees, explicit initial resources, entropy, attribution, and the unresolved frontiers.

**Dependencies and story role:** M16, M19, M22, and M25–M29, with their earlier dependencies. Integrates the narrative phase into the project's full scientific account.

**Conceptual connection:** Returning a controller is an operational requirement with a quantitative action cost. Allowing its supplied state to change permits faster established precision scaling under the same restricted dynamics, with the dimension and preparation assumptions kept explicit.

**Source pointers:** W&M §§1.4, 3.6, and A.2, through [what the project adds](ANCHOR_BRIDGE.md#what-the-project-adds); [the scientific synthesis](../science/README.md) and [three operational contracts](../science/consumed-controllers.md#5-three-operational-contracts).
