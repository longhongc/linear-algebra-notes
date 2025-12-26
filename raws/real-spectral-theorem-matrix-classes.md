# Real Spectral Theorem and Related Matrix Classes

This note summarizes which real matrices satisfy the **real spectral theorem**, and clarifies the roles of symmetric, skew-symmetric, and orthogonal matrices.

---

## 1. The Real Spectral Theorem

A real matrix \( A \in \mathbb{R}^{n \times n} \) satisfies the **real spectral theorem** if there exists a **real orthogonal matrix** \( Q \) such that
\[
Q^T A Q = \Lambda,
\]
where \( \Lambda \) is a **real diagonal matrix**.

Equivalently:
- All eigenvalues of \( A \) are real.
- There exists an orthonormal basis of eigenvectors in \( \mathbb{R}^n \).

---

## 2. Real Symmetric Matrices

### Definition
\[
A^T = A.
\]

### Properties
- All eigenvalues are real.
- Eigenvectors corresponding to distinct eigenvalues are orthogonal.
- There exists an orthonormal eigenbasis.

### Conclusion
\[
A = Q \Lambda Q^T
\]
with \( Q \) orthogonal and \( \Lambda \) real diagonal.

**This is the only class of real matrices that always satisfies the real spectral theorem.**

---

## 3. Real Skew-Symmetric Matrices

### Definition
\[
A^T = -A.
\]

### Eigenvalues
- Eigenvalues are purely imaginary or zero.
- Nonzero eigenvalues occur in conjugate pairs \( \pm i\lambda \).

### Consequences
- Cannot be diagonalized over \( \mathbb{R} \) unless \( A = 0 \).
- No real eigenbasis in general.

### What still holds
There exists an orthogonal matrix \( Q \) such that
\[
Q^T A Q =
\begin{bmatrix}
0 & -\lambda_1 & & \\
\lambda_1 & 0 & & \\
& & \ddots & \\
& & & 0
\end{bmatrix},
\]
a block-diagonal form with \(2 \times 2\) rotation blocks.

### Conclusion
- Orthogonally **block-diagonalizable**
- **Not** orthogonally diagonalizable over \( \mathbb{R} \)

---

## 4. Real Orthogonal Matrices

### Definition
\[
Q^T Q = I.
\]

### Eigenvalues
- All eigenvalues satisfy \( |\lambda| = 1 \).
- Possible eigenvalues:
  - \( \pm 1 \) (real)
  - \( e^{\pm i\theta} \) (complex conjugate pairs)

### Consequences
- May have no real eigenvectors.
- Cannot, in general, be diagonalized over \( \mathbb{R} \).

### Special case
If a real orthogonal matrix is also symmetric, then:
\[
Q^T = Q \quad \Rightarrow \quad Q^2 = I,
\]
and it *is* orthogonally diagonalizable with eigenvalues \( \pm 1 \).

### Conclusion
- Orthogonal matrices do **not** generally satisfy the real spectral theorem.
- Only the symmetric orthogonal ones do.

---

## 5. Summary Table

| Matrix Class | Real Eigenvalues | Orthonormal Eigenbasis (ℝ) | Orthogonal Diagonalization |
|-------------|-----------------|-----------------------------|----------------------------|
| Symmetric (\(A^T=A\)) | Yes | Yes | Yes |
| Skew-symmetric (\(A^T=-A\)) | No | No | No (block form only) |
| Orthogonal (\(A^T A=I\)) | Not always | Not always | No (in general) |
| Normal (real) | Not always | Not always | No (over ℝ) |

---

## 6. Key Takeaway

> Over the real numbers, **symmetry** — not normality — is the exact condition that guarantees the spectral theorem.

Normality guarantees diagonalization only over \( \mathbb{C} \); symmetry is required for diagonalization over \( \mathbb{R} \).

---

