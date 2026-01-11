# Geometric Meaning of Orthonormal Rows and Columns

## Statement

Let \( Q \in \mathbb{R}^{n \times n} \) be a square matrix.

If the **columns of $Q$** are orthonormal, then:
$$
Q^T Q = I
$$
which implies:
$$
Q^T = Q^{-1}
$$

A consequence is:
$$
Q Q^T = I
$$
so the **rows of $Q$** are also orthonormal.

At first glance, this is surprising: the rows generally point in different directions than the columns. Why must they also be orthonormal?

---

## Key Geometric Idea

The correct geometric interpretation comes from viewing $Q$ not as a collection of rows and columns, but as a **linear transformation**.

> A square matrix with orthonormal columns represents a **rigid motion** of space (a rotation or reflection).

---

## Columns: Forward Geometry

The columns of $Q$ are the images of the standard basis vectors:
$$
Q e_1, \dots, Q e_n
$$

If the columns are orthonormal, then:
- lengths are preserved
- angles are preserved

Formally:
$$
\langle Qx, Qy \rangle = \langle x, y \rangle
$$

Thus, $Q$ is an **isometry** of Euclidean space.

---

## Rows: Inverse Geometry

The rows of $Q$ are the columns of $Q^T$.

Since:
$$
Q^T = Q^{-1}
$$
the transpose represents the **inverse rigid motion**.

Rigid motions have rigid inverses:
- the inverse also preserves lengths
- the inverse also preserves angles

Therefore, the columns of $Q^T$ (i.e. the rows of $Q$) must form an orthonormal set.

---

## Why This Is Inevitable

A rigid motion must preserve inner products in *both* directions:
- forward transformation: $Q^T Q = I$
- backward transformation: $Q Q^T = I$

This forces:
- columns orthonormal
- rows orthonormal

There is no freedom for one without the other in the square case.

---

## Low-Dimensional Intuition

In 2D or 3D:
- columns show where the coordinate axes move after a rotation/reflection
- rows describe how to project back onto the original axes

Both sets must be perpendicular and unit length, or distances and angles would be distorted.

---

## One-Sentence Summary

A square matrix with orthonormal columns represents a rigid motion of space, and rigid motions have orthonormal coordinate systems in both the forward and inverse directions—so both columns and rows are necessarily orthonormal.

---

## Important Limitation

This result relies crucially on:
- the matrix being **square**

For rectangular matrices, orthonormal columns do **not** imply orthonormal rows.

---

