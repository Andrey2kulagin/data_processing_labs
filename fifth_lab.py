import numpy as np
import matplotlib.pyplot as plt
import statistics


def graph_with_trend(input_x, input_y, coefficients, lbl):  # Функция построения графика с линией тренда
    plt.scatter(input_x, input_y)  # Задание точечной диаграммы
    trend_line = np.poly1d(coefficients)  # Функция линии тренда
    plt.plot(input_x, trend_line(input_x))  # Задание линии тренда
    plt.ylabel('y')  # Название оси y
    plt.xlabel('x')  # Название оси x
    plt.title(lbl)  # Название графика
    determination = statistics.correlation(input_x, input_y)**2  # Коэффициент детерминации
    if coefficients[1] >= 0:  # Проверка знака перед 2-м коэффициентом для красивого вывода
        trend_text = "y = " + str("%.4f" % coefficients[0]) + "x + " + str("%.4f" % coefficients[1])
    else:
        trend_text = "y = " + str("%.4f" % coefficients[0]) + "x - " + str("%.4f" % abs(coefficients[1]))
    plt.text(140, 1.07, trend_text + "\nR^2 = " + str("%.4f" % determination))  # Плашка с текстом
    plt.show()  # Вывод графика


# 1. Стадия выбора
choice = input("Для работы с конкретными данными введите 1. В ином случае будет работа со случайными данными...\n")
if choice != '1':
    yT_column = np.random.random(50)  # Создание строки yT из 50 случайных чисел в промежутке (0; 1)
    xT_column = np.random.randint(10, 200, 50)  # Создание строки xT из случайных чисел в промежутке (10; 200)
else:
    yT_column = np.fromfile('5_6_y_data.txt', float, sep=" ")  # Создание строки yT из файла
    xT_column = np.fromfile('5_6_x_data.txt', int, sep=" ")  # Создание строки xT из файла

# 2. Стадия математических расчётов
y_column = yT_column.transpose()  # Создание столбца y (транспонирование строки yT)
XT_arr = np.ones((2, len(xT_column)), int)  # Создание транспонированной матрицы XT, состоящей из единиц
XT_arr[0] = xT_column  # Замена первой строки матрицы XT строкой xT; завершение матрицы XT
X_arr = XT_arr.transpose()  # Создание матрицы X транспонированием матрицы XT
XT_X = XT_arr.dot(X_arr)  # Умножение матрицы XT на матрицу X
obr_XT_X = np.linalg.inv(XT_X)  # Нахождение обратной матрицы obr_XT_X, полученной после умножения в прошлом шаге
XT_y = XT_arr.dot(y_column)  # Нахождение матрицы XT_y путём умножения матрицы XT на столбец y
# Коэффициенты уравнения парной линейной регрессии через умножение обратной матрицы obr_XT_X на матрицу XT_y
math_coefficients = obr_XT_X.dot(XT_y)

# 3. Стадия расчётов с помощью встроенных функций
func_coefficients = np.polyfit(xT_column, yT_column, 1)  # Коэффициенты уравнения парной линейной регрессии по функции
xT_sorted = np.sort(xT_column)  # Отсортированная строка xT
yT_sorted = np.sort(yT_column)  # Отсортированная строка yT
sorted_coefficients = np.polyfit(xT_sorted, yT_sorted, 1)  # Коэффициенты для отсортированных

# 4. Стадия проверки и вывода
verification = 0  # Счётчик проверки
for i in range(2):  # Проверка
    if abs(math_coefficients[i] - func_coefficients[i]) < 10**(-10):
        verification += 1
print("Проверка пройдена на ", verification, "/2.\nКоэффициенты уравнения парной линейной регрессии:", sep="")
for value in math_coefficients:
    print(value)

# 5. Стадия построения графиков
graph_with_trend(xT_column, yT_column, func_coefficients, 'Unsorted')
graph_with_trend(xT_sorted, yT_sorted, sorted_coefficients, 'Sorted')
