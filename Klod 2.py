print(f'Задача - "Матрица воплоти!"')
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

rezult1 = get_matrix(2, 2, 10)
print(rezult1)
rezult2 = get_matrix(3, 5, 42)
print(rezult2)
rezult3 = get_matrix(4, 2, 13)
print(rezult3)
rezult4 = get_matrix(3, 7,209)
print(rezult4)