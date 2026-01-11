# Schur Decomposition and Unitary Triangularization

## Statement of the Result

Let \( A \in \mathbb{C}^{n \times n} \).  
There exists a **unitary matrix** \( U \) such that

$$
U^{-1} A U = U^\ast A U = T,
$$

where \( T \) is an **upper triangular matrix**.  
The diagonal entries of \( T \) are exactly the **eigenvalues of \( A \)**, counted with algebraic multiplicity.

This result is known as the **Schur decomposition**.

---

## Key Ideas

- Every complex square matrix has at least one eigenvalue.
- A unitary change of basis preserves inner products and numerical stability.
- By repeatedly isolating eigenvectors, the problem reduces to smaller subspaces.
- Similar matrices have the same eigenvalues.

---

## Step-by-Step Explanation

### 1. Start with an eigenvector

Since \( A \) is a complex matrix, it has an eigenvalue \( \lambda \) with eigenvector \( v \neq 0 \):

$$
A v = \lambda v.
$$

Normalize \( v \) so that \( \|v\| = 1 \).

---

### 2. Construct a unitary basis

Extend \( v \) to an orthonormal basis of \( \mathbb{C}^n \):

$$
\{ v, v_2, \dots, v_n \}.
$$

Let \( U \) be the unitary matrix whose columns are these basis vectors.

---

### 3. Apply the similarity transformation

Consider the transformed matrix:

$$
U^\ast A U.
$$

Because the first column of \( U \) is \( v \):

$$
U^\ast A v = U^\ast (\lambda v) = \lambda e_1,
$$

where \( e_1 = (1, 0, \dots, 0)^T \).

This forces the transformed matrix to have zeros below the first diagonal entry.

---

### 4. Reduction to a smaller matrix

The matrix now has the block form:

$$
U^\ast A U =
\begin{pmatrix}
\lambda & * \\
0 & B
\end{pmatrix},
$$

where \( B \in \mathbb{C}^{(n-1) \times (n-1)} \).

This step **reduces the problem** from dimension \( n \) to dimension \( n-1 \).

---

### 5. Induction

Apply the same argument to the smaller matrix \( B \):

- \( B \) has an eigenvalue
- Choose an eigenvector
- Perform a unitary change of basis inside the subspace

Repeating this process yields a fully upper triangular matrix.

---

## Resulting Form

After \( n \) steps, we obtain:

$$
T =
\begin{pmatrix}
\lambda_1 & * & \cdots & * \\
0 & \lambda_2 & \cdots & * \\
\vdots & \vdots & \ddots & * \\
0 & 0 & \cdots & \lambda_n
\end{pmatrix},
$$

where \( \lambda_1, \dots, \lambda_n \) are the eigenvalues of \( A \).

---

## Important Remarks

- The matrix \( A \) need **not** be diagonalizable.
- If \( A \) *is* diagonalizable with an orthonormal eigenbasis, then \( T \) is diagonal.
- Unitary similarity preserves eigenvalues but not necessarily eigenvectors.
- This decomposition always exists over \( \mathbb{C} \), but not necessarily over \( \mathbb{R} \).

---

## Common Pitfalls

- Confusing Schur decomposition with diagonalization.
- Assuming eigenvectors must be orthogonal (this is only true for normal matrices).
- Forgetting that the reduction step works on invariant subspaces.

---

## Summary

Every complex square matrix can be transformed via a unitary similarity into an upper triangular matrix.  
This is achieved by repeatedly isolating eigenvectors and reducing the problem to smaller-dimensional subspaces, ensuring that the eigenvalues appear along the diagonal.

