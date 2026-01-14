# Sensitivity in Solving Linear Systems \( Ax = b \)

This note covers how small changes in the right-hand side vector \( b \) affect the solution \( x \) in a linear system \( Ax = b \), and how this sensitivity is quantified using condition numbers and matrix norms.

---

## Absolute vs. Relative Perturbations

To understand sensitivity, we compare the perturbation in the solution \( \delta x \) with that in the input \( \delta b \). A meaningful measure is the **relative change**:

$$
\frac{\|\delta x\|}{\|x\|} \quad \text{vs.} \quad \frac{\|\delta b\|}{\|b\|}
$$

The ratio of these two quantities describes how much the solution can change in response to a proportional change in the input.

---

## Symmetric Positive Definite Case

For symmetric positive definite (SPD) matrices \( A \), the sensitivity is governed by the eigenvalues of \( A \).

- Best-case amplification: governed by the largest eigenvalue \( \lambda_{\max} \)
- Worst-case amplification: governed by the smallest eigenvalue \( \lambda_{\min} \)

The **condition number** is defined as:

$$
\kappa(A) = \frac{\lambda_{\max}}{\lambda_{\min}}
$$

A large condition number indicates high sensitivity (ill-conditioning), meaning small changes in \( b \) can result in large changes in \( x \).

---

## Example: A Nearly Singular Matrix

Consider:

$$
A = \begin{bmatrix}
1 & 1 \\\\
1 & 1.0001
\end{bmatrix}
$$

This matrix has condition number:

$$
\kappa(A) \approx 4 \times 10^4
$$

Two right-hand sides:

- Unperturbed:  

$$
  \begin{cases}
  u + v = 2 \\\\
  u + 1.0001v = 2
  \end{cases}
  \quad \Rightarrow \quad u = 2, \ v = 0
$$

- Perturbed:  

$$
  \begin{cases}
  u + v = 2 \\\\
  u + 1.0001v = 2.0001
  \end{cases}
  \quad \Rightarrow \quad u = 1, \ v = 1
$$

Relative change in \( b \):

$$
\frac{\|\delta b\|}{\|b\|} = 10^{-4}
$$

Relative change in \( x \):

$$
\frac{\|\delta x\|}{\|x\|} = \frac{\|(-1, 1)\|}{\|(2, 0)\|} = \frac{\sqrt{2}}{2}
$$

Relative error ratio:

$$
\frac{\|\delta x\| / \|x\|}{\|\delta b\| / \|b\|} \approx 2 \times 10^4
$$

This illustrates how small input perturbations can lead to large output errors when the condition number is large.

---

## General (Unsymmetric) Case

For non-symmetric matrices, eigenvalues no longer accurately capture sensitivity. Instead, we use matrix norms.

### Operator Norm

The operator norm (induced 2-norm) is defined as:

$$
\|A\| = \max_{x \ne 0} \frac{\|Ax\|}{\|x\|}
$$

Squaring both sides:

$$
\|A\|^2 = \max_{x \ne 0} \frac{x^T A^T A x}{x^T x}
$$

This is a Rayleigh quotient, maximized by the eigenvector corresponding to the largest eigenvalue of \( A^T A \).

---

## Singular Values and General Condition Number

Let \( \sigma_{\max} \) and \( \sigma_{\min} \) denote the largest and smallest **singular values** of \( A \), respectively, defined as:

$$
\sigma_{\max} = \sqrt{\lambda_{\max}(A^T A)}, \quad
\sigma_{\min} = \sqrt{\lambda_{\min}(A^T A)}
$$

Then the **general condition number** is:

$$
\kappa(A) = \|A\| \cdot \|A^{-1}\| = \frac{\sigma_{\max}}{\sigma_{\min}}
$$

This condition number governs the worst-case relative sensitivity of the system \( Ax = b \), valid for any invertible matrix \( A \).

---

## Summary

- Relative sensitivity is more meaningful than absolute sensitivity.
- For SPD matrices, sensitivity is governed by the ratio of eigenvalues.
- For general matrices, use singular values to define the condition number.
- A large condition number implies the system is ill-conditioned and numerically unstable.


