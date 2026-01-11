# Fourier Series as Projection in Hilbert Space

## 1. Hilbert Space Setting

Fourier series are naturally understood within the framework of **Hilbert spaces**.  
The standard setting is the Hilbert space

$$
L^2([-\pi,\pi])
$$

the space of square-integrable functions on $[-\pi,\pi]$, equipped with the inner product

$$
\langle f,g \rangle = \int_{-\pi}^{\pi} f(x)\overline{g(x)}\,dx.
$$

This inner product induces the norm

$$
\|f\|_{L^2} = \left( \int_{-\pi}^{\pi} |f(x)|^2 dx \right)^{1/2}.
$$

---

## 2. Orthogonal Functions: Sines and Cosines

In $L^2([-\pi,\pi])$, the functions

$$
1,\quad \cos(nx),\quad \sin(nx), \quad n=1,2,3,\dots
$$

form an **orthogonal system** with respect to the $L^2$ inner product:

$$
\langle \sin(nx), \sin(mx) \rangle = 0 \quad \text{for } n \neq m,
$$

$$
\langle \cos(nx), \cos(mx) \rangle = 0 \quad \text{for } n \neq m,
$$

$$
\langle \sin(nx), \cos(mx) \rangle = 0 \quad \text{for all } n,m.
$$

---

## 3. Fourier Coefficients as Orthogonal Projections

Given a function $f \in L^2([-\pi,\pi])$, its Fourier coefficients are

$$
a_n = \frac{\langle f, \cos(nx) \rangle}{\langle \cos(nx), \cos(nx) \rangle},
\quad
b_n = \frac{\langle f, \sin(nx) \rangle}{\langle \sin(nx), \sin(nx) \rangle}.
$$

Each coefficient is exactly the **orthogonal projection** of $f$ onto the corresponding basis function.

The partial Fourier series

$$
S_N f = \sum_{n=1}^N \left( a_n \cos(nx) + b_n \sin(nx) \right)
$$

is the projection of $f$ onto a finite-dimensional subspace.

---

## 4. Completeness and Spanning

The sine and cosine functions do **not** span $L^2([-\pi,\pi])$ in the finite-dimensional sense.  
Instead, they are **complete**:

$$
\overline{\text{span}}\{1,\sin(nx),\cos(nx)\} = L^2([-\pi,\pi]).
$$

This means:

- Any $f \in L^2([-\pi,\pi])$ can be approximated arbitrarily well
- using finite linear combinations of sines and cosines
- with convergence measured in the $L^2$ norm.

---

## 5. Meaning of Fourier Series Convergence

For $f \in L^2([-\pi,\pi])$,

$$
\lim_{N \to \infty} \|f - S_N f\|_{L^2} = 0.
$$

Important distinctions:

- Convergence is **in norm**, not necessarily pointwise
- No continuity or smoothness is required
- Stronger convergence requires stronger assumptions on $f$

---

## 6. Relation to Fourier Transform

Fourier series:
- Domain: finite interval / periodic functions
- Basis: countable set of orthogonal functions

Fourier transform:
- Domain: $\mathbb{R}$
- Basis: uncountable family $e^{i\xi x}$
- Still a unitary operator on $L^2(\mathbb{R})$

Both are manifestations of the same Hilbert-space principle:
**decomposition into orthogonal frequency components**.

---

## 7. Key Takeaways

- Fourier series are best understood as **orthogonal projections in a Hilbert space**
- Sines and cosines form an **orthogonal and complete basis** of $L^2([-\pi,\pi])$
- Completeness, not finiteness, guarantees representability
- The statement “any function can be written as sines and cosines” is true **only in the $L^2$ sense**

This interpretation generalizes naturally to abstract Hilbert spaces.

