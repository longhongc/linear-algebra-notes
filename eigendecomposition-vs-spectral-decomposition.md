# Eigendecomposition vs. Spectral Decomposition

This note clarifies the relationship between **eigendecomposition** and **spectral decomposition**, highlighting their similarities, differences, and the precise meaning of each term in linear algebra.

---

## Eigendecomposition

Let \( A \in \mathbb{C}^{n \times n} \) be a square matrix.

If \( A \) is **diagonalizable**, then it admits an eigendecomposition of the form

$$
A = V \Lambda V^{-1}
$$

where:
- \( \Lambda \) is a diagonal matrix whose entries are the eigenvalues of \( A \)
- \( V \) is a matrix whose columns are the corresponding eigenvectors

### Properties

- Eigenvalues may be **real or complex**
- Eigenvectors need **not** be orthogonal
- \( V \) is only required to be **invertible**
- Applies to any diagonalizable matrix (not necessarily symmetric or normal)

---

## Spectral Decomposition

Spectral decomposition is a **specialized form of eigendecomposition** that applies to matrices with additional structure.

### Real symmetric matrices

If \( A \in \mathbb{R}^{n \times n} \) is **symmetric**, then by the spectral theorem:

$$
A = Q \Lambda Q^T
$$

where:
- \( Q \) is an **orthogonal matrix**
- \( Q^T Q = I \)
- Columns of \( Q \) form an **orthonormal basis** of eigenvectors
- \( \Lambda \) contains **real eigenvalues**

### Complex Hermitian matrices

If \( A \in \mathbb{C}^{n \times n} \) is **Hermitian**, then:

$$
A = U \Lambda U^*
$$

where:
- \( U \) is **unitary**
- Eigenvalues are **real**
- Eigenvectors are **orthonormal**

---

## Conceptual Distinction

- **Eigendecomposition** emphasizes the algebraic factorization using eigenvalues and eigenvectors.
- **Spectral decomposition** emphasizes the structure of the spectrum and the existence of an **orthonormal eigenbasis**.

In linear algebra, the term *spectral decomposition* usually refers specifically to the decomposition guaranteed by the **spectral theorem**.

---

## Comparison Summary

| Aspect | Eigendecomposition | Spectral Decomposition |
|------|-------------------|------------------------|
| Applicability | Any diagonalizable matrix | Symmetric / Hermitian / normal matrices |
| Eigenvalues | Real or complex | Real (symmetric / Hermitian case) |
| Eigenvectors | Linearly independent | Orthonormal |
| Decomposition form | \( A = V \Lambda V^{-1} \) | \( A = Q \Lambda Q^T \) or \( A = U \Lambda U^* \) |

---

## Key Takeaways

- Every **spectral decomposition** is an **eigendecomposition**
- Not every **eigendecomposition** is a **spectral decomposition**
- The defining feature of spectral decomposition is the presence of an **orthonormal eigenbasis**
- Confusion often arises because applied fields use the term *spectral decomposition* more loosely

---

