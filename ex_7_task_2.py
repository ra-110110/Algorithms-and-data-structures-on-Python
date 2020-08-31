"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform

int_list = []
for i in range(10):
    int_list.append(round(uniform(0, 49), 2))
print(f"исходный список {int_list}")


def mergeSort(int_list):
    # print(f"исходный список {int_list}")
    if len(int_list) > 1:
        mid = len(int_list) // 2
        left = int_list[:mid]
        right = int_list[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                int_list[k] = left[i]
                i = i + 1
            else:
                int_list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            int_list[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            int_list[k] = right[j]
            j = j + 1
            k = k + 1
    # print(f"отсортированный список {int_list}")


mergeSort(int_list)
print(f"отсортированный список {int_list}")
