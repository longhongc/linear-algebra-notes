# Spectral Decomposition of Symmetric Matrices  
## Clarifying Orthogonality vs Orthonormality

---

## 1. Spectral (eigen) decomposition

For a real symmetric matrix $$A \in \mathbb{R}^{n \times n}$$, the spectral theorem states that

$$
A = Q \Lambda Q^\top
$$

where:
- $Q$ is **orthonormal**, meaning
  $$
  Q^\top Q = QQ^\top = I
  $$
- The columns of $$Q$$ are **orthonormal eigenvectors** of $$A$$
- $\Lambda$ is a **diagonal matrix** containing the real eigenvalues of $$A$$

---

## 2. Orthogonal vs orthonormal vectors

- **Orthogonal vectors** satisfy
  $$
  v_i^\top v_j = 0 \quad \text{for } i \neq j
  $$

- **Orthonormal vectors** satisfy
  $$
  v_i^\top v_j = \delta_{ij}
  $$

Orthonormality is strictly stronger than orthogonality.

---

## 3. A special property of orthonormal matrices

For an orthonormal matrix $$Q$$:

- Rows are orthonormal
- Columns are orthonormal
- **Row orthogonality is equivalent to column orthogonality**

This equivalence is special and does **not** hold for general matrices.

---

## 4. The source of confusion: multiplying by a diagonal matrix

Consider
$$
M = D Q^\top
$$
where $$D$$ is diagonal (e.g. an eigenvalue matrix).

### Effect on rows
- Left-multiplication by $$D$$ scales rows
- Row orthogonality is preserved

### Effect on columns
Column orthogonality is determined by
$$
M^\top M = Q D^2 Q^\top
$$
which is generally **not** the identity matrix.

Therefore, the columns of $$DQ^\top$$ are **not orthogonal in general**, even if the rows are.

---

## 5. Key logical correction

> Orthogonal rows do **not** imply orthogonal columns.

This implication holds **only** for orthonormal matrices such as $$Q$$.

---

## 6. Geometric intuition: diagonal scaling

A diagonal matrix performs **anisotropic scaling**:
- Different coordinate directions are scaled by different amounts
- Vector lengths change non-uniformly
- Angles are generally not preserved

Only matrices of the form
$$
D = c I
$$
(pure isotropic scaling) preserve orthogonality.

---

## 7. Why $$Q \Lambda Q^\top$$ is not diagonal

Interpret the decomposition as:
1. $Q^\top$: rotate into the eigenbasis
2. $\Lambda$: scale along eigen-directions
3. $Q$: rotate back to the original coordinates

The scaling occurs in a rotated coordinate system, so after rotating back, the result is symmetric but generally **not diagonal** unless $Q = I$.

---

## 8. Core takeaway

> The confusion arises from assuming that orthogonality of rows implies orthogonality of columns.  
> This equivalence holds only for orthonormal matrices like $Q$, not for matrices such as $DQ^\top$.

Understanding this distinction resolves the apparent contradiction in spectral decomposition.
