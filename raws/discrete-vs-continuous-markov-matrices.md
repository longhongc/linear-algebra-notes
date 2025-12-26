# Discrete and Continuous Markov Matrices

This note explains the relationship between **discrete-time Markov matrices** and **continuous-time Markov matrices**, focusing on column sums, eigenvalues, and steady-state behavior.

---

## 1. Discrete-Time Markov Matrices

A matrix \( A \in \mathbb{R}^{n \times n} \) is a **discrete Markov matrix** if:

1. All entries are nonnegative:
   \[
   A_{ij} \ge 0
   \]
2. Each column sums to one:
   \[
   \sum_i A_{ij} = 1 \quad \text{for all } j
   \]

### Key Consequences
- The vector of all ones satisfies
  \[
  \mathbf{1}^T A = \mathbf{1}^T
  \]
- Therefore, \( \lambda = 1 \) is an eigenvalue of \( A \)
- By Perron–Frobenius theory, this eigenvalue is the **maximum eigenvalue**:
  \[
  \lambda_{\max} = 1
  \]

### Difference Equation
The discrete-time evolution is
\[
x_{k+1} = A x_k
\]
The steady-state mode corresponds to the term
\[
1^k
\]
which remains constant as \( k \to \infty \).

---

## 2. Continuous-Time Markov Matrices

A matrix \( B \in \mathbb{R}^{n \times n} \) is a **continuous Markov matrix** (or generator matrix) if:

1. Off-diagonal entries are nonnegative:
   \[
   B_{ij} \ge 0 \quad (i \ne j)
   \]
2. Each column sums to zero:
   \[
   \sum_i B_{ij} = 0 \quad \text{for all } j
   \]

### Key Consequences
- The vector of all ones satisfies
  \[
  \mathbf{1}^T B = 0
  \]
- Therefore, \( \lambda = 0 \) is an eigenvalue of \( B \)
- This eigenvalue is the **maximum eigenvalue**:
  \[
  \lambda_{\max} = 0
  \]

### Differential Equation
The continuous-time evolution is
\[
\frac{dx}{dt} = Bx
\]
The steady-state mode corresponds to
\[
e^{0t} = 1
\]
which remains constant for all time.

---

## 3. Relationship Between Discrete and Continuous Markov Matrices

A matrix \( A \) is a **discrete Markov matrix if and only if**
\[
B = A - I
\]
is a **continuous Markov matrix**.

### Explanation
- Subtracting the identity shifts all eigenvalues by \(-1\):
  \[
  \lambda(B) = \lambda(A) - 1
  \]
- Since a discrete Markov matrix satisfies \( \lambda_{\max}(A) = 1 \), the matrix \( B \) satisfies
  \[
  \lambda_{\max}(B) = 0
  \]
- Column sums transform as
  \[
  \sum_i B_{ij} = \sum_i A_{ij} - 1 = 0
  \]

This shows that discrete and continuous Markov models describe the **same conservation principle**, expressed in different time frameworks.

---

## 4. Steady-State Interpretation

| System type | Dominant eigenvalue | Steady-state coefficient |
|------------|--------------------|--------------------------|
| Difference equation | \( \lambda = 1 \) | \( 1^k \) |
| Differential equation | \( \lambda = 0 \) | \( e^{0t} \) |

In both cases, the steady-state contribution is constant, reflecting conservation of total probability.

---

## 5. Conceptual Summary

- Discrete Markov matrices conserve probability **per time step**
- Continuous Markov matrices conserve probability **per unit time**
- The transformation \( B = A - I \) links the two models
- Steady states appear as constant modes:
  \[
  1^k \quad \leftrightarrow \quad e^{0t}
  \]

These two formulations are mathematically equivalent descriptions of the same stochastic dynamics.

