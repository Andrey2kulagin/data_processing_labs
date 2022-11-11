import random
import statistics
import matplotlib.pyplot as plt
import numpy as np


def sr_znach(input_arr):  # Функция нахождения среднего значения
    summa = 0
    for x in input_arr:
        summa += x
    return summa / len(input_arr)


def dispersion(input_arr, input_mean):  # Функция нахождения дисперсии
    summa = 0
    for x in input_arr:
        summa += (x - input_mean) ** 2
    return summa / (len(input_arr) - 1)


def set_graf(arr_y, input_mean, input_sko, lbl):  # Функция построения графика
    arr_x = [x for x in range(len(arr_y))]  # Задание значений оси x
    plt.plot(arr_x, arr_y)  # Задание основной линии
    arr_y_mean = [input_mean] * len(arr_x)
    plt.plot(arr_x, arr_y_mean)  # Задание линии среднего значения
    arr_y_sko_up = [input_mean + input_sko] * len(arr_x)
    plt.plot(arr_x, arr_y_sko_up)  # Задание линии отклонения от среднего значения вверх
    arr_y_sko_down = [input_mean - input_sko] * len(arr_x)
    plt.plot(arr_x, arr_y_sko_down)  # Задание линии отклонения от среднего значения вниз
    plt.title(lbl)  # Название графика
    plt.xlabel('x')  # Название оси x
    plt.ylabel('Значения')  # Название оси y
    plt.show()  # Вывод графика


# 1. Стадия создания наборов
work_type = input("Для работы с конкретными данными введите 1. В ином случае будет работа со случайными данными...\n")
if work_type != '1':
    first_arr = []
    for i in range(41):
        first_arr.append(random.random())
    second_arr = []
    for j in range(41):
        second_arr.append(random.randint(1, 10))
else:
    first_arr = np.fromfile('1_first_arr.txt', float, sep=" ")
    second_arr = np.fromfile('1_second_arr.txt', float, sep=" ")

# 2. Стадия расчётов
first_sr_znach = sr_znach(first_arr)  # Среднее значение первого набора
first_dispersion = dispersion(first_arr, first_sr_znach)  # Дисперсия первого набора
first_sko = first_dispersion**0.5  # Среднеквадратичное отклонение первого набора
second_sr_znach = statistics.mean(second_arr)  # Среднее значение второго набора
second_dispersion = statistics.variance(second_arr)  # Дисперсия второго набора
second_sko = second_dispersion**0.5  # Среднеквадратичное отклонение второго набора

# 3. Стадия построения графиков
set_graf(first_arr, first_sr_znach, first_sko, "Набор (0; 1)")
set_graf(second_arr, second_sr_znach, second_sko, "Набор [1; 10]")
