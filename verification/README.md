# Reproducing the channel calculations

The universal lower bounds and complete-channel guarantees are analytical results. These scripts independently check the explicit dynamical constructions and the algebra used in their proofs. They do not optimize over arbitrary protocols or numerically certify a dimension-independent theorem.

## Run the checks

Use Python 3.12 or a compatible recent Python version. The recorded environment used NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8; exact versions are listed in [requirements.txt](requirements.txt). From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
python verification/plot_action.py
```

The first script exits with an error if a stated numerical comparison fails and writes [results.json](results.json). The plotting script regenerates [action-accuracy.svg](../figures/action-accuracy.svg), a PNG preview, and [action-accuracy.csv](action-accuracy.csv). All paths are resolved relative to the scripts, so the checks also work when invoked from another directory. The calculations use fixed inputs and a fixed random seed where randomized matrices are used.

## What is independently checked

| Calculation | Independent comparison | Scope |
|---|---|---|
| Pure returned helper | Direct integration of the laboratory Lindblad equation on a normalized reference–data–controller Choi state, compared with the helper Bloch transfer matrix and constant-frame solution | $`Z`$ and a generic qubit unitary, each at three stage durations; both stages and residual correlations are included |
| Exactly returned mixed helper | Direct integration of the complex controller block, compared with the two-dimensional real matrix exponential | Zero action and six positive actions; trace, positivity, and the exact controller marginal are checked |
| Consumed exchange flags | Exact constant-jump evolution in an eigenoperator basis, compared with the full geometric-flag Choi channel | Two target gates and four controller sizes, including ten stages |
| Fixed-dimensional rotating flags | Direct reference-extended Lindblad integration, compared with the full joint channel including flag coherences, the reduced mixture, and controller populations | A generic unitary with three Pauli components and $`Z`$, controller dimensions two through four, and eight cases including unequal stage actions |
| Purity geometry | Direct matrix calculations with noncommuting jumps and piecewise exact propagators; a separate weighted projection identity | Joint dimensions two, three, and six; mixed-controller weights include a small positive eigenvalue |

The pure-helper Choi half-trace distance is a finite diagnostic. In general, a normalized Choi-state trace distance is not the diamond distance. Its comparison with the analytical upper bound does not substitute for the reference-uniform proof in [pure-helper.md](../science/pure-helper.md).

For the mixed $`Z`$ gate and both consumed-controller families, the proofs identify the reduced channel as an explicit mixture of the identity and the target unitary. Their half-diamond errors then follow exactly by homogeneity of the norm; no numerical diamond-norm optimization is needed.

The [fixed_dimension.py](fixed_dimension.py) module contains the independent fixed-size calculation. It can also be run directly to print its results without changing other files. Singular mixed controller states are handled analytically by restricting to their invariant support. Numerical conditioning checks with small positive eigenvalues corroborate the weighted identity but do not replace that support argument.

## Recorded numerical accuracy

The recorded pure-helper direct-versus-reduced Choi residual is below $`5.2\times10^{-11}`$. The mixed-controller block residual is below $`7.5\times10^{-12}`$, and its returned marginal residual is zero at recorded precision. The exchange-flag full-channel formula residual is below $`8\times10^{-16}`$. The direct fixed-dimension comparisons agree with their reduced channel formula to below $`10^{-10}`$. Purity and weighted-projection identity residuals are below $`3\times10^{-16}`$. Exact per-case values are retained in [results.json](results.json).

These residuals depend on floating-point integration tolerances and library versions. The assertions allow modest numerical variation while remaining well below the gate errors in the tested cases. A passing run establishes consistency for those finite cases, not a proof of generality or an optimized physical implementation.

## Figure conventions

The action–accuracy plot uses the fixed target $`Z`$. The returned-controller lower curve is $`A\ge(1-\epsilon)^2/\epsilon`$. The mixed-return curve inverts its exact scalar error. The approximate pure joint-return curve is the sufficient bound $`A=(\pi^2+\pi)/\epsilon`$, rather than an exact minimum.

The qutrit curve has two equal rotating stages and inverts $`q(A/2)^2=\epsilon`$. The growing-flag curve uses exchange stages of action one and the smallest integer stage count meeting the error target. Its step structure is therefore real and its dimension is explicitly recorded in the CSV. The solid construction curves are achievable costs, not universal lower bounds for disposable controllers.

For large action the scalar solution is evaluated with a slow exponential rate and cancellation-resistant functions. This avoids overflow in a direct product of $`e^{-A}`$ and $`\cosh\sqrt{A^2-\pi^2}`$ and loss of precision when the error is small.
