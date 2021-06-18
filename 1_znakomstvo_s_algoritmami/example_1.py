# coding=utf-8
# бинарный поиск выполняется за
# log n шагов

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if item == guess:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print binary_search(my_list, 3)

print binary_search(my_list, -1)
