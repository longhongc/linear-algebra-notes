# Solutions of Linear Difference and Differential Equations

This note explains how solutions of linear **difference equations** and **differential equations** arise from eigenvalues and eigenvectors, with a detailed derivation for the differential case.

---

## 1. Problem setup

Let \( A \in \mathbb{C}^{n \times n} \) be a constant matrix, and assume it is **diagonalizable**:
\[
A = S \Lambda S^{-1},
\]
where
- \( S \) is the matrix of eigenvectors,
- \( \Lambda = \mathrm{diag}(\lambda_1,\dots,\lambda_n) \) is the diagonal matrix of eigenvalues.

---

## 2. Discrete-time system (difference equation)

Consider the linear recurrence
\[
u_{k+1} = A u_k, \qquad u_0 \text{ given}.
\]

### Derivation
Iterating the recurrence:
\[
u_k = A^k u_0.
\]

Using diagonalization:
\[
A^k = (S \Lambda S^{-1})^k = S \Lambda^k S^{-1}.
\]

### Solution
\[
u_k = S \Lambda^k S^{-1} u_0.
\]

### Interpretation
- Each eigenvalue contributes a factor \( \lambda_i^k \).
- Modes with \( |\lambda_i| < 1 \) decay; modes with \( |\lambda_i| > 1 \) grow.
- Diagonalization decouples the system into independent modes.

---

## 3. Continuous-time system (differential equation)

Consider the linear ODE system
\[
\frac{du}{dt} = A u(t), \qquad u(0) \text{ given}.
\]

---

## 4. Change of variables (key step)

Define a new variable
\[
v(t) = S^{-1} u(t).
\]

Differentiate:
\[
\frac{dv}{dt} = S^{-1} \frac{du}{dt}.
\]

Substitute \( \frac{du}{dt} = A u \) and \( u = S v \):
\[
\frac{dv}{dt} = S^{-1} A S v.
\]

Since \( A = S \Lambda S^{-1} \),
\[
S^{-1} A S = \Lambda.
\]

Thus the system becomes
\[
\frac{dv}{dt} = \Lambda v.
\]

---

## 5. Solving the diagonal system

Because \( \Lambda \) is diagonal, the system decouples:
\[
\frac{dv_i}{dt} = \lambda_i v_i.
\]

Each scalar equation has solution
\[
v_i(t) = e^{\lambda_i t} v_i(0).
\]

In matrix form:
\[
v(t) = e^{\Lambda t} v(0),
\]
where
\[
e^{\Lambda t} =
\begin{pmatrix}
e^{\lambda_1 t} & & \\
& \ddots & \\
& & e^{\lambda_n t}
\end{pmatrix}.
\]

---

## 6. Transforming back to the original variables

Since \( u(t) = S v(t) \),
\[
u(t) = S e^{\Lambda t} v(0).
\]

Using \( v(0) = S^{-1} u(0) \), we obtain
\[
u(t) = S e^{\Lambda t} S^{-1} u(0).
\]

---

## 7. Matrix exponential viewpoint

The matrix exponential is defined by
\[
e^{At} = \sum_{k=0}^{\infty} \frac{(At)^k}{k!}.
\]

If \( A = S \Lambda S^{-1} \), then
\[
e^{At} = S e^{\Lambda t} S^{-1}.
\]

Hence the solution can be written compactly as
\[
u(t) = e^{At} u(0).
\]

---

## 8. Discrete vs continuous time: key analogy

\[
\Lambda^k \quad \longleftrightarrow \quad e^{\Lambda t}.
\]

- Difference equations use **powers** of eigenvalues.
- Differential equations use **exponentials** of eigenvalues.
- In both cases, diagonalization reveals independent dynamical modes.

---

## 9. Conceptual takeaway

- Eigenvectors define invariant directions of the dynamics.
- Along each eigenvector, the system behaves like a scalar equation:
  - \( x_{k+1} = \lambda x_k \) (discrete),
  - \( \dot{x} = \lambda x \) (continuous).
- The matrices \( S \) and \( S^{-1} \) simply change coordinates between physical space and eigenmode space.

---

## 10. Common pitfalls

- If \( A \) is **not diagonalizable**, Jordan blocks appear and extra polynomial factors multiply \( e^{\lambda t} \).
- Stability criteria differ:
  - Discrete time: \( |\lambda_i| < 1 \),
  - Continuous time: \( \mathrm{Re}(\lambda_i) < 0 \).

