"""Check the exact channel for consumed controllers of fixed dimension.

Run from the repository root with ``python verification/fixed_dimension.py``.
The callable ``run_checks()`` returns JSON-serializable results and writes no files.
"""

import json

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def _stage_coefficients(action):
    """Return the failure probability q and retained coherence b."""
    action = float(action)
    if action < 0:
        raise ValueError("Stage action must be nonnegative.")
    if action <= np.pi + 1:
        z, x = expm(np.array([[0.0, np.pi], [-np.pi, -2 * action]])) @ [1, 0]
        return float((1 - z) / 2), float(-x / 2)

    # Avoid cancellation in 1-z and overflow in exp(-a)*cosh(delta).
    delta = np.sqrt(action * action - np.pi**2)
    slow = np.pi**2 / (action + delta)
    correction = (
        np.pi**2
        / (2 * delta * (action + delta))
        * (-np.expm1(-2 * delta))
    )
    log_z = -slow + np.log1p(correction)
    q = -np.expm1(log_z) / 2
    b = np.pi * np.exp(-slow) * (-np.expm1(-2 * delta)) / (4 * delta)
    return float(q), float(b)


def _jump_parts(unitary, dimension, flag):
    basis = np.eye(dimension, dtype=complex)
    e0, ej = basis[:, 0], basis[:, flag]
    zz = np.outer(e0, e0.conj()) - np.outer(ej, ej.conj())
    transfer = (
        np.kron(unitary, np.outer(ej, e0.conj()))
        + np.kron(unitary.conj().T, np.outer(e0, ej.conj()))
    )
    return np.kron(I2, zz), transfer


def _integrate_joint(unitary, actions, input_rs):
    dimension = len(actions) + 1
    e0 = np.eye(dimension, dtype=complex)[:, 0]
    rho = np.kron(input_rs, np.outer(e0, e0.conj()))
    total_dimension = 4 * dimension
    for flag, action in enumerate(actions, start=1):
        zz, transfer = _jump_parts(unitary, dimension, flag)

        def rhs(s, vector):
            state = vector.reshape(total_dimension, total_dimension)
            jump_sc = np.cos(np.pi * s) * zz + np.sin(np.pi * s) * transfer
            jump = np.kron(I2, jump_sc)
            jump_squared = jump @ jump
            derivative = action * (
                jump @ state @ jump
                - (jump_squared @ state + state @ jump_squared) / 2
            )
            return derivative.reshape(-1)

        solution = solve_ivp(
            rhs,
            (0.0, 1.0),
            rho.reshape(-1),
            method="DOP853",
            atol=2e-12,
            rtol=2e-11,
        )
        if not solution.success:
            raise RuntimeError(solution.message)
        rho = solution.y[:, -1].reshape(total_dimension, total_dimension)
    return rho


def _exact_joint(unitary, actions, input_rs):
    """Evaluate the full joint expression, retaining every 0,j coherence."""
    dimension = len(actions) + 1
    basis = np.eye(dimension, dtype=complex)
    lifted_unitary = np.kron(I2, unitary)
    target_rs = lifted_unitary @ input_rs @ lifted_unitary.conj().T
    coefficients = [_stage_coefficients(a) for a in actions]
    qs = np.array([item[0] for item in coefficients])
    prefixes = np.concatenate(([1.0], np.cumprod(qs)))
    joint = prefixes[-1] * np.kron(input_rs, np.outer(basis[:, 0], basis[:, 0]))
    probabilities = [prefixes[-1]]
    for index, (q, b) in enumerate(coefficients):
        flag = index + 1
        weight = prefixes[index] * (1 - q)
        probabilities.append(weight)
        joint += weight * np.kron(target_rs, np.outer(basis[:, flag], basis[:, flag]))
        coherence = prefixes[index] * b * np.exp(-sum(actions[index + 1 :]) / 2)
        block_0j = np.outer(basis[:, 0], basis[:, flag])
        joint += coherence * np.kron(input_rs @ lifted_unitary.conj().T, block_0j)
        joint += coherence * np.kron(lifted_unitary @ input_rs, block_0j.conj().T)
    return joint, float(prefixes[-1]), np.array(probabilities), target_rs


def _entropy_bits(matrix):
    eigenvalues = np.linalg.eigvalsh((matrix + matrix.conj().T) / 2)
    positive = eigenvalues[eigenvalues > 0]
    return float(-np.sum(positive * np.log2(positive)))


def _check_generator_action(unitary):
    gamma = 0.37
    zz, transfer = _jump_parts(unitary, dimension=3, flag=2)
    rows = []
    for local_time in [0.0, 0.271, 1.0]:
        jump = np.sqrt(gamma) * (
            np.cos(np.pi * local_time) * zz + np.sin(np.pi * local_time) * transfer
        )
        identity = np.eye(jump.shape[0], dtype=complex)
        squared = jump @ jump
        generator = np.kron(jump.conj(), jump) - (
            np.kron(identity, squared) + np.kron(squared.T, identity)
        ) / 2
        strength = float(np.linalg.eigvalsh(-generator)[-1] / 2)
        defect = abs(strength - gamma)
        assert defect < 2e-12, (local_time, strength, gamma)
        rows.append(
            {
                "local_time": local_time,
                "gamma": gamma,
                "half_generator_norm": strength,
                "absolute_error": float(defect),
            }
        )
    return rows


