# Weighted Least Squares (WLS)

## 1. Review: Ordinary Least Squares
Given an overdetermined linear system
$$
Ax = b,
$$
the **ordinary least-squares (OLS)** problem seeks
$$
x_b = \arg\min_x \|Ax - b\|_2^2.
$$

This leads to the normal equations:
$$
A^T A x_b = A^T b.
$$

---

## 2. Motivation for Weighted Least Squares
In many applications, different components of the data vector \( b \) have different levels of reliability.  
To reflect this, we introduce a **weighting matrix** \( W \), typically:
- square,
- diagonal,
- positive definite.

Weights allow certain residuals to be penalized more strongly than others.

---

## 3. Reformulated Least-Squares Problem
Instead of minimizing the unweighted residual, WLS minimizes:
$$
\|W(Ax - b)\|_2^2.
$$

This is equivalent to applying ordinary least squares to the **transformed system**:
$$
WAx = Wb.
$$

The least-squares solution of this system is denoted by \( x_{bW} \).

---

## 4. Derivation of the Weighted Normal Equations
Applying OLS to \( WAx = Wb \), we obtain:
$$
(WA)^T (WA) x_{bW} = (WA)^T (Wb).
$$

Using \( (WA)^T = A^T W^T \), this becomes:
$$
\boxed{
(A^T W^T W A)\, x_{bW} = A^T W^T W b
}
$$

These are called the **weighted normal equations**.

---

## 5. Structure and Interpretation
- The matrix \( W^T W \) appears on both sides of the equations.
- If \( W = I \), the weighted normal equations reduce to the ordinary normal equations.
- Larger weights increase the influence of the corresponding equations in the solution.

A common statistical choice is:
$$
W = \Sigma^{-1/2},
$$
where \( \Sigma \) is the covariance matrix of the measurement errors.

---

## 6. Explicit Solution
If the matrix \( A^T W^T W A \) is invertible, the weighted least-squares solution is:
$$
\boxed{
x_{bW} = (A^T W^T W A)^{-1} A^T W^T W b
}
$$

---

## 7. Summary
- Weighted least squares modifies OLS by scaling the system with a weight matrix \( W \).
- The original system \( Ax = b \) is replaced by \( WAx = Wb \).
- The solution changes from \( x_b \) to \( x_{bW} \).
- The key result is the weighted normal equations involving \( A^T W^T W A \).

