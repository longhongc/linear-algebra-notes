# Inverse of a Transpose Identity

## Statement of the Identity

For a square, invertible matrix $A$, the following identity holds:
$$
(A^T)^{-1} = (A^{-1})^T
$$

This means that **taking the transpose and taking the inverse commute**.

---

## Conditions for Validity

This identity is valid **if and only if**:

- $A$ is a **square** matrix
- $A$ is **invertible** (equivalently, $\det(A) \neq 0$)

If $A$ is not invertible, neither $(A^T)^{-1}$ nor $A^{-1}$ exists, so the identity is not defined.

---

## Proof

Start from the definition of the inverse:
$$
A A^{-1} = I
$$

Take the transpose of both sides:
$$
(A A^{-1})^T = I^T
$$

Using standard transpose properties:
- $(BC)^T = C^T B^T$
- $I^T = I$

we obtain:
$$
(A^{-1})^T A^T = I
$$

This shows that $(A^{-1})^T$ is a **left inverse** of $A^T$.  
Since $A^T$ is square, the left inverse equals the right inverse, so:
$$
(A^T)^{-1} = (A^{-1})^T
$$

---

## Conceptual Interpretation

- The **transpose** operation swaps rows and columns.
- The **inverse** operation undoes the linear transformation.

Because transposition preserves invertibility and only rearranges how the transformation is represented, the order of these two operations does not matter.

---

## Example

Let
$$
A =
\begin{pmatrix}
1 & 2 \\\\
3 & 4
\end{pmatrix}
$$

The inverse of $A$ is:
$$
A^{-1} =
\begin{pmatrix}
-2 & 1 \\\\
\frac{3}{2} & -\frac{1}{2}
\end{pmatrix}
$$

Taking its transpose:
$$
(A^{-1})^T =
\begin{pmatrix}
-2 & \frac{3}{2} \\\\
1 & -\frac{1}{2}
\end{pmatrix}
$$

Now transpose first:
$$
A^T =
\begin{pmatrix}
1 & 3 \\\\
2 & 4
\end{pmatrix}
$$

and invert:
$$
(A^T)^{-1} =
\begin{pmatrix}
-2 & \frac{3}{2} \\\\
1 & -\frac{1}{2}
\end{pmatrix}
$$

The results match, confirming the identity.

---

## Related Identities

For invertible matrices $A$ and $B$:

- $(AB)^{-1} = B^{-1} A^{-1}$
- $(AB)^T = B^T A^T$
- $(A^T)^T = A$

Special case:
- If $A$ is **orthogonal**, then $A^{-1} = A^T$

---

## Summary

- The identity $(A^T)^{-1} = (A^{-1})^T$ holds for all square, invertible matrices.
- It follows directly from the definition of the inverse and basic transpose rules.
- This result is frequently used in proofs involving orthogonal matrices, least squares, and matrix factorizations.

