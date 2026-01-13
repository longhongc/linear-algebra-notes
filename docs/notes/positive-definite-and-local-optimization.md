# Positive Definite and Local Optimization

## Stationary Points and Derivative Tests

To determine the nature of a point in multivariable functions:

- **First-order condition**: A point \( \mathbf{x}_0 \) is a stationary point if
  $$
  \nabla f(\mathbf{x}_0) = 0
  $$
- **Second-order condition**: The behavior near a stationary point is determined by the second derivative (the Hessian matrix).

## Justifying the Use of Quadratic Approximation

- The function \( F \) may have higher-order or nonlinear terms (e.g. trigonometric terms).
- A simpler quadratic function \( f \) can be used to analyze local behavior because:
  - **Lower-order terms vanish** at the stationary point.
  - **Higher-order terms** do not affect the local behavior significantly.
- Thus, the **quadratic part of the Taylor expansion** governs the local nature of \( F \) near the stationary point.

## General Quadratic Form in Two Variables

Given:
$$
f(x, y) = ax^2 + 2bxy + cy^2
$$

The conditions for local behavior are:

- If \( a > 0 \) and \( ac - b^2 > 0 \): local **minimum**
- If \( ac - b^2 = 0 \): **valley** (flat direction)
- If \( ac - b^2 < 0 \): **saddle point**

## Matrix Representation and Generalization

The quadratic form can be written as:
$$
f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}, \quad A = \begin{bmatrix} a & b \\\\ b & c \end{bmatrix}
$$

This approach generalizes to higher dimensions.

- The matrix \( A \) is symmetric.
- The definiteness of \( A \) determines the nature of the stationary point.

## Definiteness and Optimization

- **Positive definite** \( \Rightarrow \) strict local **minimum**
- **Negative definite** \( \Rightarrow \) strict local **maximum**
- **Indefinite** \( \Rightarrow \) **saddle point**
- **Semidefinite** \( \Rightarrow \) possibly a **valley**; further analysis needed

## Taylor Expansion in Matrix Form

Second-order Taylor expansion at \( \mathbf{x}_0 \):
$$
f(\mathbf{x}) \approx f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T (\mathbf{x} - \mathbf{x}_0) + \frac{1}{2} (\mathbf{x} - \mathbf{x}_0)^T H (\mathbf{x} - \mathbf{x}_0)
$$

- At stationary points, the gradient term vanishes.
- The behavior is governed by the Hessian matrix \( H \).

## Local Analysis at Arbitrary Points

Even if the stationary point is not at the origin, shifting coordinates allows the same analysis to apply. The local behavior around any point reduces to analyzing a quadratic form centered at the origin.

## When Second Derivatives Are Inconclusive

If the **quadratic part is singular** (e.g., semidefinite Hessian with zero eigenvalues), the second-order test is **inconclusive**.

> In such cases, **third-order derivatives** (or higher) may be needed to determine the nature of the stationary point.

This includes semidefinite cases, where the Hessian is not invertible and flat directions exist.

## Summary

- The concept of **positive definiteness** of a matrix is fundamental in determining whether a stationary point is a local minimum.
- Analyzing the **quadratic part** of the function suffices for local analysis.
- This bridges linear algebra (quadratic forms, definiteness) and multivariable calculus (optimization).

