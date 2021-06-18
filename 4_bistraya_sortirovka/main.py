def sumCicle(arr):
    total = 0
    for x in arr:
        total += x
    return total


def sumRecursive(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sumRecursive(arr[1:])


def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


my_list = [2, 44, 3, 11, 25, 4, 5, 6, 10]
sortedList = quickSort(my_list)

print 'sorted list'
print sortedList

print sumCicle(my_list)
print sumRecursive(my_list)


def alterLen(arr):
    try:
        if arr[0]:
            return 1 + alterLen(arr[1:])
    except IndexError:
        return 0


print alterLen(my_list)


def getLargestRec(arr, largest=0):
    if len(arr) == 0:
        return largest
    else:
        if arr[0] > largest:
            return getLargestRec(arr[1:], arr[0])
        else:
            return getLargestRec(arr[1:], largest)


print getLargestRec(my_list)


def binary_search(arr, item):
    if len(arr) == 0:
        return None
    else:
        high = len(arr) - 1
        mid = high / 2
        if item == arr[mid]:
            return mid
        elif item > arr[mid]:
            res = binary_search(arr[mid + 1:], item)
            return res + mid + 1 if res is not None else None
        else:
            return binary_search(arr[:mid], item)


print binary_search(my_list, 12)

