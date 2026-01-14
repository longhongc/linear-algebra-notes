# The 2×2 Eigenvalue-Shift Identity and Column–Nullspace Relation

## Overview

For a $2\times2$ matrix $A$ with **distinct eigenvalues** $\lambda_1, \lambda_2$, a special and useful identity holds:

$$
(A - \lambda_1 I)(A - \lambda_2 I) = 0.
$$

This identity explains a textbook observation:

> The columns of $A - \lambda_1 I$ point in the direction of the eigenvector for $\lambda_2$, and vice versa.

This note explains **why** this happens and why it is special to $2\times2$ matrices.

---

## 1. Origin of the Identity

### Characteristic polynomial (2×2 case)

For a $2\times2$ matrix $A$,

$$
p(\lambda) = \lambda^2 - (\operatorname{tr}A)\lambda + \det A
= (\lambda - \lambda_1)(\lambda - \lambda_2).
$$

Thus,

$$
\lambda_1 + \lambda_2 = \operatorname{tr}A,
\quad
\lambda_1\lambda_2 = \det A.
$$

### Cayley–Hamilton theorem

Every square matrix satisfies its own characteristic polynomial:

$$
p(A) = A^2 - (\operatorname{tr}A)A + (\det A)I = 0.
$$

Substituting the eigenvalue expressions:

$$
A^2 - (\lambda_1 + \lambda_2)A + \lambda_1\lambda_2 I = 0.
$$

This factors as:

$$
(A - \lambda_1 I)(A - \lambda_2 I) = 0.
$$

---

## 2. Immediate Consequence

For any vector $v$,

$$
(A - \lambda_1 I)\big((A - \lambda_2 I)v\big) = 0.
$$

Therefore,

$$
\operatorname{Col}(A - \lambda_2 I) \subseteq \ker(A - \lambda_1 I).
$$

This is the key structural relationship.

---

## 3. Interpreting the Nullspace

By definition,

$$
\ker(A - \lambda_1 I) = E_{\lambda_1},
$$

the eigenspace corresponding to $\lambda_1$.

For a $2\times2$ matrix with **distinct eigenvalues**:

$$
\dim E_{\lambda_1} = 1.
$$

So the nullspace is a **one-dimensional line** spanned by the eigenvector $x_1$.

---

## 4. Rank and Column Space of $A - \lambda_2 I$

Since $\lambda_2$ is an eigenvalue:

$$
\det(A - \lambda_2 I) = 0,
$$

so $A - \lambda_2 I$ is singular.

In $2\times2$:

$$
\operatorname{rank}(A - \lambda_2 I) = 1.
$$

Thus,

$$
\dim \operatorname{Col}(A - \lambda_2 I) = 1.
$$

---

## 5. Why Containment Becomes Equality

We now have:

- $\operatorname{Col}(A - \lambda_2 I) \subseteq \ker(A - \lambda_1 I)$
- Both spaces are 1-dimensional

Therefore,

$$
\operatorname{Col}(A - \lambda_2 I) = \ker(A - \lambda_1 I).
$$

---

## 6. Consequence for the Columns

Because the column space is one-dimensional:

- Every column of $A - \lambda_2 I$ is a scalar multiple of the same vector
- That vector spans $\ker(A - \lambda_1 I)$
- Hence every column points in the direction of the eigenvector for $\lambda_1$

Symmetrically:
- Columns of $A - \lambda_1 I$ point in the direction of the eigenvector for $\lambda_2$

---

## 7. Geometric Intuition

In the plane:

- $A - \lambda_2 I$ collapses all vectors onto a single line
- $A - \lambda_1 I$ annihilates that line
- Dimension constraints force everything to align with the other eigenvector

---

## 8. Why This Is Special to 2×2

This phenomenon relies on:

- Degree-2 characteristic polynomial
- Rank–nullity forcing rank = 1
- One-dimensional eigenspaces

In higher dimensions:
- Nullspaces can have dimension greater than 1
- Columns need not align
- The clean “eigenvector swap” property fails

---

## Key Takeaway

For a $2\times2$ matrix with distinct eigenvalues,

$$
(A - \lambda_1 I)(A - \lambda_2 I) = 0
$$

forces the column space of one eigenvalue shift to coincide with the eigenspace of the other.  
This dimensional constraint explains why eigenvectors appear directly in the columns when computing them.

