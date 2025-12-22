# Properties of $A^T A$: Symmetry and Positive (Semi-)Definiteness

This note summarizes key structural properties of matrices of the form $A^T A$ for real matrices $A$, focusing on symmetry, positive semidefiniteness, and the condition for positive definiteness.

---

## Symmetry of $A^T A$

Let $A \in \mathbb{R}^{m \times n}$.

We have
$$
(A^T A)^T = A^T (A^T)^T = A^T A.
$$

Therefore:

- $A^T A$ is always a **symmetric matrix**.

This holds for all real matrices $A$, regardless of rank or shape.

---

## Positive Semidefiniteness of $A^T A$

For any vector $x \in \mathbb{R}^n$,
$$
x^T A^T A x = (Ax)^T (Ax) = \|Ax\|^2 \ge 0.
$$

Thus:

- $A^T A$ is always **positive semidefinite**.

This follows directly from the nonnegativity of squared Euclidean norms.

---

## Characterization of Positive Definiteness

A symmetric matrix $M$ is **positive definite** if
$$
x^T M x > 0 \quad \text{for all } x \neq 0.
$$

Applying this to $A^T A$:
$$
x^T A^T A x = \|Ax\|^2 > 0 \quad \text{for all } x \neq 0
$$
if and only if
$$
Ax = 0 \Rightarrow x = 0.
$$

This condition is equivalent to:

- The **columns of $A$ are linearly independent**
- $A$ has **full column rank**
- $\operatorname{null}(A) = \{0\}$

Hence:

- $A^T A$ is **positive definite if and only if $A$ has full column rank**

---

## Summary

- $A^T A$ is always **symmetric**
- $A^T A$ is always **positive semidefinite**
- $A^T A$ is **positive definite** if and only if the **columns of $A$ are linearly independent**
- If the columns are linearly dependent, then $A^T A$ is positive semidefinite but **not** positive definite

---

## Common Pitfall

- The condition for positive definiteness depends on the **column space** of $A$, not the row space.
- Row rank equals column rank in dimension, but positive definiteness of $A^T A$ is governed specifically by the null space of $A$.
