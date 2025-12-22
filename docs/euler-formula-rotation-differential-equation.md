# Euler’s Formula via Rotation

## Goal

Explain why

$$
e^{it} = \cos t + i \sin t
$$

in a way that reveals *structure and meaning*, not coincidence.

---

## Core Idea

Euler’s formula expresses the fact that **complex exponentials describe rotation**, and  
$\cos t + i \sin t$ is the **coordinate description of the same rotation**.

Both arise from the same differential equation.

---

## Rotation as a Differential Equation

Let $z(t)$ be a complex-valued function representing a point in the complex plane.

Uniform circular motion has two defining properties:

1. The speed is constant.
2. The velocity is always perpendicular to the position.

In the complex plane, multiplication by $i$ rotates a vector by $90^\circ$ counterclockwise.

Therefore, uniform rotation is described by the differential equation

$$
\frac{dz}{dt} = i z
$$

---

## Solving the Equation

Solve the differential equation:

$$
\frac{dz}{dt} = i z
$$

Separate variables:

$$
\frac{1}{z} \, dz = i \, dt
$$

Integrate:

$$
\ln z = it + C
$$

Exponentiate:

$$
z(t) = C e^{it}
$$

Applying the initial condition $z(0) = 1$ gives $C = 1$, so

$$
z(t) = e^{it}
$$

This shows that $e^{it}$ represents a point rotating on the unit circle with angular speed $1$.

---

## Coordinate Description of the Same Motion

A point on the unit circle at angle $t$ has Cartesian coordinates

$$
(\cos t, \sin t)
$$

In complex form, this is

$$
z(t) = \cos t + i \sin t
$$

This expression also describes uniform rotation on the unit circle.

---

## Conclusion

Both expressions describe **the same geometric motion**:

- $e^{it}$ arises as the solution to the rotation differential equation.
- $\cos t + i \sin t$ arises from coordinate geometry.

Since they represent the same function of $t$ with the same initial condition,

$$
e^{it} = \cos t + i \sin t
$$

---

## Key Insight

Euler’s formula is not a coincidence of power series.

It reflects the deep principle that:

- Real exponentials describe growth and decay.
- Imaginary exponentials describe rotation.

