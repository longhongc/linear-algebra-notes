# Positive Definite Matrices vs Entry-wise Positivity

## Key Question
Does having all positive entries in a matrix imply it is **positive definite**?  
Does being **positive definite** imply all entries are positive?

**Answer:** No in both directions.

---

## Definition: Positive Definite Matrix

A real symmetric matrix $A \in \mathbb{R}^{n \times n}$ is **positive definite** if
$$
x^T A x > 0 \quad \text{for all } x \neq 0.
$$

This condition depends on the **quadratic form**, not on individual matrix entries.

---

## Positive Entries $\nRightarrow$ Positive Definite

A matrix can have all positive entries but still fail to be positive definite.

### Example
$$
A =
\begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix}
$$

- All entries are positive
- Eigenvalues are $3$ and $-1$

Since one eigenvalue is negative, $A$ is **not** positive definite.

**Insight:** Positive entries do not prevent directions where the quadratic form becomes negative.

---

## Positive Definite $\nRightarrow$ Positive Entries

A matrix can be positive definite even if some entries are negative.

### Example
$$
B =
\begin{pmatrix}
2 & -1 \\
-1 & 2
\end{pmatrix}
$$

- Eigenvalues are $1$ and $3$
- Hence $B$ is positive definite
- Off-diagonal entries are negative

**Insight:** Negative correlations between coordinates are allowed.

---

## Equivalent Characterizations (Real Symmetric Case)

For a real symmetric matrix $A$, the following are equivalent:

1. $x^T A x > 0$ for all $x \neq 0$
2. All eigenvalues of $A$ are positive
3. All leading principal minors are positive (Sylvester’s criterion)
4. $A = C^T C$ for some invertible matrix $C$

**None of these require entry-wise positivity.**

---

## Special Cases Where Positivity Helps

- **Diagonal matrix**:  
  Positive definite ⇔ all diagonal entries are positive
- **Diagonally dominant symmetric matrix with positive diagonal**:  
  Often positive definite, but still requires verification

---

## Summary

- Positive definiteness is a **global geometric property**
- Entry-wise positivity is a **local, coordinate-dependent property**
- Eigenvalues and quadratic forms—not individual entries—determine positive definiteness

---

## One-Line Takeaway

> Positive definite matrices are about **energy in all directions**, not about having all positive numbers.

