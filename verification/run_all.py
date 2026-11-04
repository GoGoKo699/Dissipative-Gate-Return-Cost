#!/usr/bin/env python3
"""Finite checks of the channel formulas; the general bounds are proved in science/."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from numpy.linalg import eigvalsh, norm
from scipy.integrate import solve_ivp
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
P0 = np.diag([1, 0]).astype(complex)
P1 = I2 - P0
SIGMA = [X, Y, Z]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def half_trace_distance(a: np.ndarray, b: np.ndarray) -> float:
    delta = (a - b + (a - b).conj().T) / 2
    return float(np.abs(eigvalsh(delta)).sum() / 2)


def dissipator(f: np.ndarray, rho: np.ndarray) -> np.ndarray:
    square = f @ f
    return f @ rho @ f - (square @ rho + rho @ square) / 2


def generator(jumps: list[np.ndarray]) -> np.ndarray:
    d = len(jumps[0])
    eye = np.eye(d)
    out = np.zeros((d*d, d*d), dtype=complex)
    for f in jumps:
        square = f @ f
        out += np.kron(f.T, f) - (np.kron(square.T, eye) + np.kron(eye, square)) / 2
    return out


def hermitian_step(f: np.ndarray, rho: np.ndarray, duration: float) -> np.ndarray:
    """Exact constant-jump evolution in the jump's eigenbasis."""
    values, basis = np.linalg.eigh(f)
    matrix = basis.conj().T @ rho @ basis
    damping = np.exp(-duration * (values[:, None] - values[None, :])**2 / 2)
    return basis @ (matrix * damping) @ basis.conj().T


def bell(d: int) -> np.ndarray:
    v = np.eye(d).reshape(-1) / np.sqrt(d)
    return np.outer(v, v)


def reflection(u: np.ndarray, angle: float) -> np.ndarray:
    d = len(u)
    lowering = np.array([[0, 1], [0, 0]], dtype=complex)
    return (np.cos(2*angle) * np.kron(np.eye(d), Z)
            + np.sin(2*angle) * (np.kron(u, lowering.T)
                                  + np.kron(u.conj().T, lowering)))


def integrate_stage(u: np.ndarray, rho_rsc: np.ndarray, duration: float) -> np.ndarray:
    """Integrate the physical time-dependent equation, retaining a d-dimensional reference."""
    d = len(u)
    shape = rho_rsc.shape
    def rhs(t, vector):
        f = np.kron(np.eye(d), reflection(u, np.pi*t/(2*duration)))
        return dissipator(f, vector.reshape(shape)).reshape(-1)
    sol = solve_ivp(rhs, (0, duration), rho_rsc.reshape(-1),
                    method="DOP853", rtol=2e-11, atol=2e-12)
    require(sol.success, sol.message)
    return sol.y[:, -1].reshape(shape)


def helper_transfer_matrix(duration: float) -> np.ndarray:
    omega = np.pi / duration
    rotating = np.array([[-2, 0, -omega], [0, -2, 0], [omega, 0, 0]])
    final_frame = np.diag([-1, 1, -1])
    return final_frame @ expm(duration * rotating)


