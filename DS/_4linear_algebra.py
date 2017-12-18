def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_columns, entry_fn):
    return [[entry_fn(i, j) for j in range(num_columns)] for i in range(num_rows)]