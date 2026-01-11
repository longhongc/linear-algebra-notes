# Hilbert Space View of Convolution and Fourier Transform

## 1. Hilbert Spaces and Inner Products
A Hilbert space is a vector space equipped with an inner product and complete with respect to the induced norm.  
For function spaces such as \( L^2(\mathbb{R}) \), the inner product is

$$
\langle f, g \rangle = \int_{-\infty}^{\infty} f(t)\,\overline{g(t)}\,dt
$$

This generalizes the dot product from finite-dimensional vector spaces to spaces of functions.

---

## 2. Convolution as a Linear Operator
Fix a function \( g \in L^2(\mathbb{R}) \). Convolution with \( g \) defines a linear operator:

$$
T_g(f) = f * g
$$

where

$$
(f * g)(t) = \int_{-\infty}^{\infty} f(\tau)\,g(t-\tau)\,d\tau
$$

In the time (or spatial) domain, this operator mixes values of \( f \), making direct computation and analysis difficult.

---

## 3. Convolution as Sliding Inner Products
For each fixed \( t \), convolution can be interpreted as an inner product:

$$
(f * g)(t) = \langle f, g_t^\ast \rangle
$$

where \( g_t^\ast(\tau) = g(t-\tau) \) is a shifted (and possibly reversed) version of \( g \).  
Thus, convolution measures similarity between \( f \) and shifted copies of \( g \).

---

## 4. Fourier Transform as a Change of Basis
The Fourier transform

$$
\mathcal{F}: L^2(\mathbb{R}) \to L^2(\mathbb{R})
$$

is a unitary operator, meaning it preserves inner products and norms. It expresses functions in terms of an orthonormal basis of complex exponentials:

$$
e^{i\omega t}
$$

These exponentials play the role of basis vectors, analogous to orthonormal eigenvectors in finite-dimensional linear algebra.

---

## 5. Eigenfunction Interpretation
The key observation is that complex exponentials are eigenfunctions of convolution operators:

$$
T_g(e^{i\omega t}) = (e^{i\omega t} * g)(t) = \hat g(\omega)\,e^{i\omega t}
$$

Here, \( \hat g(\omega) \) is the Fourier transform of \( g \).  
Thus, in the Fourier basis, convolution acts by simple scalar multiplication.

---

## 6. Diagonalization Viewpoint
This leads to the fundamental identity:

$$
\mathcal{F}(f * g) = \hat f(\omega)\,\hat g(\omega)
$$

Interpretation:
- In the original (time) basis, convolution is a complicated mixing operation.
- In the Fourier basis, the convolution operator is diagonal.
- Each frequency component is scaled independently by \( \hat g(\omega) \).

This is the infinite-dimensional analogue of diagonalizing a matrix.

---

## 7. Analogy with Finite-Dimensional Linear Algebra

| Finite-dimensional | Hilbert space |
|-------------------|---------------|
| Vector \( x \) | Function \( f(t) \) |
| Matrix \( A \) | Convolution operator \( T_g \) |
| Eigenvectors of \( A \) | Exponentials \( e^{i\omega t} \) |
| Diagonal matrix \( D \) | Multiplication by \( \hat g(\omega) \) |
| Change of basis \( P^{-1}AP \) | Fourier transform |

---

## 8. Key Insight
The Fourier transform diagonalizes convolution operators.  
Convolution becomes pointwise multiplication because the Fourier basis consists of eigenfunctions of all convolution operators.

---

## 9. Summary
- Convolution defines a linear operator on a Hilbert space of functions.
- The Fourier transform is a unitary change of basis to sinusoidal coordinates.
- In this basis, convolution becomes simple multiplication.
- This mirrors matrix diagonalization in finite-dimensional linear algebra and explains why Fourier methods simplify convolution-heavy problems.

