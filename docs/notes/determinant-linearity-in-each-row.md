# Determinant: Linearity in Each Row

## Statement

Let \( A \) be an \( n \times n \) matrix with rows \( R_1, R_2, \dots, R_n \).

The determinant is **linear in each row when all other rows are fixed**.  
This property is called **multilinearity**.

---

## Meaning of Linearity in One Row

Fix all rows except the \( i \)-th row.

### Additivity
$$
\det(R_1, \dots, R_i + S_i, \dots, R_n)
=
\det(R_1, \dots, R_i, \dots, R_n)
+
\det(R_1, \dots, S_i, \dots, R_n)
$$

### Homogeneity
$$
\det(R_1, \dots, c R_i, \dots, R_n)
=
c \det(R_1, \dots, R_i, \dots, R_n)
$$

Additivity + homogeneity define linearity.

---

## Multilinearity

A function
$$
f : (\mathbb{R}^n)^n \to \mathbb{R}
$$
is **multilinear** if it is linear in each argument separately.

The determinant is multilinear in its rows (and equivalently, in its columns).

---

## Axiomatic Definition of the Determinant

The determinant is the unique function satisfying:

1. Multilinearity in rows  
2. Alternating property  
   - If two rows are equal, the determinant is zero  
   - Swapping two rows changes the sign  
3. Normalization  
$$
\det(I_n) = 1
$$

Linearity in each row is an **axiom**, not a derived result.

---

## Geometric Interpretation

The determinant represents **signed volume** of the parallelepiped spanned by the row vectors.

- Scaling one row scales the volume linearly  
- Replacing one row by a sum splits the volume additively  

Thus, volume behavior motivates linearity in each row.

---

## Consequence

Multilinearity expands the determinant into sums of products of entries.  
The alternating property eliminates terms with repeated rows or columns.

The remaining terms correspond to permutations, yielding the Leibniz formula.

---

## Key Insight

The determinant is linear in each row because it models oriented volume, which depends linearly on one vector at a time when the others are fixed.

