# Orthogonal Matrices: Rotations, Reflections, and Permutations

## Definition
A real square matrix \( A \in \mathbb{R}^{n \times n} \) is **orthogonal** if

$$
A^T A = A A^T = I.
$$

Equivalently, the columns (and rows) of $A$ form an **orthonormal basis** of \( \mathbb{R}^n \).

---

## Fundamental Properties
- Inverse equals transpose:

$$
  A^{-1} = A^T
$$

- Length and angle preservation:

$$
  \|Ax\| = \|x\|, \quad (Ax)^T(Ay) = x^T y
$$

- Determinant:

$$
  \det(A) = \pm 1
$$

Orthogonal matrices represent **isometries** of Euclidean space.

---

## Orthogonal Matrices Are Not Only Rotations

A common misconception is that orthogonal matrices represent only rotations. In fact, they include several types of transformations.

---

## Rotation Matrices
- Preserve orientation
- Determinant:

$$
  \det(A) = +1
$$

Example (2D rotation):

$$
R =
\begin{bmatrix}
\cos\theta & -\sin\theta \\\\
\sin\theta & \cos\theta
\end{bmatrix}
$$

---

## Reflection Matrices
- Reflect space across a line or plane
- Reverse orientation
- Determinant:

$$
  \det(A) = -1
$$

Example (reflection across the $x$-axis):

$$
F =
\begin{bmatrix}
1 & 0 \\\\
0 & -1
\end{bmatrix}
$$

---

## Permutation Matrices
- Obtained by permuting rows (or columns) of the identity matrix
- Columns remain orthonormal, so the matrix is orthogonal
- Some permutations act as reflections

Example (swap coordinate axes):

$$
P =
\begin{bmatrix}
0 & 1 \\\\
1 & 0
\end{bmatrix}
$$

Properties:

$$
P^T = P^{-1}
$$

- Even permutations:

$$
  \det(P) = +1
$$

- Odd permutations:

$$
  \det(P) = -1
$$

Odd permutations correspond to **reflections**.

---

## Combined Transformations
An orthogonal matrix may represent:
- A pure rotation
- A pure reflection
- A permutation of axes
- A rotation combined with a reflection

Classification by determinant:

$$
\det(A) =
\begin{cases}
+1 & \text{rotation} \\\\
-1 & \text{reflection (possibly with rotation)}
\end{cases}
$$

---

## Key Takeaway
Orthogonal matrices are a broad class of transformations that:
- Preserve lengths and angles
- Include rotations, reflections, and permutations
- Are distinguished geometrically by the sign of their determinant

They describe **all rigid linear transformations** of Euclidean space.

