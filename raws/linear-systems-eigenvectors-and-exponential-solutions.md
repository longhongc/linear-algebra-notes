# Linear Systems of Differential Equations and Eigenvalues

## Problem setup

Consider a linear, homogeneous system of first-order differential equations:

$$
\frac{d\mathbf{x}}{dt} = A\mathbf{x},
$$

where:
- $\mathbf{x}(t) \in \mathbb{R}^n$ is the state vector,
- $A \in \mathbb{R}^{n \times n}$ is a constant matrix.

This is the vector analogue of the scalar equation $\dot{x} = ax$.

---

## Why eigenvectors appear

The matrix $A$ generally **mixes components** of $\mathbf{x}$, making the system coupled.  
To simplify the dynamics, we look for directions that are *not mixed* by $A$.

### Eigenvector condition

A vector $\mathbf{v} \neq 0$ is an eigenvector if

$$
A\mathbf{v} = \lambda \mathbf{v}.
$$

Along such a direction:
- $A$ only scales the vector,
- the direction of motion is preserved.

These directions are called **invariant directions** of the system.

---

## Reduction to the scalar equation

Assume the solution evolves along an eigenvector direction:

$$
\mathbf{x}(t) = y(t)\mathbf{v}.
$$

Differentiate and substitute into the system:

$$
\dot{\mathbf{x}} = y'(t)\mathbf{v} = A(y(t)\mathbf{v}) = \lambda y(t)\mathbf{v}.
$$

Cancel $\mathbf{v}$:

$$
y'(t) = \lambda y(t).
$$

---

## Exponential solutions

The scalar equation

$$
\dot{y} = \lambda y
$$

has the unique solution:

$$
y(t) = Ce^{\lambda t}.
$$

Therefore, each eigenpair $(\lambda, \mathbf{v})$ produces a solution:

$$
\mathbf{x}(t) = C\,\mathbf{v}e^{\lambda t}.
$$

**Key point:**  
Exponentials appear because they are the only functions whose derivative is proportional to themselves. This is true whether the unknown is scalar or vector-valued.

---

## General solution

If $A$ has $n$ linearly independent eigenvectors $\mathbf{v}_1, \dots, \mathbf{v}_n$ with eigenvalues $\lambda_1, \dots, \lambda_n$, then any initial condition can be decomposed as

$$
\mathbf{x}(0) = \sum_{i=1}^n c_i \mathbf{v}_i.
$$

Each component evolves independently, giving the general solution:

$$
\mathbf{x}(t) = \sum_{i=1}^n c_i \mathbf{v}_i e^{\lambda_i t}.
$$

Each term represents an independent **mode of motion**.

---

## Role of the nullspace

### Eigenvectors as nullspaces

Eigenvectors satisfy

$$
(A - \lambda I)\mathbf{v} = 0,
$$

so

$$
\mathbf{v} \in \mathcal{N}(A - \lambda I).
$$

Thus:
- eigenvectors are precisely the nonzero vectors in the nullspace of $A - \lambda I$,
- nontrivial nullspaces occur exactly when $\lambda$ is an eigenvalue.

---

### Connection to homogeneous systems

The system $\dot{\mathbf{x}} = A\mathbf{x}$ is **homogeneous**:
- there is no forcing term,
- the zero solution always exists,
- the set of solutions forms a vector space.

Because of homogeneity and linearity:
- solutions can be added and scaled,
- the nullspace structure determines the fundamental solution directions.

---

## Conceptual summary

- Eigenvectors identify directions where the system decouples.
- Along each eigenvector direction, the vector ODE reduces to the scalar equation $\dot{y} = \lambda y$.
- Exponential functions arise from this scalar dynamics.
- The general solution is a linear combination of eigenvector–exponential modes.
- Nullspaces explain why eigenvectors exist and how homogeneous systems admit nontrivial solutions.

---

## One-sentence intuition

> A linear system evolves exponentially along its invariant directions, and those directions are exactly the eigenvectors of the system matrix.