def run_checks():
    """Run complete-channel, normalization, entropy, and asymptotic checks."""
    generic_unitary = expm(-0.5j * (0.71 * X + 0.37 * Y + 0.91 * Z))
    bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    input_rs = np.outer(bell, bell.conj())
    cases = [
        ("generic", generic_unitary, [1.0]),
        ("generic", generic_unitary, [10.0]),
        ("generic", generic_unitary, [3.0, 3.0]),
        ("generic", generic_unitary, [10.0, 10.0]),
        ("generic", generic_unitary, [30.0, 30.0]),
        ("generic", generic_unitary, [10.0, 10.0, 10.0]),
        ("generic", generic_unitary, [0.7, 4.0, 11.0]),
        ("Z", Z, [10.0, 10.0]),
    ]
    rows = []
    for label, unitary, actions in cases:
        dimension = len(actions) + 1
        observed = _integrate_joint(unitary, actions, input_rs)
        expected, failure, probabilities, target_rs = _exact_joint(
            unitary, actions, input_rs
        )
        tensor = observed.reshape(4, dimension, 4, dimension)
        output_rs = np.trace(tensor, axis1=1, axis2=3)
        controller = np.trace(tensor, axis1=0, axis2=2)
        expected_rs = failure * input_rs + (1 - failure) * target_rs
        full_defect = float(np.max(np.abs(observed - expected)))
        reduced_defect = float(np.max(np.abs(output_rs - expected_rs)))
        population_defect = float(np.max(np.abs(np.diag(controller) - probabilities)))
        trace_defect = float(abs(np.trace(observed) - 1))
        minimum_eigenvalue = float(
            np.linalg.eigvalsh((observed + observed.conj().T) / 2)[0]
        )
        controller_entropy = _entropy_bits(controller)
        positive = probabilities[probabilities > 0]
        diagonal_entropy = float(-np.sum(positive * np.log2(positive)))
        coherence_norm = float(
            np.linalg.norm(controller - np.diag(np.diag(controller)), ord="fro")
        )
        assert full_defect < 2e-9, (label, actions, full_defect)
        assert reduced_defect < 2e-9, (label, actions, reduced_defect)
        assert population_defect < 2e-9, (label, actions, population_defect)
        assert trace_defect < 2e-9, (label, actions, trace_defect)
        assert minimum_eigenvalue > -2e-9, (label, actions, minimum_eigenvalue)
        assert controller_entropy <= diagonal_entropy + 2e-9
        row = {
            "target": label,
            "stage_actions": actions,
            "controller_dimension": dimension,
            "total_action": float(sum(actions)),
            "failure_probability": failure,
            "full_choi_max_abs_error": full_defect,
            "reduced_choi_max_abs_error": reduced_defect,
            "controller_population_error": population_defect,
            "trace_error": trace_defect,
            "minimum_joint_eigenvalue": minimum_eigenvalue,
            "controller_entropy_bits": controller_entropy,
            "diagonal_entropy_bound_bits": diagonal_entropy,
            "controller_off_diagonal_frobenius_norm": coherence_norm,
        }
        if label == "Z":
            difference = output_rs - target_rs
            choi_trace_distance = float(
                np.sum(np.abs(np.linalg.eigvalsh((difference + difference.conj().T) / 2)))
                / 2
            )
            # The identity and Z normalized Choi states are orthogonal.
            assert abs(choi_trace_distance - failure) < 2e-9
            row["Z_normalized_choi_trace_distance"] = choi_trace_distance
        if len(set(actions)) == 1:
            q, _ = _stage_coefficients(actions[0])
            binary_entropy = -q * np.log2(q) - (1 - q) * np.log2(1 - q)
            geometric_entropy = binary_entropy * sum(q**k for k in range(len(actions)))
            assert abs(geometric_entropy - diagonal_entropy) < 2e-12
            row["geometric_entropy_formula_bits"] = float(geometric_entropy)
        rows.append(row)

    q_bound_rows = []
    for action in [0.01, 0.1, 1.0, float(np.pi), 10.0, 100.0, 1e4]:
        q, _ = _stage_coefficients(action)
        bound = min(1.0, np.pi**2 / (4 * action))
        assert 0 <= q <= bound + 2e-14, (action, q, bound)
        q_bound_rows.append({"action": action, "q": q, "upper_bound": float(bound)})

    coefficient = float(np.pi**4 / 4)
    asymptotic_rows = []
    for action in [1e3, 1e4, 1e5]:
        q, _ = _stage_coefficients(action / 2)
        scaled_error = action**2 * q**2
        relative_error = abs(scaled_error / coefficient - 1)
        asymptotic_rows.append(
            {
                "total_action": action,
                "A_squared_Z_error": float(scaled_error),
                "limiting_coefficient": coefficient,
                "relative_error": float(relative_error),
            }
        )
    assert asymptotic_rows[-1]["relative_error"] < 2e-4
    assert all(
        later["relative_error"] < earlier["relative_error"]
        for earlier, later in zip(asymptotic_rows, asymptotic_rows[1:])
    )

    return {
        "scope": "Fixed-dimensional consumed pure controllers; numerical checks of exact channel identities.",
        "complete_channel_cases": rows,
        "generator_action_normalization": _check_generator_action(generic_unitary),
        "stage_failure_bound": q_bound_rows,
        "qutrit_asymptotic_coefficient": asymptotic_rows,
        "maximum_full_choi_error": max(row["full_choi_max_abs_error"] for row in rows),
        "maximum_reduced_choi_error": max(row["reduced_choi_max_abs_error"] for row in rows),
        "all_checks_passed": True,
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, allow_nan=False))
