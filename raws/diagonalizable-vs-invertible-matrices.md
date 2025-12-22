# Diagonalizable vs Invertible Matrices

This note clarifies the relationship between **diagonalizability** and **invertibility** for square matrices, correcting common misconceptions.

---

## Diagonalizability

### Definition
An \( n \times n \) square matrix \( A \) is **diagonalizable** if there exists an invertible matrix \( P \) and a diagonal matrix \( D \) such that
\[
A = P D P^{-1}.
\]

### Eigenvector Criterion
A matrix \( A \) is diagonalizable **if and only if** it has \( n \) **linearly independent eigenvectors**.

Equivalently:
- The eigenvectors of \( A \) form a basis of \( \mathbb{R}^n \) (or \( \mathbb{C}^n \)).
- The geometric multiplicity of each eigenvalue equals its algebraic multiplicity, and the total number of independent eigenvectors is \( n \).

---

## Invertibility

### Definition
A square matrix \( A \) is **invertible** if there exists a matrix \( A^{-1} \) such that
\[
A A^{-1} = A^{-1} A = I.
\]

### Eigenvalue Criterion
A matrix is invertible **if and only if**:
\[
0 \text{ is not an eigenvalue of } A.
\]

---

## Relationship Between Diagonalizability and Invertibility

### Key Facts

1. **Diagonalizable does NOT imply invertible**
   - A diagonalizable matrix may have zero eigenvalues.
   - Example:
     \[
     A = \begin{pmatrix}0 & 0 \\ 0 & 0\end{pmatrix}
     \]
     This matrix is diagonal (hence diagonalizable) but not invertible.

2. **Invertible does NOT imply diagonalizable**
   - A matrix can be invertible yet lack enough independent eigenvectors.
   - Example:
     \[
     A = \begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}
     \]
     This matrix is invertible, but not diagonalizable because it has only one independent eigenvector.

3. **Diagonalizable AND invertible**
   - A matrix is both diagonalizable and invertible **if and only if**:
     - It has \( n \) independent eigenvectors, and
     - None of its eigenvalues are zero.

---

## Summary Table

| Property | Requires |
|--------|---------|
| Diagonalizable | \( n \) independent eigenvectors |
| Invertible | No zero eigenvalues |
| Diagonalizable ⇒ Invertible | ❌ False |
| Invertible ⇒ Diagonalizable | ❌ False |
| Diagonalizable + no zero eigenvalues | ✅ Invertible |

---

## Conceptual Takeaway

- **Diagonalizability** is about having enough eigenvectors (a basis).
- **Invertibility** is about eigenvalues being nonzero.
- These are logically independent properties, though they may coincide in many important cases.

