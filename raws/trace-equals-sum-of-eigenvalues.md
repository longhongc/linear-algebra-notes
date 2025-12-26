# Trace Equals the Sum of Eigenvalues

## Core Statement

For any square matrix \( A \in \mathbb{R}^{n \times n} \) or \( \mathbb{C}^{n \times n} \),

\[
\operatorname{tr}(A) = \lambda_1 + \lambda_2 + \cdots + \lambda_n,
\]

where \( \lambda_1, \ldots, \lambda_n \) are the eigenvalues of \( A \), counted with **algebraic multiplicity**.

This result holds:
- for all dimensions \( n \),
- even if eigenvalues are complex,
- even if the matrix is **not diagonalizable**.

---

## Characteristic Polynomial View (Main Proof)

### Definition

The characteristic polynomial of \( A \) is
\[
p_A(\lambda) = \det(\lambda I - A).
\]

It is a degree-\(n\) polynomial.

---

### Expression via Eigenvalues

Over \( \mathbb{C} \), the polynomial factors as
\[
p_A(\lambda)
= (\lambda - \lambda_1)(\lambda - \lambda_2)\cdots(\lambda - \lambda_n).
\]

Expanding the highest-order terms:
\[
p_A(\lambda)
= \lambda^n
- (\lambda_1 + \cdots + \lambda_n)\lambda^{n-1}
+ \cdots
+ (-1)^n \lambda_1\cdots\lambda_n.
\]

---

### Expression via Matrix Invariants

From determinant expansion theory,
\[
p_A(\lambda)
= \lambda^n
- (\operatorname{tr} A)\lambda^{n-1}
+ \cdots
+ (-1)^n \det(A).
\]

This formula depends only on the matrix entries and is always valid.

---

### Coefficient Comparison

Since both expressions describe the same polynomial,
\[
\operatorname{tr}(A) = \lambda_1 + \cdots + \lambda_n,
\quad
\det(A) = \lambda_1 \cdots \lambda_n.
\]

---

## Diagonalizable Case (Intuition)

If \( A \) is diagonalizable,
\[
A = SDS^{-1}, \quad
D = \operatorname{diag}(\lambda_1,\dots,\lambda_n).
\]

Because trace is similarity-invariant,
\[
\operatorname{tr}(A) = \operatorname{tr}(D)
= \lambda_1 + \cdots + \lambda_n.
\]

The characteristic-polynomial proof shows this result remains true even when diagonalization fails.

---

## Key Takeaways

- Trace is the **first symmetric polynomial** of the eigenvalues.
- Determinant is the **last symmetric polynomial** of the eigenvalues.
- The trace–eigenvalue relationship is purely algebraic and does not rely on eigenvectors.
- This fact underlies many results in:
  - stability of differential equations,
  - matrix exponentials,
  - spectral analysis.

---

## Common Pitfalls

- The sum includes **multiplicity**, not just distinct eigenvalues.
- Real matrices may have complex eigenvalues; the sum is still real.
- Infinite eigenvectors do **not** affect the count—only eigenvalues matter.

---

## Summary Formula

\[
\boxed{
\operatorname{tr}(A)
= \sum_{i=1}^n \lambda_i
}
\]

