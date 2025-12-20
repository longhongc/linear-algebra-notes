# LU Decomposition with Pivoting

## Overview
LU decomposition factors a square matrix into the product of a **lower triangular** matrix and an **upper triangular** matrix.  
In general, **row permutations are required** to guarantee existence.

The standard and universally valid form is the **LU decomposition with pivoting**.

---

## Standard Form
For any square matrix \( A \in \mathbb{R}^{n \times n} \), there exists a **permutation matrix** \( P \), a **lower triangular** matrix \( L \), and an **upper triangular** matrix \( U \) such that
\[
PA = LU.
\]

Equivalently, since permutation matrices satisfy \( P^{-1} = P^T \),
\[
A = P^T L U.
\]

---

## Components
### Permutation Matrix \( P \)
- Obtained by row swaps
- Orthogonal matrix: \( P^T P = I \)
- Encodes **row pivoting** during Gaussian elimination

### Lower Triangular Matrix \( L \)
- Lower triangular
- Typically **unit lower triangular** (diagonal entries equal to 1)
- Stores the multipliers used during elimination

### Upper Triangular Matrix \( U \)
- Upper triangular
- Contains the pivots and the transformed system

---

## Existence
### With Pivoting
- **Always exists** for every square matrix
- Guaranteed by Gaussian elimination with row swaps
- Handles zero or small pivots safely

### Without Pivoting
An LU decomposition of the form
\[
A = LU
\]
(with no permutation matrix) **does not always exist**.

A sufficient condition for existence without pivoting is:
- All **leading principal minors** of \( A \) are nonzero  
  (equivalently, no zero pivots occur during elimination).

---

## Interpretation
LU decomposition corresponds exactly to Gaussian elimination:
- \( P \): records row swaps
- \( L \): records elimination steps
- \( U \): resulting echelon form

---

## Summary
- The decomposition \( PA = LU \) **always exists** for square matrices
- Row pivoting is essential for general matrices
- The form \( A = LU \) requires additional conditions and is not guaranteed

This makes **LU with pivoting** one of the most fundamental and reliable matrix factorizations in numerical linear algebra.

