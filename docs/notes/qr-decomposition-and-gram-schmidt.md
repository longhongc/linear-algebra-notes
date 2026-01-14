# QR Decomposition and the Gram–Schmidt Process

## Overview

The **QR decomposition** factors a matrix into an orthonormal part and a triangular part.  
It is closely connected to the **Gram–Schmidt process**, which constructs an orthonormal basis from a set of linearly independent vectors.

This note explains:
- what QR decomposition is,
- how it is constructed,
- and how Gram–Schmidt naturally leads to the QR factorization.

---

## QR Decomposition

Let \( A \in \mathbb{R}^{m \times n} \) with linearly independent columns.

The **QR decomposition** is the factorization

$$
A = QR
$$

where:
- \( Q \in \mathbb{R}^{m \times n} \) has **orthonormal columns**,

$$
  Q^\top Q = I,
$$

- \( R \in \mathbb{R}^{n \times n} \) is **upper triangular** with positive diagonal entries.

---

## Interpretation

- The columns of \( A \) form some (generally non-orthogonal) basis of the column space.
- The columns of \( Q \) form an **orthonormal basis** of the same column space.
- The matrix \( R \) records how to express each column of \( A \) as a linear combination of the columns of \( Q \).

Thus, QR decomposition separates:
- **geometry** (orthonormal directions in \( Q \)),
- from **coordinates and scaling** (coefficients in \( R \)).

---

## Gram–Schmidt Process

The **Gram–Schmidt process** converts a linearly independent set of vectors into an orthonormal set spanning the same space.

Let the columns of \( A \) be

$$
A = [a_1 \; a_2 \; \cdots \; a_n].
$$

### Step 1: Orthogonalization

Define vectors \( u_k \) recursively:

$$
u_1 = a_1,
$$

$$
u_k = a_k - \sum_{j=1}^{k-1} \operatorname{proj}_{q_j}(a_k),
\quad k \ge 2,
$$

where

$$
\operatorname{proj}_{q_j}(a_k) = (q_j^\top a_k)\, q_j.
$$

Each \( u_k \) is orthogonal to all previous \( q_j \).

---

### Step 2: Normalization

Normalize each \( u_k \):

$$
q_k = \frac{u_k}{\|u_k\|}.
$$

The vectors \( q_1, \dots, q_n \) are:
- mutually orthogonal,
- of unit length,
- spanning the same subspace as \( a_1, \dots, a_n \).

These vectors form the columns of \( Q \).

---

## How \( R \) Appears

Each column \( a_k \) can be written as a linear combination of \( q_1, \dots, q_k \):

$$
a_k = \sum_{j=1}^k r_{jk} q_j,
$$

where

$$
r_{jk} = q_j^\top a_k.
$$

Properties of \( R \):
- \( r_{jk} = 0 \) for \( j > k \) (upper triangular),
- \( r_{kk} = \|u_k\| > 0 \).

Collecting all coefficients \( r_{jk} \) gives the matrix \( R \).

---

## Gram–Schmidt and QR: The Core Connection

- **Gram–Schmidt constructs \( Q \)** by orthonormalizing the columns of \( A \).
- **The projection coefficients produced by Gram–Schmidt form \( R \)**.
- Writing the result in matrix form gives:

$$
A = QR.
$$

$$
\boxed{\text{QR decomposition is Gram–Schmidt expressed in matrix form.}}
$$

---

## Remarks on Practice

- Classical Gram–Schmidt can be numerically unstable.
- Modified Gram–Schmidt improves stability.
- Householder reflections are commonly used in numerical software to compute QR reliably.

---

## Key Takeaways

- QR decomposition rewrites a matrix using an orthonormal basis.
- Gram–Schmidt explains *why* such a decomposition exists.
- \( Q \) captures orthogonality; \( R \) captures coordinates.
- QR is fundamental in least squares, numerical linear algebra, and eigenvalue algorithms.

