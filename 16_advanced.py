# binary search

def binarySearch(sort: list, target: int, start: int, stop: int, value: bool):
    """binary search with recursion"""
    if start > stop:
        if value:
            return None  # not found value
        else:
            return -1  # not found index

    else:
        mid = (start + stop) // 2

        if target == sort[mid]:
            if value:
                return sort[mid]  # found value
            else:
                return mid  # found index

        elif target < sort[mid]:
            return binarySearch(sort, target, start, mid - 1, value)
        else:
            return binarySearch(sort, target, mid + 1, stop, value)


arr = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]

print(binarySearch(arr, 33, 0, len(arr), True))
print(binarySearch(arr, 74, 0, len(arr), True))

print(binarySearch(arr, 33, 0, len(arr), False))
print(binarySearch(arr, 74, 0, len(arr), False))

############################################################

# bubble sort

def bubbleSort(unsort: list) -> list:
    """bubble sort"""
    arr = unsort.copy()
    last = len(arr) - 1

    for i in range(0, last):
        for j in range(0, last - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap

    return arr

nums = [10, 2, 5, 33, -5, -34, 26, 49, 1]

print(nums)
print(bubbleSort(nums))
