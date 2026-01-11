# Existence of Complex Eigenvalues and Their Meaning

## 1. Do eigenvalues always exist?

### Square matrices
Eigenvalues are defined only for **square matrices**.

For any \( n \times n \) matrix \( A \) (real or complex), when we work over the **complex numbers**:

- **Eigenvalues always exist**
- In fact, there are **exactly \( n \) complex eigenvalues**, counted with algebraic multiplicity

This is guaranteed by the **Fundamental Theorem of Algebra**.

### Real vs complex
- Over \( \mathbb{R} \): eigenvalues may fail to exist
- Over \( \mathbb{C} \): eigenvalues always exist

---

## 2. Why complex eigenvalues always exist (key theorem)

### Characteristic polynomial
Eigenvalues are defined as roots of the characteristic polynomial:
$$
p(\lambda) = \det(A - \lambda I)
$$

Facts:
- \( p(\lambda) \) is a polynomial of degree \( n \)
- Its coefficients are real or complex
- It is not the zero polynomial

### Fundamental Theorem of Algebra
Every degree-\( n \) polynomial with complex coefficients has **exactly \( n \) complex roots**, counting multiplicity.

Therefore:
$$
p(\lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2)\cdots(\lambda - \lambda_n)
$$
and each \( \lambda_i \in \mathbb{C} \) is an eigenvalue of \( A \).

---

## 3. Counting multiplicity

Eigenvalues must be counted with **algebraic multiplicity**.

Example:
$$
A =
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
$$

- Characteristic polynomial: \( (\lambda - 1)^2 \)
- One distinct eigenvalue, but **two eigenvalues counted with multiplicity**

So:
- Distinct eigenvalues \( \le n \)
- Total eigenvalues (with multiplicity) \( = n \)

---

## 4. Eigenvalues vs eigenvectors

Having \( n \) eigenvalues does **not** mean having \( n \) independent eigenvectors.

- Diagonalizable matrix: \( n \) independent eigenvectors
- Defective matrix: fewer eigenvectors than eigenvalues

This distinction is crucial in applications.

---

## 5. Real matrices and complex conjugate pairs

If \( A \in \mathbb{R}^{n \times n} \):

- Complex eigenvalues occur in **conjugate pairs**
$$
\lambda = \alpha + i\beta \quad \Rightarrow \quad \bar{\lambda} = \alpha - i\beta
$$
- The number of non-real eigenvalues is always even

---

## 6. Eigenvectors for complex eigenvalues

For a **real matrix**:
- Complex eigenvalues have **complex eigenvectors**
- No real eigenvector corresponds to a complex eigenvalue

Reason:
$$
A v = \lambda v
$$
If \( A \) and \( v \) are real but \( \lambda \) is complex, the equation is impossible.

---

## 7. Meaning for systems of differential equations

Consider:
$$
\dot{x} = A x
$$

### Always solvable
- Solutions always exist and are unique
- Even if no real eigenvalues exist

### Complex eigenvalues imply oscillation
If:
$$
\lambda = \alpha \pm i\beta
$$
then solutions involve:
$$
e^{\alpha t}(\cos \beta t, \sin \beta t)
$$

Interpretation:
- \( \beta \neq 0 \): oscillation / rotation
- \( \alpha < 0 \): decaying spiral (stable)
- \( \alpha = 0 \): pure oscillation (center)
- \( \alpha > 0 \): growing spiral (unstable)

---

## 8. Geometric intuition

- **Real eigenvectors** → invariant directions (straight-line motion)
- **Complex eigenvalues** → no invariant real direction
- Motion occurs in planes as **rotation or spiraling**

---

## Key takeaways

- Every \( n \times n \) matrix has **exactly \( n \) complex eigenvalues**, counting multiplicity
- Real eigenvalues are not guaranteed, complex ones are
- Complex eigenvalues correspond to oscillatory dynamics
- Eigenvalues existing does not imply diagonalizability
- Complex eigenvectors encode real rotational behavior through their real and imaginary parts

