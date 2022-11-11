import numpy as np


# 1. Стадия создания матриц
choice = input("Для работы с конкретными данными введите 1. В ином случае будет работа со случайными данными...\n")
if choice != '1':
    matrix_10_10 = np.random.randint(-10, 11, (10, 10))  # Создание матрицы 10x10 со случайными числами от -10 до 10
    free_elements = np.random.randint(-10, 11, 10)  # Создание столбца (массива) свободных членов с аналогичными числами
else:
    matrix_file = open('3_matrix.txt')
    matrix_10_10 = np.full((10, 10), 0)  # Создание матрицы 10x10, состоящей из нулей
    for i in range(10):  # Заполнение матрицы 10x10 значениями из файла
        matrix_10_10[i] = [int(value) for value in matrix_file.readline().split()]
    matrix_file.close()
    free_elements = np.fromfile('3_free_elements.txt', int, sep=" ")  # Создание столбца свободных членов из файла

# 2. Стадия расчётов
main_det = np.linalg.det(matrix_10_10)
if main_det != 0:
    solutions = []  # Матрица переменных x
    for i in range(10):
        work_matrix = matrix_10_10.copy()
        for j in range(10):
            work_matrix[j][i] = free_elements[j]  # Создание матриц, i-й столбец которых – столбец свободных членов
        solutions.append(np.linalg.det(work_matrix) / main_det)  # Нахождение x-ов и их сохранение

# 3. Стадия проверки
    # Нахождение столбца свободных членов путём умножения исходной матрицы на матрицу x-ов для проверки
    new_elements = matrix_10_10.dot(solutions)
    verification = 0  # Счётчик проверки
    for i in range(10):  # Проверка
        if abs(new_elements[i] - free_elements[i]) < 10**(-11):
            verification += 1
    if verification == 10:
        print("Проверка пройдена на ", verification, "/10.", sep="")

# 4. Стадия вывода
    print("Решение СЛАУ:")
    for value in solutions:
        print(value)
else:
    print("Метод Крамера не работает.")
