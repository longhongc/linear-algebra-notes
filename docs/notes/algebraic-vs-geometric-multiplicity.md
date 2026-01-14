# Algebraic vs Geometric Multiplicity of Eigenvalues

## 1. Eigenvalues and Eigenspaces

For a square matrix \( A \in \mathbb{R}^{n \times n} \):

- An **eigenvalue** \( \lambda \) satisfies

$$
  \det(A - \lambda I) = 0
$$

- The corresponding **eigenspace** is

$$
  E_\lambda = \ker(A - \lambda I)
$$

---

## 2. Algebraic Multiplicity

**Definition**

The **algebraic multiplicity** of an eigenvalue \( \lambda \) is the number of times \( \lambda \) appears as a root of the characteristic polynomial:

$$
\det(\lambda I - A)
$$

**Why “algebraic”?**
- Defined purely by algebraic objects: determinants and polynomials
- Ignores vector spaces and geometry

**Example**

If

$$
\det(\lambda I - A) = (\lambda - 2)^3(\lambda + 1),
$$

then the algebraic multiplicity of \( \lambda = 2 \) is **3**.

---

## 3. Geometric Multiplicity

**Definition**

The **geometric multiplicity** of an eigenvalue \( \lambda \) is:

$$
\dim \ker(A - \lambda I)
$$

i.e. the number of **linearly independent eigenvectors** associated with \( \lambda \).

**Why “geometric”?**
- Dimension measures the size of a vector space
- Counts independent directions, not individual vectors

---

## 4. Key Relationship

For any eigenvalue \( \lambda \):

$$
1 \le \text{geometric multiplicity} \le \text{algebraic multiplicity}
$$

### Explanation
- The lower bound comes from the definition of eigenvalue (at least one nonzero eigenvector exists).
- The upper bound comes from the structure of linear operators:
  - Algebraic multiplicity counts how many times \( \lambda \) appears in the characteristic polynomial.
  - Geometric multiplicity counts how many independent directions are fixed by \( A \).
  - A single direction cannot account for more geometric dimensions than allowed by the polynomial structure.

---

## 5. Infinite Eigenvectors vs Finite Dimension

A crucial distinction:

- A vector space can contain **infinitely many vectors**
- But still have **finite dimension**

### Example: Identity Matrix \( I_3 \)

- Eigenvalue: \( \lambda = 1 \)
- Characteristic polynomial:

$$
  \det(\lambda I - I_3) = (\lambda - 1)^3
$$

  - Algebraic multiplicity = 3

- Eigenspace:

$$
  \ker(I_3 - I_3) = \mathbb{R}^3
$$

  - Infinitely many eigenvectors
  - Dimension = 3
  - Geometric multiplicity = 3

**Key Insight**

Geometric multiplicity does **not** count eigenvectors.  
It counts **independent directions**.

---

## 6. Diagonalizability Connection

A matrix \( A \) is **diagonalizable** if and only if:

$$
\text{geometric multiplicity} = \text{algebraic multiplicity}
$$

for every eigenvalue.

If geometric multiplicity is smaller for some eigenvalue, the matrix is **defective**.

---

## 7. Common Pitfalls

- ❌ “Infinite eigenvectors implies infinite multiplicity”  
  → False: multiplicity depends on **dimension**, not cardinality.

- ❌ “Algebraic multiplicity means the maximum number of duplicates”  
  → False: it is the **actual root multiplicity**.

- ✔️ Always distinguish:
  - **how many times a root appears**
  - **how many independent eigen-directions exist**

---

## 8. Conceptual Summary

- **Algebraic multiplicity**: polynomial root count  
- **Geometric multiplicity**: eigenspace dimension  
- Infinite vectors can span a finite-dimensional space  
- Geometry is about directions, not quantity

