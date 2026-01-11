# Why Positive Definiteness Is Not Meaningful for Unsymmetric Matrices

Positive definiteness is a concept that is fundamentally tied to **symmetric (or Hermitian)** matrices. Extending this notion directly to unsymmetric matrices is generally not meaningful. This note explains why.

---

## 1. Eigenvalues of Unsymmetric Matrices Can Be Complex

For a real symmetric matrix:
- All eigenvalues are real.
- Positivity of eigenvalues is well-defined and meaningful.

For a real **unsymmetric** matrix:
- Eigenvalues may be complex (often appearing in conjugate pairs).
- Complex numbers cannot be ordered, so the notion of “positive eigenvalues” loses meaning.

Thus, eigenvalue-based definitions of positive definiteness do not naturally extend to unsymmetric matrices.

---

## 2. Decomposition into Symmetric and Skew-Symmetric Parts

Any real square matrix \( A \) can be uniquely decomposed as
$$
A = S + K
$$
where
$$
S = \frac{A + A^T}{2} \quad \text{(symmetric)}, \qquad
K = \frac{A - A^T}{2} \quad \text{(skew-symmetric)}.
$$

For any vector \( x \),
$$
x^T K x = 0,
$$
so the quadratic form satisfies
$$
x^T A x = x^T S x.
$$

**Key consequence:**  
All quadratic-form-based notions of positivity depend **only on the symmetric part** \( S \), not on the full matrix \( A \).

Therefore, asking whether an unsymmetric matrix is positive definite is effectively the same as asking whether its symmetric part is positive definite.

---

## 3. Relation to Eigenvalues and Stability

If the symmetric part \( S \) is positive definite, then all eigenvalues \( \lambda \) of \( A \) satisfy
$$
\operatorname{Re}(\lambda) > 0.
$$

This is important in applications such as stability analysis of dynamical systems.

However:
- Eigenvalues of \( A \) may still be complex.
- Positive real parts do **not** imply real or positive eigenvalues.
- The converse is also false: positive real parts of eigenvalues do not imply \( S \) is positive definite.

Thus, positive definiteness of the symmetric part gives a **one-way guarantee** on the real parts of eigenvalues, not a full eigenvalue characterization.

---

## 4. Conceptual Takeaway

- Positive definiteness is inherently a **symmetric-matrix concept**.
- For unsymmetric matrices:
  - Eigenvalues may be complex.
  - Quadratic forms ignore the skew-symmetric part.
  - Meaningful positivity statements must refer to the symmetric part.

---

## Summary

- Unsymmetric matrices can have complex eigenvalues, making “positivity” ill-defined.
- Any matrix decomposes into symmetric and skew-symmetric parts.
- The skew-symmetric part contributes nothing to \( x^T A x \).
- Positive definiteness of the symmetric part implies positive real parts of eigenvalues, but not vice versa.
- Therefore, checking positive definiteness for an unsymmetric matrix is not meaningful unless explicitly interpreted through its symmetric part.

