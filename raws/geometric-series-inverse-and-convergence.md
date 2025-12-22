# Geometric Series and the Inverse \((I - A)^{-1}\)

## 1. Scalar Geometric Series

The scalar geometric series is

$$
1 + a + a^2 + a^3 + \cdots
$$

It has the closed-form identity

$$
\frac{1}{1 - a} = 1 + a + a^2 + a^3 + \cdots
$$

**only if**

$$
|a| < 1.
$$

---

## 2. Why the Condition \(|a| < 1\) Is Necessary

Consider the partial sum

$$
S_N = 1 + a + a^2 + \cdots + a^N.
$$

This sum can be written exactly as

$$
S_N = \frac{1 - a^{N+1}}{1 - a}.
$$

The infinite series is defined as the limit

$$
\lim_{N \to \infty} S_N.
$$

- If \(|a| < 1\), then \(a^{N+1} \to 0\), and the limit exists:
  $$
  \lim_{N \to \infty} S_N = \frac{1}{1 - a}.
  $$

- If \(|a| \ge 1\), then \(a^{N+1}\) does not go to zero (it grows or oscillates), so the limit does not exist and the series diverges.

Thus, the condition \(|a| < 1\) ensures **convergence**, not algebraic correctness.

---

## 3. Why Formal Algebra Can Be Misleading

A common symbolic manipulation is

$$
S = 1 + a + a^2 + \cdots
$$

$$
aS = a + a^2 + a^3 + \cdots
$$

Subtracting,

$$
S - aS = 1
$$

$$
S(1 - a) = 1
$$

$$
S = \frac{1}{1 - a}.
$$

This reasoning implicitly assumes that \(S\) is a **finite number**.  
If the series diverges, \(S\) does not exist, and these steps are not valid.

---

## 4. Matrix Geometric Series

The matrix analogue is

$$
(I - A)^{-1} = I + A + A^2 + A^3 + \cdots
$$

This is called the **Neumann series**.

---

## 5. Convergence Condition for Matrices

The matrix series converges if and only if

$$
A^n \to 0 \quad \text{as } n \to \infty.
$$

A key sufficient and necessary condition is

$$
\rho(A) < 1,
$$

where \(\rho(A)\) is the **spectral radius**, the largest absolute value of the eigenvalues of \(A\).

If this condition holds:

- The infinite sum converges
- \((I - A)\) is invertible
- The series equals \((I - A)^{-1}\)

If not, the series diverges and the identity fails.

---

## 6. Conceptual Interpretation

- The geometric series represents repeated feedback or accumulation.
- Convergence requires each successive contribution to shrink.
- In scalars, this means \(|a| < 1\).
- In matrices, this means all eigenvalues lie inside the unit circle.

---

## 7. Key Takeaway

The geometric series formula does **not** always work.

It is valid because the infinite sum converges, not because of algebraic manipulation.

- Scalars: \(|a| < 1\)
- Matrices: \(\rho(A) < 1\)

Without convergence, the “sum” is not defined, and the inverse identity has no meaning.

