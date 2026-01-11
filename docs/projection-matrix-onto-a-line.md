# Projection Matrix onto a Line

## Goal
Given a nonzero vector \( u \in \mathbb{R}^n \), construct and understand the matrix that gives the **orthogonal projection** of any vector \( x \) onto the line
$$
L = \operatorname{span}\{u\}.
$$

---

## Key Idea (Geometric)
The orthogonal projection of \( x \) onto the line spanned by \( u \) is the unique vector \( Px \) such that:
1. \( Px \) lies on the line \( \operatorname{span}\{u\} \)
2. The error \( x - Px \) is orthogonal to the line

---

## Derivation

### Step 1: Form of the projection
Since the projection lies on the line,
$$
Px = \alpha u
$$
for some scalar \( \alpha \) depending on \( x \).

### Step 2: Orthogonality condition
Orthogonality of the error gives
$$
u^T(x - Px) = 0.
$$

Substitute \( Px = \alpha u \):
$$
u^T x - \alpha\, u^T u = 0.
$$

### Step 3: Solve for the scalar
$$
\alpha = \frac{u^T x}{u^T u}.
$$

Thus,
$$
Px = \left( \frac{u^T x}{u^T u} \right) u.
$$

---

## Projection Matrix Formula
Rewrite the projection in matrix form:
$$
Px = \frac{u u^T}{u^T u}\, x.
$$

Since this holds for all \( x \), the projection matrix is
$$
\boxed{
P = \frac{u u^T}{u^T u}
}
$$

---

## Role of the Condition \( Pu = u \)
The condition
$$
Pu = u
$$
means vectors already on the line are unchanged by the projection.

- This condition is **necessary**, but not sufficient, to define the projection uniquely.
- Orthogonality (equivalently, symmetry) is what selects the orthogonal projection among all possible projections.

---

## Key Properties
For the orthogonal projection matrix
$$
P = \frac{u u^T}{u^T u}:
$$

- **Idempotent:** \( P^2 = P \)
- **Symmetric:** \( P^T = P \)
- **Eigenvalues:** only \( 0 \) and \( 1 \)
  - Eigenvalue \( 1 \): direction of \( u \)
  - Eigenvalue \( 0 \): directions orthogonal to \( u \)
- **Rank:** \( 1 \)

---

## Special Case: Unit Vector
If \( u \) is normalized so that \( u^T u = 1 \), then
$$
P = u u^T.
$$

---

## Common Pitfalls
- Assuming \( Pu = u \) alone defines the projection matrix
- Forgetting to divide by \( u^T u \) when \( u \) is not a unit vector
- Confusing orthogonal projection with general (oblique) projections

---

## Takeaway
The projection matrix onto a line is derived by enforcing:
- alignment with the line, and
- orthogonality of the projection error.

These conditions lead uniquely to
$$
P = \frac{u u^T}{u^T u}.
$$

