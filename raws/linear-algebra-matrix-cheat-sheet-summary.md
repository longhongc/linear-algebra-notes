# Linear Algebra Matrix Cheat Sheet — Quick Review

This note summarizes common matrix classes, their eigenvalue behavior, and standard decompositions. Use it as a fast conceptual reference.

---

## 1. Matrix Classes and Spectral Properties

### Symmetric (real)
- Definition: \( A^T = A \)
- Eigenvalues: real
- Eigenvectors: orthogonal
- Diagonalization: \( A = Q \Lambda Q^T \)

### Orthogonal
- Definition: \( Q^T = Q^{-1} \)
- Eigenvalues: \( |\lambda| = 1 \)
- Columns: orthonormal
- Interpretation: rotations / reflections

### Skew-symmetric
- Definition: \( A^T = -A \)
- Eigenvalues: purely imaginary or 0
- Eigenvectors: orthogonal (complex inner product)

### Hermitian (complex)
- Definition: \( \bar{A}^T = A \)
- Eigenvalues: real
- Eigenvectors: orthonormal
- Complex analogue of symmetric matrices

### Positive Definite
- Definition: \( x^T A x > 0 \) for all \( x \neq 0 \)
- Eigenvalues: strictly positive
- Automatically symmetric

---

## 2. Special Matrices

### Similar Matrices
- Form: \( B = M^{-1} A M \)
- Eigenvalues preserved: \( \lambda(B) = \lambda(A) \)
- Eigenvectors transformed by \( M^{-1} \)

### Projection
- Definition: \( P^2 = P = P^T \)
- Eigenvalues: \( 0, 1 \)
- Geometry: projects onto column space; nullspace is orthogonal complement

### Reflection
- Form: \( I - 2uu^T \), with \( \|u\| = 1 \)
- Eigenvalues: \( -1 \) (along \( u \)), \( +1 \) otherwise

### Rank-1 Matrix
- Form: \( uv^T \)
- Eigenvalues: \( v^T u \), others 0
- Eigenvectors: \( u \) and \( v^\perp \)

---

## 3. Eigenvalue Transformations

### Inverse
- \( A^{-1} \) has eigenvalues \( 1/\lambda(A) \)
- Eigenvectors unchanged

### Shift
- \( A + cI \) has eigenvalues \( \lambda + c \)
- Eigenvectors unchanged

---

## 4. Stability Criteria

### Discrete Stability
- \( A^n \to 0 \) if and only if \( |\lambda| < 1 \) for all eigenvalues

### Continuous Stability
- \( e^{At} \to 0 \) if and only if \( \mathrm{Re}(\lambda) < 0 \)

---

## 5. Special Structured Matrices

### Markov Matrices
- Properties: \( m_{ij} \ge 0 \), column sums = 1
- Largest eigenvalue: \( \lambda_{\max} = 1 \)
- Steady state: positive eigenvector

### Cyclic Permutation
- Property: \( P^n = I \)
- Eigenvalues: \( \lambda_k = e^{2\pi i k/n} \)
- Eigenvectors follow geometric progression

---

## 6. Matrix Decompositions

### Diagonalizable Matrices
- Form: \( A = S \Lambda S^{-1} \)
- Condition: \( n \) independent eigenvectors

### Symmetric Diagonalization
- Form: \( A = Q \Lambda Q^T \)
- Columns of \( Q \): orthonormal eigenvectors

### Jordan Form
- Form: \( A = M J M^{-1} \)
- Each Jordan block contributes one eigenvector
- Captures non-diagonalizable behavior

### Singular Value Decomposition (All Matrices)
- Form: \( A = U \Sigma V^T \)
- Rank: \( \mathrm{rank}(A) = \mathrm{rank}(\Sigma) \)
- \( V \): eigenvectors of \( A^T A \)
- \( U \): eigenvectors of \( A A^T \)

---

## Key Unifying Ideas

- **Eigenvalues describe behavior**, eigenvectors describe directions.
- **Symmetry ⇒ orthogonality ⇒ stability of diagonalization**.
- **Similarity preserves eigenvalues**, not eigenvectors.
- **SVD generalizes eigen-decomposition to all matrices**.

