# Simultaneous Diagonalization and Commutativity

## Statement

Let \( A, B \in \mathbb{C}^{n \times n} \) be **diagonalizable matrices**.

Then the following are equivalent:

1. \( A \) and \( B \) are **simultaneously diagonalizable**, i.e., there exists an invertible matrix \( S \) such that
   \[
   A = S D_A S^{-1}, \quad B = S D_B S^{-1},
   \]
   where \( D_A \) and \( D_B \) are diagonal matrices.

2. \( A \) and \( B \) **commute**:
   \[
   AB = BA.
   \]

In words:
> **Diagonalizable matrices share the same eigenvector matrix if and only if they commute.**

---

## Intuition

- Diagonalization means choosing a basis of eigenvectors.
- Sharing the same eigenvector matrix means **both matrices act independently on the same coordinate directions**.
- Commutativity ensures that applying \( A \) then \( B \) has the same effect as applying \( B \) then \( A \), which is only possible when they do not mix each other’s eigenspaces.

---

## Why Simultaneous Diagonalization Implies Commutativity

Assume
\[
A = S D_A S^{-1}, \quad B = S D_B S^{-1}.
\]

Then
\[
AB = S D_A D_B S^{-1}, \quad BA = S D_B D_A S^{-1}.
\]

Since diagonal matrices commute,
\[
D_A D_B = D_B D_A,
\]
so
\[
AB = BA.
\]

---

## Why Commutativity Implies Simultaneous Diagonalization

Assume:
- \( A \) and \( B \) are diagonalizable
- \( AB = BA \)

Key idea:
- Commuting matrices **preserve each other’s eigenspaces**.
- Each eigenspace of \( A \) is invariant under \( B \).
- Since \( B \) is diagonalizable, it can be diagonalized *within* each eigenspace of \( A \).

Thus, a **common eigenbasis** exists, yielding a single matrix \( S \) that diagonalizes both.

---

## Important Caveats

- Commutativity **alone is not sufficient** if matrices are **not diagonalizable**.
- This result holds cleanly over \( \mathbb{C} \); over \( \mathbb{R} \), complex eigenvalues may obstruct real diagonalization.

---

## Key Takeaway

\[
\boxed{
\text{Diagonalizable } A, B \text{ share eigenvectors}
\;\Longleftrightarrow\;
AB = BA
}
\]

Commutativity is exactly the condition that allows two diagonalizable linear transformations to be expressed independently in the same coordinate system.

