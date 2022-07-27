import numpy as np
import time
import random

N = 1000  # количество элементов в массиве
arr_main = np.random.randint(-100, 100, N)  # создаем и заполняем массив

# создаем 3-и копии массива arr_main для 3-х разных сортировок

arr_bubble = arr_main.copy()  # для сортировки пузырьком
arr_insertionSort = arr_main.copy()  # для сортировки вставками
arr_quickSort = arr_main.copy()  # для быстрой сортировки


# создаем функцию для рассчета времени работы сортировок. (Декоратор)

def testTime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        dt = time.time() - start_time
        print(f"Время работы: {dt} сек")
        return result

    return wrapper


# Реализуем сортировку пузырьком

print("<Соритровка пузырьком>")


@testTime
def bubble(arr_bubble):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr_bubble[j] > arr_bubble[j + 1]:
                arr_bubble[j], arr_bubble[j + 1] = arr_bubble[j + 1], arr_bubble[j]


bubble(arr_bubble)

print('------------------------')

# Реализуем сортировку вставками
print("<Сортировка вставками>")


@testTime
def insertion_sort(arr_insertionSort):
    for i in range(1, len(arr_insertionSort)):
        el = arr_insertionSort[i]
        j = i - 1
        while j >= 0 and arr_insertionSort[j] > el:
            arr_insertionSort[j + 1] = arr_insertionSort[j]
            j -= 1
            arr_insertionSort[j + 1] = el


insertion_sort(arr_insertionSort)
print('------------------------')

# Реализуем быструю сортировку
print("<Быстрая сортировка>")


# @testTime
def quick_sort(arr_quickSort):
    if len(arr_quickSort) <= 1:
        return arr_quickSort
    else:
        value = random.choice(arr_quickSort)

    left_side = [i for i in arr_quickSort if value < i]
    middle = [i for i in arr_quickSort if i == value]
    right_side = [i for i in arr_quickSort if value > i]

    return quick_sort(left_side) + middle + quick_sort(right_side)


quicksort_time = time.time()
Qsorted_arr = quick_sort(arr_quickSort)
print("Время работы = %.18f сек" % (time.time() - quicksort_time))
