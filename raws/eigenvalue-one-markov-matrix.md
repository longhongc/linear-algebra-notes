# Why \( \lambda = 1 \) Is Always an Eigenvalue of a Markov Matrix

## 1. Markov (Transition) Matrices

A **Markov matrix** \( A \) (column-stochastic version) satisfies:

- All entries are nonnegative.
- Each column sums to 1:
  $$
  \sum_i a_{ij} = 1 \quad \text{for all } j
  $$

This reflects conservation of total probability in a Markov process.

---

## 2. Eigenvalue Condition

A scalar \( \lambda \) is an eigenvalue of \( A \) if:
$$
\det(A - \lambda I) = 0
$$

To show that \( \lambda = 1 \) is an eigenvalue, we analyze the matrix \( A - I \).

---

## 3. Column-Sum Argument for \( A - I \)

Since each column of \( A \) sums to 1, subtracting the identity matrix gives:
$$
\sum_i (a_{ij} - \delta_{ij}) = 1 - 1 = 0
$$

Thus **each column of \( A - I \) sums to zero**.

---

## 4. Linear Dependence and Singularity

If the columns of a matrix sum to zero, then:

- The columns are linearly dependent.
- Equivalently, the rows are linearly dependent.

Therefore, the matrix \( A - I \) is singular:
$$
\det(A - I) = 0
$$

---

## 5. Conclusion

Since \( A - I \) is singular, we conclude:
$$
\boxed{\lambda = 1 \text{ is always an eigenvalue of a Markov matrix}}
$$

This result follows directly from probability conservation and does not depend on the size of the matrix.

---

## 6. Interpretation in Markov Processes

The eigenvalue \( \lambda = 1 \) corresponds to a **steady-state (stationary) distribution**:

- An eigenvector \( v \) such that:
  $$
  Av = v
  $$
- Applying the transition matrix leaves the distribution unchanged.

This explains why eigenvalue 1 plays a central role in the long-term behavior of Markov chains.

---

## 7. Key Takeaway

> Probability conservation forces \( A - I \) to be singular, so eigenvalue 1 must exist for every Markov matrix.

