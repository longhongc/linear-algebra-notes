# Derivative of a Complex Exponential and Its Physical Meaning

## Setup

Let
$$
a = \alpha + i\beta \quad (\alpha, \beta \in \mathbb{R})
$$
and consider the complex exponential
$$
x(t) = e^{a t} = e^{(\alpha + i\beta)t}.
$$

---

## Derivative Formula

The derivative with respect to \( t \) follows the same rule as in the real case:
$$
\frac{d}{dt} e^{a t} = a\, e^{a t}.
$$

Explicitly,
$$
\frac{d}{dt} e^{(\alpha + i\beta)t} = (\alpha + i\beta)e^{(\alpha + i\beta)t}.
$$

---

## Decomposition Using Euler’s Formula

Using Euler’s formula,
$$
e^{(\alpha + i\beta)t} = e^{\alpha t}(\cos \beta t + i \sin \beta t).
$$

This naturally separates the behavior into:
- **Magnitude (radius)**: \( r(t) = e^{\alpha t} \)
- **Phase (angle)**: \( \theta(t) = \beta t \)

---

## Geometric Interpretation in the Complex Plane

The signal \( x(t) \) can be viewed as a vector in the complex plane:

- The vector **rotates** with angle \( \theta(t) = \beta t \)
- The vector’s **length changes** according to \( r(t) = e^{\alpha t} \)

Thus, \( x(t) \) traces a spiral (or circle) in the complex plane.

---

## Velocity Decomposition

The velocity is
$$
\dot{x}(t) = (\alpha + i\beta)x(t).
$$

This splits into two orthogonal components:

### 1. Radial (Magnitude) Velocity — \( \alpha \)

$$
\frac{d}{dt}|x(t)| = \alpha e^{\alpha t}.
$$

- \( \alpha < 0 \): exponential decay (stable)
- \( \alpha = 0 \): constant magnitude
- \( \alpha > 0 \): exponential growth (unstable)

This controls the **envelope** of the motion.

---

### 2. Tangential (Oscillatory) Velocity — \( i\beta \)

The phase evolves as
$$
\dot{\theta}(t) = \beta.
$$

- \( \beta \) is the **angular velocity**
- Multiplication by \( i \) corresponds to a \( 90^\circ \) rotation
- \( i\beta x(t) \) gives velocity **perpendicular** to the radius

The tangential speed magnitude is
$$
v_{\text{tan}} = r(t)\beta = \beta e^{\alpha t},
$$
analogous to circular motion \( v = r\omega \).

---

## Physical Interpretation

- **\( \alpha \)** controls growth or decay → stability
- **\( \beta \)** controls oscillation frequency

Common cases:

| \( \alpha \) | \( \beta \) | Behavior |
|-------------|-------------|----------|
| \( < 0 \) | \( = 0 \) | Pure exponential decay |
| \( = 0 \) | \( \neq 0 \) | Undamped oscillation |
| \( < 0 \) | \( \neq 0 \) | Damped oscillation (inward spiral) |
| \( > 0 \) | \( \neq 0 \) | Growing oscillation (outward spiral) |

---

## Connection to Real Signals

Taking the real part:
$$
\Re\{e^{(\alpha+i\beta)t}\} = e^{\alpha t}\cos(\beta t).
$$

- \( \beta \): oscillation frequency
- \( \alpha \): exponential envelope

---

## Key Intuition

A complex exponential represents a **rotating vector whose length changes exponentially**:
- \( \alpha \): radial (magnitude) velocity
- \( \beta \): angular (oscillatory) velocity

