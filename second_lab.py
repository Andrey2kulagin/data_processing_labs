import statistics
import random
import matplotlib.pyplot as plt


def print_graph(arr_x, arr_y, lbl):  # Функция построения точечной диаграммы
    plt.scatter(arr_x, arr_y)  # Задание точечной диаграммы
    plt.xlabel('x_arr')  # Подпись оси y
    plt.ylabel('y_arr')  # Подпись оси x
    plt.title(lbl)  # Название графика
    plt.show()  # Отображение графика


# 1. Стадия создания наборов
x_arr = []
y_arr = []
choice = input("Для работы с конкретными данными введите 1. В ином случае будет работа со случайными данными...\n")
if choice == '1':
    x_file = open('2_x_data.txt', 'r')
    x_arr = [float(line.strip()) for line in x_file]
    x_file.close()
    y_file = open('2_y_data.txt', 'r')
    y_arr = [float(line.strip()) for line in y_file]
    y_file.close()
else:
    for i in range(40):  # создание двух наборов случайных чисел определённой длины (можно изменить)
        x_arr.append(random.random())  # значения от 0 до 1
        y_arr.append(float(random.randint(1, 10)))  # значения от 1 до 10
    x_arr = sorted(x_arr)  # сортировка x по возрастанию
    y_arr = sorted(y_arr)  # сортировка y по возрастанию

xy_arr = []
x_pow2 = []
y_pow2 = []
for i in range(len(x_arr)):
    xy_arr.append(x_arr[i] * y_arr[i])  # создание набора произведений x*y
    x_pow2.append(x_arr[i] ** 2)  # создание набора x^2
    y_pow2.append(y_arr[i] ** 2)  # создание набора y^2

# 2. Стадия математических расчётов
x_mean = statistics.mean(x_arr)  # среднее значение x
y_mean = statistics.mean(y_arr)  # среднее значение y
xy_mean = statistics.mean(xy_arr)  # среднее значение x*y
cov_maths = xy_mean - x_mean * y_mean  # ковариация по математической формуле
cov_function = statistics.covariance(x_arr, y_arr)  # ковариация с помощью встроенной функции
x_sko = statistics.stdev(x_arr, x_mean)  # среднеквадратичное отклонение x
y_sko = statistics.stdev(y_arr, y_mean)  # среднеквадратичное отклонение y
r_x_y_maths = cov_maths / (x_sko * y_sko)  # коэффициент корреляции x и y по математической формуле
print("Коэффициент корреляции x и y по математической формуле:", r_x_y_maths, "\n")

# 3. Стадия нахождения коэффициентов корреляции с помощью функций
r_x_y_function = statistics.correlation(x_arr, y_arr)  # коэффициент корреляции x и y с помощью встроенной функции
print("Коэффициент корреляции x и y:", r_x_y_function)
r_x2_y_function = statistics.correlation(x_pow2, y_arr)  # коэффициент корреляции x^2 и y с помощью встроенной функции
print("Коэффициент корреляции x^2 и y:", r_x2_y_function)
r_x_y2_function = statistics.correlation(x_arr, y_pow2)  # коэффициент корреляции x и y^2 с помощью встроенной функции
print("Коэффициент корреляции x и y^2:", r_x_y2_function)

# 4. Стадия построения графиков
print_graph(x_arr, y_arr, "x, y")
print_graph(x_pow2, y_arr, "x^2, y")
print_graph(x_arr, y_pow2, "x, y^2")
