# Stability via Trace and Determinant

This note explains how the **trace** and **determinant** of a matrix can be used to determine the stability of a linear dynamical system, with a focus on **2 × 2 systems**, where these quantities give complete qualitative information.

---

## 1. Problem Setup

Consider a linear system of differential equations

$$
\dot{x} = A x,
$$

where $A \in \mathbb{R}^{n \times n}$.

The equilibrium $x = 0$ is:

- **Asymptotically stable** if all eigenvalues of $A$ have strictly negative real parts
- **Unstable** if at least one eigenvalue has positive real part
- **Marginally stable** if eigenvalues have non-positive real parts and at least one has zero real part (no Jordan instability)

---

## 2. Trace and Determinant (2 × 2 Case)

Let

$$
A =
\begin{pmatrix}
a & b \\\\
c & d
\end{pmatrix}.
$$

Definitions:

$$
\operatorname{tr}(A) = a + d, 
\qquad
\det(A) = ad - bc
$$

---

## 3. Relationship to Eigenvalues

Let $\lambda_1, \lambda_2$ be the eigenvalues of $A$. Then:

$$
\lambda_1 + \lambda_2 = \operatorname{tr}(A),
\qquad
\lambda_1 \lambda_2 = \det(A)
$$

Thus:
- **Trace** controls the *sum* (average growth/decay rate)
- **Determinant** controls whether eigenvalues have the *same sign* or *opposite signs*

---

## 4. Characteristic Equation

For a 2 × 2 matrix:

$$
\lambda^2 - (\operatorname{tr}A)\lambda + \det(A) = 0
$$

Discriminant:

$$
\Delta = (\operatorname{tr}A)^2 - 4\det(A)
$$

- $\Delta > 0$: real eigenvalues
- $\Delta = 0$: repeated eigenvalues
- $\Delta < 0$: complex conjugate eigenvalues

---

## 5. Stability Classification (2 × 2 Systems)

| Condition | Stability Interpretation |
|---------|--------------------------|
| $\det(A) < 0$ | Unstable (saddle point) |
| $\det(A) > 0$, $\operatorname{tr}(A) < 0$ | Asymptotically stable |
| $\det(A) > 0$, $\operatorname{tr}(A) > 0$ | Unstable |
| $\det(A) > 0$, $\operatorname{tr}(A) = 0$ | Marginally stable (center if $\Delta < 0$) |
| $\det(A) = 0$ | Unstable or inconclusive |

---

## 6. Intuition

- **Negative trace**: average contraction of trajectories
- **Positive determinant**: eigenvalues have the same sign or are complex conjugates
- **Negative determinant**: eigenvalues have opposite signs → one expanding direction

Thus:
- Stability requires **both** contraction (negative trace) **and** no expanding direction (positive determinant).

---

## 7. Scope and Limitations

- The trace–determinant method is **complete only for 2 × 2 systems**
- For higher dimensions:
  - Trace and determinant alone are insufficient
  - Stability depends on the full eigenvalue spectrum
  - Other tools include eigenvalue analysis, Gershgorin disks, and Lyapunov methods

---

## 8. Key Takeaway

For 2 × 2 linear systems:

$$
\boxed{
\text{Stable} \iff \det(A) > 0 \;\text{and}\; \operatorname{tr}(A) < 0
}
$$

Trace measures **overall growth vs decay**,  
Determinant detects **directional instability**.

