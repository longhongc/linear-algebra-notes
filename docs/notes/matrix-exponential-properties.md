# Properties of the Matrix Exponential \( e^{At} \)

Let \( A \in \mathbb{R}^{n \times n} \) (or \( \mathbb{C}^{n \times n} \)) and \( t \in \mathbb{R} \).
The matrix exponential \( e^{At} \) generalizes the scalar exponential and is fundamental in linear differential equations and dynamical systems.

---

## 1. Definition (Taylor Series)

The matrix exponential is defined by the power series

$$
e^{At} \;=\; \sum_{k=0}^{\infty} \frac{(At)^k}{k!}
\;=\;
I + At + \frac{(At)^2}{2!} + \frac{(At)^3}{3!} + \cdots
$$

**Key facts**
- The series converges for every square matrix \( A \).
- No diagonalization assumption is required.
- This definition is the foundation of all properties below.

---

## 2. Linearity in the Exponent (Addition Rule)

If two matrices commute,

$$
AB = BA,
$$

then

$$
e^{A} e^{B} = e^{A+B}.
$$

In particular, for the same matrix \( A \),

$$
e^{At_1} e^{At_2} = e^{A(t_1 + t_2)}.
$$

**Important caveat**

$$
e^{A} e^{B} \neq e^{A+B}
\quad \text{in general if } AB \neq BA.
$$

---

## 3. Inverse Property

The matrix exponential is always invertible:

$$
\left(e^{At}\right)^{-1} = e^{-At}.
$$

This follows directly from the power series and mirrors the scalar identity

$$
e^{x} e^{-x} = 1.
$$

---

## 4. Diagonalization Formula

If \( A \) is diagonalizable,

$$
A = V \Lambda V^{-1},
$$

where \( \Lambda = \mathrm{diag}(\lambda_1, \dots, \lambda_n) \), then

$$
e^{At} = V e^{\Lambda t} V^{-1},
$$

with

$$
e^{\Lambda t}
=
\mathrm{diag}\!\left(e^{\lambda_1 t}, \dots, e^{\lambda_n t}\right).
$$

**Consequences**
- Eigenvalues of \( e^{At} \) are \( e^{\lambda_i t} \).
- Computation reduces to scalar exponentials.
- If \( A \) is not diagonalizable, Jordan form introduces polynomial factors in \( t \).

---

## 5. Differentiation Rule

The matrix exponential differentiates exactly like the scalar case:

$$
\frac{d}{dt} e^{At} = A e^{At} = e^{At} A.
$$

This works because \( A \) commutes with all its powers.

---

## 6. Role in Linear Differential Equations

For the linear system

$$
\dot{x}(t) = A x(t),
$$

the unique solution with initial condition \( x(0) \) is

$$
x(t) = e^{At} x(0).
$$

Thus, \( e^{At} \) acts as the **state transition matrix**, describing how the system evolves over time.

---

## 7. Key Takeaways

- \( e^{At} \) is defined by a convergent power series.
- It behaves like the scalar exponential **when matrices commute**.
- It is always invertible.
- Diagonalization simplifies computation and reveals system behavior.
- Differentiation mirrors the scalar exponential.
- Stability and long-term behavior are governed by eigenvalues of \( A \).

---

