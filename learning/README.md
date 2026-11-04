# Learning the cost of returning a controller

A dephasing process can move information when its dephasing basis changes. The scientific question here is what action that motion requires when it must implement a gate on an unknown input and also meet a specified controller-return condition.

This route connects that physical picture to the complete scientific account. It uses one educational anchor: **Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control*, Cambridge University Press, first published 2010**, ISBN 978-0-521-80442-4. The [official frontmatter and contents](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf) identify the edition and relevant sections. Section pointers refer to this edition; the local derivations are supplied in this repository.

## Choose a reading route

| Purpose | Begin here | Then follow |
|---|---|---|
| Connect the physical picture to the result | [Anchor bridge](ANCHOR_BRIDGE.md) | The scientific topic linked at each step |
| Build an organized understanding of the project | [30-milestone map](MILESTONES.md) | Earlier dependencies and the listed source pointers |
| Inspect a precise assumption or proof | [Scientific entry point](../science/README.md) | The pure-return law, matching construction, mixed-return law, or consumed-controller construction |
| Reproduce a calculation or inspect evidence | [Verification guide](../verification/README.md) | The independent channel checks, saved results, and figure generator |
| Assess what comes from earlier work | [Related-work comparison](../references/RELATED_WORK.md) | The relevant primary source and its stated comparison scope |

The bridge translates notation, introduces an explicit gate example, and supplies the steps between the textbook foundations and the project. The map contains exactly 30 project-defined understanding targets in two phases, background/preliminaries and narrative/innovation. Each phase progresses from local objects and mechanisms toward an integrated account. It maps the load-bearing ideas, while the scientific pages retain the full derivations and technical qualifications.

## Keep the operational promises separate

An initially pure controller must approximately return jointly with the gate output in the pure-return theorem. The mixed-controller theorem requires exact marginal return and permits final correlations. The consumed-controller constructions allow the supplied pure controller to change; a fixed qutrit and a growing flag register give different resource tradeoffs. The same error symbol therefore always carries its stated output contract.

Every gate guarantee concerns the complete channel, including input entanglement with an inert reference. A successful transfer of one state and a numerical Choi-state comparison alone do not establish that guarantee. The local proofs explain where the complete-channel statements enter.

The textbook is the single educational anchor. The [research bibliography](../references/references.bib) retains the primary literature needed to credit mechanisms and compare theorems; it is not an additional prerequisite reading list.

[Repository overview](../README.md) · [Scientific account](../science/README.md)