def apply_helper_map(rho: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """Apply a unital one-qubit map to the final tensor factor."""
    n = rho.shape[0] // 2
    tensor = rho.reshape(n, 2, n, 2)
    result = np.zeros_like(tensor)
    paulis = [I2, X, Y, Z]
    images = [I2] + [sum(matrix[k, j] * SIGMA[k] for k in range(3)) for j in range(3)]
    for a in range(n):
        for b in range(n):
            block = tensor[a, :, b, :]
            result[a, :, b, :] = sum(np.trace(p @ block) * image / 2
                                     for p, image in zip(paulis, images))
    return result.reshape(rho.shape)


def check_pure_helper() -> list[dict]:
    records = []
    for name, u in [("Z", Z), ("generic_qubit", expm(-0.37j*(X + 0.6*Z)))]:
        d = len(u)
        phi = bell(d)
        input_state = np.kron(phi, P0)
        w = np.kron(np.eye(d), P0) + np.kron(u, P1)
        wr = np.kron(np.eye(d), w)
        ur = np.kron(np.eye(d), u)
        ideal = np.kron(ur @ phi @ ur.conj().T, P0)
        for duration in [2.0, 8.0, 25.0]:
            transfer = helper_transfer_matrix(duration)
            tau = (I2 + sum(transfer[k, 2]*SIGMA[k] for k in range(3))) / 2
            frame_stage_one = wr @ np.kron(phi, tau) @ wr.conj().T
            frame_two_stage = apply_helper_map(frame_stage_one, transfer)
            direct_one = integrate_stage(u, input_state, duration)
            direct_two = integrate_stage(np.eye(d), direct_one, duration)
            residual = float(norm(frame_two_stage-direct_two))
            require(residual < 3e-8, f"Pure-helper Choi reduction failed: {residual}")
            require(abs(np.trace(direct_two)-1) < 1e-9, "Trace not preserved")
            require(eigvalsh((direct_two+direct_two.conj().T)/2).min() > -1e-9,
                    "Nonpositive Choi state")
            choi_distance = half_trace_distance(direct_two, ideal)
            stage_error = half_trace_distance(tau, P1)
            certified_bound = (np.pi**2+np.pi)/(2*duration)
            require(choi_distance <= 2*stage_error+2e-9, "Composition bound failed")
            require(2*stage_error <= certified_bound+1e-10, "Analytic finite-time bound failed")
            records.append({"gate": name, "stage_time": duration, "action": 2*duration,
                            "direct_vs_reduced_choi_residual": residual,
                            "normalized_choi_half_trace_distance": choi_distance,
                            "certified_joint_half_diamond_upper_bound": min(1.0, certified_bound)})
    return records


def mixed_z_error(action: float) -> float:
    """Stable exact reduced-channel error, including large-action cancellation control."""
    if action <= np.pi + 1:
        a = (expm(np.array([[0., np.pi], [-np.pi, -2*action]])) @ np.array([1., 0.]))[0]
        return float((1-a)/2)
    delta = np.sqrt(action*action-np.pi*np.pi)
    slow = np.pi*np.pi/(action+delta)
    correction = np.pi*np.pi/(2*delta*(action+delta)) * (-np.expm1(-2*delta))
    log_a = -slow + np.log1p(correction)
    return float(-np.expm1(log_a)/2)


def check_mixed_helper() -> list[dict]:
    records = []
    for action in [0., .3, 1., 3., 10., 30., 100.]:
        def rhs(s, vector):
            b = vector.reshape(2, 2)
            direction = np.cos(2*np.pi*s)*Z + np.sin(2*np.pi*s)*X
            return (action*(Z @ b @ direction-b)).reshape(-1)
        sol = solve_ivp(rhs, (0, 1), (I2/2).reshape(-1), method="DOP853",
                        rtol=2e-11, atol=2e-12)
        require(sol.success, sol.message)
        direct = sol.y[:, -1].reshape(2, 2)
        a, b = expm(np.array([[0., np.pi], [-np.pi, -2*action]])) @ np.array([1., 0.])
        predicted = -(a*I2 + b*1j*Y)/2
        residual = float(norm(direct-predicted))
        epsilon = mixed_z_error(action)
        require(residual < 3e-8, f"Mixed-controller block failed: {residual}")
        require(abs(epsilon-(1+np.trace(direct).real)/2) < 3e-9,
                "Reduced dephasing parameter mismatch")
        require(0 <= epsilon <= 1+1e-12, "Invalid dephasing probability")
        if action > 0:
            require(epsilon <= np.pi*np.pi/(4*action)+1e-12, "Mixed upper bound failed")
        # Reconstruct the full normalized Choi state from its four data blocks.
        choi = np.zeros((8, 8), dtype=complex)
        for r in range(2):
            for s in range(2):
                block = I2/2 if r == s else (direct if (r, s) == (0, 1) else direct.conj().T)
                ketbra = np.zeros((4, 4), dtype=complex)
                ketbra[2*r+r, 2*s+s] = .5
                choi += np.kron(ketbra, block)
        controller = np.trace(choi.reshape(4, 2, 4, 2), axis1=0, axis2=2)
        require(norm(controller-I2/2) < 1e-10, "Controller marginal changed")
        require(eigvalsh((choi+choi.conj().T)/2).min() > -1e-8, "Mixed Choi not positive")
        records.append({"action": action, "half_diamond_error": epsilon,
                        "action_times_error": action*epsilon, "block_residual": residual,
                        "controller_marginal_residual": float(norm(controller-I2/2))})
    return records


def check_consumed_helper() -> list[dict]:
    records = []
    for name, u in [("Z", Z), ("generic_qubit", expm(-0.37j*(X+0.6*Z)))]:
        d = len(u)
        phi = bell(d)
        ur = np.kron(np.eye(d), u)
        target = ur @ phi @ ur.conj().T
        for m in [1, 2, 5, 10]:
            dimension = m+1
            a = .8
            q = (1+np.exp(-2*a))/2
            initial_flag = np.zeros((dimension, dimension)); initial_flag[0, 0] = 1
            rho = np.kron(phi, initial_flag).astype(complex)
            predicted = (q**m*np.kron(phi, initial_flag)).astype(complex)
            for j in range(1, m+1):
                move = np.zeros((dimension, dimension)); move[j, 0] = 1
                f = np.kron(u, move) + np.kron(u.conj().T, move.T)
                rho = hermitian_step(np.kron(np.eye(d), f), rho, a)
                label = np.zeros_like(initial_flag); label[j, j] = 1
                predicted += (1-q)*q**(j-1)*np.kron(target, label)
            residual = float(norm(rho-predicted))
            require(residual < 2e-12, "Consumed-controller full-channel formula failed")
            reduced = np.trace(rho.reshape(d*d, dimension, d*d, dimension), axis1=1, axis2=3)
            expected = q**m*phi + (1-q**m)*target
            require(norm(reduced-expected) < 2e-12, "Reduced mixture failed")
            probabilities = np.array([q**m] + [(1-q)*q**(j-1) for j in range(1, m+1)])
            entropy = float(-np.sum(probabilities*np.log(probabilities)))
            bound = float((-q*np.log(q)-(1-q)*np.log(1-q))/(1-q))
            require(entropy <= bound+1e-12, "Flag entropy bound failed")
            if name == "Z":
                require(abs(half_trace_distance(reduced,target)-q**m) < 2e-12,
                        "Orthogonal Z witness error mismatch")
            records.append({"gate":name,"stages":m,"flag_dimension":dimension,"action":m*a,
                            "identity_weight":q**m,"choi_formula_residual":residual,
                            "flag_entropy_nats":entropy,"entropy_upper_bound_nats":bound})
    return records


def check_purity_geometry() -> dict:
    rng = np.random.default_rng(12917)
    largest_identity_residual = 0.
    smallest_margin = np.inf
    for d in [2, 3, 6]:
        v = rng.normal(size=d)+1j*rng.normal(size=d); v /= norm(v)
        start = np.outer(v,v.conj()); rho=start.copy(); action=0.
        for duration in [.17,.31,.13]:
            jumps=[]
            for _ in range(2):
                matrix=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
                f=(matrix+matrix.conj().T)/2; f/=norm(f,2); jumps.append(f)
            g=generator(jumps)
            velocity=sum(dissipator(f,rho) for f in jumps)
            purity_loss=sum(norm(f@rho-rho@f)**2 for f in jumps)
            residual=abs(2*np.trace(rho@velocity).real+purity_loss)
            largest_identity_residual=max(largest_identity_residual,float(residual))
            strength=float(eigvalsh(-g).max()/2)
            require(norm(velocity)**2 <= strength*purity_loss+1e-11,"Speed-purity bound failed")
            rho=(expm(g*duration)@rho.reshape(-1,order='F')).reshape(d,d,order='F')
            action+=strength*duration
        margin=action*(1-np.trace(rho@rho).real)-norm(rho-start)**2
        smallest_margin=min(smallest_margin,float(margin))
        require(margin >= -1e-10,"Integrated trajectory bound failed")
    require(largest_identity_residual < 1e-11,"Purity identity mismatch")
    # Independent singular-spectrum conditioning check for the weighted projection.
    projection_residual=0.
    for eigenvalue in [1e-6,.2,.5]:
        beta=np.diag([eigenvalue,1-eigenvalue]); inv=np.kron(I2,np.linalg.inv(beta))
        plus=np.array([1.,1.])/np.sqrt(2); start=np.kron(np.outer(plus,plus),beta)
        f=np.kron(X,P0)+np.kron((X+Z)/np.sqrt(2),P1)
        out=hermitian_step(f,start,.7)
        reduced=np.trace(out.reshape(2,2,2,2),axis1=1,axis2=3)
        proj=np.kron(reduced,beta)
        weighted=lambda x: float(np.trace(x.conj().T@inv@x).real)
        residual=abs(weighted(out)-weighted(out-proj)-np.trace(reduced@reduced).real)
        projection_residual=max(projection_residual,float(residual))
        require(residual < 1e-10,"Weighted partial-trace projection failed")
    return {"max_purity_identity_residual":largest_identity_residual,
            "minimum_integrated_bound_margin":smallest_margin,
            "max_weighted_projection_residual":projection_residual}


def main() -> None:
    from fixed_dimension import run_checks as check_fixed_dimension
    results={"scope":"Finite independent matrix/ODE checks; general claims are analytical proofs.",
             "pure_helper":check_pure_helper(),"mixed_helper":check_mixed_helper(),
             "consumed_helper":check_consumed_helper(),"purity_geometry":check_purity_geometry(),
             "fixed_dimension":check_fixed_dimension()}
    out=ROOT/'verification'/'results.json'
    out.write_text(json.dumps(results,indent=2)+'\n')
    print('PASS: pure-helper full Choi evolution, mixed-controller blocks, exchange flags, fixed-dimensional rotating flags, and purity geometry.')
    print('The pure-helper Choi distance is a finite diagnostic, not a numerical diamond-norm certificate.')
    print(f'Results written to {out.relative_to(ROOT)}')


if __name__=='__main__':
    main()
