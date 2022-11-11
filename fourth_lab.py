import numpy as np


# 1. Стадия создания матриц
choice = input("Для работы с конкретными данными введите 1. В ином случае будет работа со случайными данными...\n")
if choice != '1':
    matrix_100_100 = np.random.randint(1, 100, (100, 100))  # Создание матрицы 100x100 со случайными числами от 1 до 100
    free_elements = np.random.randint(1, 100, 100)  # Создание столбца свободных членов с аналогичными числами
else:
    free_elements = np.fromfile('4_free_elements.txt', int, sep=" ")  # Создание столбца свободных членов из файла
    matrix_file = open('4_matrix.txt')
    matrix_100_100 = np.full((100, 100), 0)  # Создание матрицы 100x100 из нулей
    for i in range(100):  # Заполнение матрицы 100x100 значениями из файла
        matrix_100_100[i] = [int(value) for value in matrix_file.readline().split()]
    matrix_file.close()

# 2. Стадия расчётов
obr_matrix = np.linalg.inv(matrix_100_100)  # Нахождение обратной матрицы 100x100
solutions = obr_matrix.dot(free_elements)  # Нахождение x-ов умножением обратной матрицы на столбец свободных членов

# 3. Стадия проверки
new_elements = matrix_100_100.dot(solutions)  # Нахождение столбца свободных членов для проверки
verification = 0
for i in range(100):
    if abs(free_elements[i] - new_elements[i]) < 10**(-11):
        verification += 1
print("Проверка пройдена на ", verification, "/100.", sep="")

# 4. Стадия вывода
print("Решения СЛАУ:")
for value in solutions:
    print(value)
