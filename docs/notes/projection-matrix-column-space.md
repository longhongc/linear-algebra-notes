# Projection Matrix onto the Column Space

## Definition

Let \( A \in \mathbb{R}^{m \times n} \) with **linearly independent columns**, so that \( A^T A \) is invertible.

The **projection matrix onto the column space of $A$** is

$$
P = A (A^T A)^{-1} A^T
$$

This matrix projects vectors in \( \mathbb{R}^m \) onto the column space of $A$.

---

## Action on a Vector

For any vector \( b \in \mathbb{R}^m \):

- The vector

$$
  p = Pb
$$

  is the **orthogonal projection of $b$** onto the column space \( C(A) \).

- The vector

$$
  e = b - Pb
$$

  is the **error (residual)**.

Thus,

$$
b = Pb + (b - Pb)
$$

---

## Orthogonal Decomposition

This decomposition is **orthogonal**:

- \( Pb \in C(A) \)
- \( (I - P)b \in N(A^T) \)

The column space and the left nullspace satisfy

$$
C(A) \perp N(A^T)
$$

So every vector \( b \) splits uniquely into two perpendicular components:

$$
\text{(column space component)} + \text{(orthogonal complement)}
$$

---

## The Matrix \( I - P \)

The matrix

$$
I - P
$$

is also a projection matrix:

- It projects onto \( N(A^T) \), the orthogonal complement of \( C(A) \)
- Its output is exactly the residual \( b - Pb \)

---

## Properties of the Projection Matrix

The projection matrix $P$ satisfies:

- **Idempotence**

$$
  P^2 = P
$$

- **Symmetry**

$$
  P^T = P
$$

These properties characterize orthogonal projection matrices.

---

## Geometric Interpretation

- \( Pb \) is the **closest vector in \( C(A) \)** to \( b \)
- The residual \( b - Pb \) is perpendicular to every column of $A$
- This construction underlies the **least squares method**

---

## Summary

The projection matrix

$$
P = A (A^T A)^{-1} A^T
$$

provides a matrix formula for decomposing any vector \( b \in \mathbb{R}^m \) into two perpendicular components:
- one in the column space \( C(A) \),
- one in the left nullspace \( N(A^T) \).

