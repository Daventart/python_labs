def check_matrix(mat):
    if len(mat) == 0:
        return
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("Матрица рваная")


def transpose(mat: list[list[float | int]]) -> list[list]:
    check_matrix(mat)
    if len(mat) == 0:
        return []
    
    res = []
    for j in range(len(mat[0])):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])
        res.append(row)
    return res

def row_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    res = []
    for row in mat:
        s = 0
        for x in row:
            s += x
        res.append(s)
    return res

def col_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    res = []
    for j in range(len(mat[0])):
        s = 0
        for i in range(len(mat)):
            s += mat[i][j]
        res.append(s)
    return res


# Тест кейсы
# transpose
print('transpose')
print(f'transpose([[1, 2, 3]]) ->', transpose([[1, 2, 3]]))
print(f'transpose([[1], [2], [3]]) ->', transpose([[1], [2], [3]]))
print(f'transpose([[1, 2], [3, 4]]) ->', transpose([[1, 2], [3, 4]]))
print(f'transpose([]) ->', transpose([]))

try:
    print(f'transpose([[1, 2], [3]]) ->', transpose([[1, 2], [3]]))
except ValueError as error:
    print(f'transpose([[1, 2], [3]]) -> ValueError: {error}')

# row_sums
print('row_sums')
print(f'row_sums([[1, 2, 3], [4, 5, 6]]) ->', row_sums([[1, 2, 3], [4, 5, 6]]))
print(f'row_sums([[-1, 1], [10, -10]]) ->', row_sums([[-1, 1], [10, -10]]))
print(f'row_sums([[0, 0], [0, 0]]) ->', row_sums([[0, 0], [0, 0]]))

try:
    print(f'row_sums([[1, 2], [3]]) ->', row_sums([[1, 2], [3]]))
except ValueError as error:
    print(f'row_sums([[1, 2], [3]]) -> ValueError: {error}')

# col_sums
print('col_sums')
print(f'col_sums([[1, 2, 3], [4, 5, 6]]) ->', col_sums([[1, 2, 3], [4, 5, 6]]))
print(f'col_sums([[-1, 1], [10, -10]]) ->', col_sums([[-1, 1], [10, -10]]))
print(f'col_sums([[0, 0], [0, 0]]) ->', col_sums([[0, 0], [0, 0]]))

try:
    print(f'col_sums([[1, 2], [3]]) ->', col_sums([[1, 2], [3]]))
except ValueError as error:
    print(f'col_sums([[1, 2], [3]]) -> ValueError: {error}')
