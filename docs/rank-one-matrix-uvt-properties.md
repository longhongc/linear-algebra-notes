# Rank-1 Matrices of the Form \( A = u v^T \)

This note summarizes the key algebraic and geometric properties of rank-1 matrices of the form
$$
A = u v^T
$$
where $u, v \in \mathbb{R}^n$ (or $\mathbb{C}^n$) are nonzero vectors.

---

## 1. Rank, Column Space, and Row Space

- The matrix $A = u v^T$ has **rank 1** (provided $u \neq 0$ and $v \neq 0$).
- Every column of $A$ is a scalar multiple of $u$.

Therefore:
$$
\text{Col}(A) = \text{span}\{u\}
$$
$$
\text{Row}(A) = \text{span}\{v^T\}
$$

---

## 2. Action of $A$ on a Vector

For any vector $x$,
$$
Ax = u(v^T x)
$$

Interpretation:
- First take the inner product $v^T x$ (a scalar),
- then scale the vector $u$ by this scalar.

Thus, $A$ maps every vector into the direction of $u$.

---

## 3. Eigenvalues and Eigenvectors

### Nonzero Eigenvalue

Apply $A$ to $u$:
$$
Au = u(v^T u) = (v^T u)\,u
$$

So:
- $u$ is an eigenvector
- The corresponding eigenvalue is
$$
\lambda = v^T u
$$

If $v^T u \neq 0$, this is the **unique nonzero eigenvalue** of $A$.

---

### Zero Eigenvalue

Since $A$ has rank 1 in an $n$-dimensional space:
- The eigenvalue $0$ has multiplicity $n-1$.

The eigenspace corresponding to eigenvalue $0$ is:
$$
\{x : v^T x = 0\} = v^\perp
$$

---

## 4. Nullspace

The nullspace of $A$ is:
$$
\text{Null}(A) = \{x : Ax = 0\}
$$

From $Ax = u(v^T x)$, we get:
$$
Ax = 0 \iff v^T x = 0
$$

Therefore:
$$
\text{Null}(A) = v^\perp
$$

This is an $(n-1)$-dimensional subspace.

---

## 5. Special Case: Projection Matrix

If:
- $v = u$
- $u$ is a **unit vector**

then:
$$
A = uu^T
$$

This matrix is the **orthogonal projection** onto the line spanned by $u$.

### Properties
- Symmetric: $A^T = A$
- Idempotent: $A^2 = A$
- Eigenvalues:
  - $1$ with eigenvector $u$
  - $0$ with eigenspace $u^\perp$

In this case:
$$
\text{Null}(A) = u^\perp
$$

---

## 6. Conceptual Summary

- A rank-1 matrix collapses all vectors onto a single direction.
- The direction is determined by $u$ (column space).
- The nullspace is determined by orthogonality to $v$.
- The scalar interaction between $u$ and $v$ appears as the sole nonzero eigenvalue $v^T u$.
- When $u = v$ and $\|u\|=1$, the matrix becomes an orthogonal projector.

---

## 7. Common Pitfalls

- Saying “the nullspace is spanned by $v^\perp$” — instead, the nullspace **is** $v^\perp$.
- Forgetting that eigenvalue $0$ has multiplicity $n-1$.
- Assuming $u$ is always an eigenvector with nonzero eigenvalue (this fails if $v^T u = 0$).

---

