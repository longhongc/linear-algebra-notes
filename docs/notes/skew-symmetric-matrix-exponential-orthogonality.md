# Skew-Symmetric Matrices and Orthogonality of the Matrix Exponential

## Statement

Let \( A \in \mathbb{R}^{n \times n} \) be a **skew-symmetric matrix**, meaning
$$
A^T = -A.
$$
Then for any \( t \in \mathbb{R} \), the matrix exponential
$$
e^{At}
$$
is an **orthogonal matrix**, i.e.
$$
(e^{At})^T e^{At} = I.
$$

---

## Key Definitions

- **Skew-symmetric matrix**:  
  A matrix \( A \) such that
$$
  A^T = -A.
$$

- **Orthogonal matrix**:  
  A matrix \( Q \) satisfying
$$
  Q^T Q = I.
$$

- **Matrix exponential**:
$$
  e^{At} = \sum_{k=0}^{\infty} \frac{(At)^k}{k!}.
$$

---

## Proof

Using basic properties of the matrix exponential:

1. Transpose of the exponential:
$$
   (e^{At})^T = e^{(At)^T}.
$$

2. Since \( A^T = -A \),
$$
   (At)^T = -At,
$$
   so
$$
   (e^{At})^T = e^{-At}.
$$

3. Multiply:
$$
   (e^{At})^T e^{At} = e^{-At} e^{At} = e^{0} = I.
$$

Thus, \( e^{At} \) is orthogonal.

---

## Intuition and Interpretation

- Skew-symmetric matrices generate **infinitesimal rotations**.
- The exponential map converts this infinitesimal generator into a **finite rotation**.
- Orthogonality means:
  - Vector lengths are preserved
  - Angles and inner products are preserved
- Therefore, the dynamical system
$$
  \dot{x}(t) = A x(t)
$$
  represents **pure rotation**, with no growth or decay.

---

## Consequences

- All eigenvalues of a real skew-symmetric matrix are **purely imaginary or zero**.
- The flow \( e^{At} \) is **norm-preserving**:
$$
  \| e^{At} x \| = \| x \|.
$$
- This property is fundamental in:
  - Rigid body dynamics
  - Hamiltonian systems
  - Lie group theory (Lie algebra of \( O(n) \))

---

## Common Pitfall

- Skew-symmetric \( A \) does **not** imply \( A \) is diagonalizable over \( \mathbb{R} \).
- Orthogonality of \( e^{At} \) holds **regardless** of diagonalizability.

---

## Summary

- Skew-symmetric matrices satisfy \( A^T = -A \).
- Their matrix exponentials are always orthogonal.
- Exponentiation turns infinitesimal rotations into finite rotations.
- This explains why such systems conserve energy and norms.

