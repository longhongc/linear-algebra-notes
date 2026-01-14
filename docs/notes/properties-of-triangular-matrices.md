# Properties of Triangular Matrices

## Definition
A **triangular matrix** is a square matrix in which all entries on one side of the main diagonal are zero.

- **Upper triangular**: all entries below the diagonal are zero  
- **Lower triangular**: all entries above the diagonal are zero  

---

## Invertibility
A triangular matrix **does not always have an inverse**.

**Key fact**
A triangular matrix is invertible **if and only if all diagonal entries are nonzero**.

- If any diagonal entry is zero, the matrix is singular.
- If all diagonal entries are nonzero, the inverse exists and is triangular of the same type (upper or lower).

---

## Determinant
For a triangular matrix \( A \in \mathbb{R}^{n \times n} \),

$$
\det(A) = a_{11} a_{22} \cdots a_{nn}
$$

Consequences:
- The determinant is zero if and only if at least one diagonal entry is zero.
- Invertibility can be checked directly from the diagonal.

---

## Eigenvalues
The eigenvalues of a triangular matrix are **exactly its diagonal entries**, counted with algebraic multiplicity.

This holds even if the matrix is not diagonalizable.

---

## Solving Linear Systems
Triangular systems can be solved efficiently.

- Upper triangular systems are solved by **back substitution**
- Lower triangular systems are solved by **forward substitution**

This is why Gaussian elimination aims to transform matrices into triangular form.

---

## Rank
The rank of a triangular matrix equals the **number of nonzero diagonal entries**.

---

## Product of Triangular Matrices
- The product of two upper triangular matrices is upper triangular.
- The product of two lower triangular matrices is lower triangular.
- The diagonal entries of the product are the products of the diagonal entries.

---

## Powers of Triangular Matrices
If \( A \) is triangular, then \( A^k \) is also triangular for any positive integer \( k \).

The diagonal entries satisfy

$$
\operatorname{diag}(A^k) = (a_{11}^k, a_{22}^k, \dots, a_{nn}^k)
$$

---

## Special Case: Diagonal Matrices
Diagonal matrices are a special case of triangular matrices.

- All off-diagonal entries are zero
- Invertibility, determinant, eigenvalues, and powers are especially simple

---

## Summary
- Triangular matrices are easy to analyze because key properties depend only on the diagonal.
- A triangular matrix is invertible **if and only if** all diagonal entries are nonzero.
- Determinant, eigenvalues, rank, and powers can be read directly from the diagonal.
- Triangular form is fundamental in numerical linear algebra and matrix factorizations.

