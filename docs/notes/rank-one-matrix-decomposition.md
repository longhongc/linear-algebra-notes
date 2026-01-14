# Decomposition of a Matrix into Rank-1 Matrices

## Overview

A **rank-1 matrix** is a matrix that can be written as an outer product

$$
u v^T
$$

where $u \in \mathbb{R}^m$ and $v \in \mathbb{R}^n$.
Such a matrix has rank at most 1.

A fundamental fact in linear algebra is:

> **Every matrix can be expressed as a sum of rank-1 matrices.**

This note summarizes the main ways to achieve such decompositions, their properties, and when each is useful.

---

## 1. Column-wise (Outer Product) Decomposition

Let $A \in \mathbb{R}^{m \times n}$ with columns $a_1, \dots, a_n$.

$$
A = \begin{bmatrix} a_1 & a_2 & \cdots & a_n \end{bmatrix}
$$

Then:

$$
A = \sum_{j=1}^n a_j e_j^T
$$

where $e_j$ is the $j$-th standard basis vector in $\mathbb{R}^n$.

- Each term $a_j e_j^T$ has rank at most 1.
- This decomposition always exists.

**Remarks**
- Simple and constructive.
- Not minimal.
- No orthogonality or optimality.

---

## 2. Rank Factorization

If $\operatorname{rank}(A) = r$, then there exist matrices

$$
U \in \mathbb{R}^{m \times r}, \quad V \in \mathbb{R}^{n \times r}
$$

such that

$$
A = U V^T
$$

Writing columns:

$$
U = [u_1, \dots, u_r], \quad V = [v_1, \dots, v_r]
$$

$$
A = \sum_{k=1}^r u_k v_k^T
$$

**Remarks**
- Uses the minimal possible number of rank-1 terms.
- Not unique.
- No orthogonality structure.

---

## 3. Singular Value Decomposition (SVD)

For any matrix $A \in \mathbb{R}^{m \times n}$,

$$
A = U \Sigma V^T
$$

where:
- $U = [u_1, \dots, u_r]$ has orthonormal columns,
- $V = [v_1, \dots, v_r]$ has orthonormal columns,
- $\Sigma = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$,
- $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$,
- $r = \operatorname{rank}(A)$.

This yields:

$$
A = \sum_{k=1}^r \sigma_k u_k v_k^T
$$

**Remarks**
- Canonical rank-1 decomposition.
- Rank-1 terms are orthogonal in Frobenius inner product.
- Provides best low-rank approximations (Eckart–Young theorem).
- Widely used in PCA, compression, and numerical linear algebra.

---

## 4. Symmetric Matrix Case (Eigen Decomposition)

If $A \in \mathbb{R}^{n \times n}$ is symmetric:

$$
A = Q \Lambda Q^T
$$

where:
- $Q = [q_1, \dots, q_n]$ is orthogonal,
- $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$.

Then:

$$
A = \sum_{k=1}^n \lambda_k q_k q_k^T
$$

**Remarks**
- Each term is rank 1 or zero.
- Special case of SVD for symmetric matrices.
- Closely tied to quadratic forms and energy decomposition.

---

## 5. Entry-wise Decomposition

Every matrix can be written as:

$$
A = \sum_{i=1}^m \sum_{j=1}^n A_{ij} e_i e_j^T
$$

**Remarks**
- Always valid.
- Uses $mn$ rank-1 matrices.
- Conceptually simple but inefficient.

---

## Comparison Summary

| Method | Always exists | Number of terms | Orthogonal | Optimal |
|------|---------------|-----------------|------------|----------|
| Entry-wise | Yes | $mn$ | No | No |
| Column-wise | Yes | $n$ | No | No |
| Rank factorization | Yes | $r$ | No | Minimal only |
| SVD | Yes | $r$ | Yes | Yes |
| Eigen (symmetric) | Yes | $\le n$ | Yes | Yes |

---

## Key Takeaways

- Every matrix can be decomposed into rank-1 matrices.
- The **rank** of the matrix determines the minimal number of rank-1 terms.
- The **SVD** provides the most structured, orthogonal, and optimal rank-1 decomposition.
- Different decompositions serve different purposes: theoretical clarity, computation, or approximation.

