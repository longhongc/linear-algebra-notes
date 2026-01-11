# Similarity Invariance of Eigenvalues and Multiplicities

## Overview
In linear algebra, **similarity transformations** describe a change of basis.  
Two matrices that are similar represent the *same linear operator* under different coordinate systems.  
As a result, fundamental spectral properties—such as eigenvalues and their multiplicities—are preserved.

---

## Similarity Transformation
Two \( n \times n \) matrices \( A \) and \( B \) are **similar** if
$$
B = P^{-1} A P
$$
for some invertible matrix \( P \).

Similarity corresponds to rewriting a linear map in a different basis.

---

## Eigenvalues Are Invariant
Similarity preserves the characteristic polynomial:
$$
\det(\lambda I - B)
= \det(\lambda I - P^{-1} A P)
= \det(\lambda I - A)
$$

Therefore:
- \( A \) and \( B \) have the **same eigenvalues**
- with the **same algebraic multiplicities**

---

## Algebraic Multiplicity
**Definition:**  
The algebraic multiplicity of an eigenvalue \( \lambda \) is its multiplicity as a root of the characteristic polynomial.

**Invariance under similarity:**
Since the characteristic polynomial is unchanged, algebraic multiplicity is preserved.

---

## Geometric Multiplicity
**Definition:**  
The geometric multiplicity of an eigenvalue \( \lambda \) is
$$
\dim \ker(A - \lambda I)
$$

**Why it is preserved:**
If \( B = P^{-1} A P \), then
$$
\ker(B - \lambda I) = P^{-1} \ker(A - \lambda I)
$$

Thus:
- The eigenspaces are isomorphic
- Their dimensions are equal

So geometric multiplicity is invariant under similarity.

---

## Consequences

### Diagonalizability Is Preserved
A matrix is diagonalizable if and only if, for every eigenvalue,
$$
\text{geometric multiplicity} = \text{algebraic multiplicity}
$$

Since both multiplicities are similarity invariants:
- Either **all** similar matrices are diagonalizable
- Or **none**

