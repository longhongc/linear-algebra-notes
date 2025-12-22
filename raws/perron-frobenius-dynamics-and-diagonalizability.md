# Perron–Frobenius Theorem: Dynamics and Diagonalizability

## Core Question

When analyzing the iteration

$$
x_{k+1} = A x_k
$$

do we need to assume that the matrix \(A\) is diagonalizable in order to conclude Perron–Frobenius–type long-term behavior?

**Answer:** No. Diagonalizability is not required.

---

## Setting

Let \(A\) be a positive or irreducible nonnegative square matrix.

Let:
- \( \lambda_{\max} \) be the Perron (largest) eigenvalue
- \( v_{\max} \) be the corresponding right Perron eigenvector
- \( w_{\max} \) be the corresponding left Perron eigenvector

---

## What Perron–Frobenius Guarantees

The Perron–Frobenius theorem guarantees the following:

- \( \lambda_{\max} \) is real and strictly positive  
- \( \lambda_{\max} \) is simple (algebraic multiplicity 1)  
- \( v_{\max} \) has strictly positive entries  
- No other eigenvalue satisfies \( |\lambda_i| = \lambda_{\max} \)  
- Left and right Perron eigenvectors both exist  

---

## What Perron–Frobenius Does *Not* Guarantee

The theorem does **not** guarantee:

- That \(A\) is diagonalizable  
- That all eigenvectors are linearly independent  
- That Jordan blocks do not exist for non-Perron eigenvalues  

Thus, writing an arbitrary vector as a sum of eigenvectors is, in general, an assumption and not always valid.

---

## Why Diagonalizability Is Not Needed

Even when \(A\) is not diagonalizable, the powers of \(A\) admit a dominant-term expansion:

$$
A^k = \lambda_{\max}^k \, v_{\max} w_{\max}^T + \text{lower-order terms}
$$

The lower-order terms involve factors of the form

$$
k^m \lambda_i^k \quad \text{with } |\lambda_i| < \lambda_{\max}
$$

Polynomial growth in \(k\) cannot overcome exponential dominance by \( \lambda_{\max}^k \).

---

## Correct Long-Term Formula

For any initial vector \(x_0 \ge 0\),

$$
A^k x_0
=
\lambda_{\max}^k \, v_{\max} (w_{\max}^T x_0)
+ O((\rho + \epsilon)^k)
$$

where \( \rho = \max_{i \ne \max} |\lambda_i| \).

This result follows from **spectral projection**, not from eigenvector decomposition.

---

## Dynamical Consequences

The Perron eigenvector always determines the asymptotic *shape*, while the Perron eigenvalue determines the *magnitude* behavior.

- If \( \lambda_{\max} > 1 \): exponential growth along \( v_{\max} \)
- If \( \lambda_{\max} = 1 \): stable shape (no growth or decay)
- If \( 0 < \lambda_{\max} < 1 \): exponential decay to zero

In all cases, normalized states converge to \( v_{\max} \).

---

## Key Takeaway

Perron–Frobenius theory does not rely on diagonalizability.  
Even in the presence of Jordan blocks, the Perron eigenvalue dominates all other spectral components, ensuring predictable long-term behavior governed by a single positive eigenvector.

