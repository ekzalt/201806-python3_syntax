# binary search

def binarySearchRec(sort: list, target: int, start: int, stop: int, value: bool):
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
            return binarySearchRec(sort, target, start, mid - 1, value)
        else:
            return binarySearchRec(sort, target, mid + 1, stop, value)


arr = range(0, 1000000)[::2]

print(binarySearchRec(arr, 222222, 0, len(arr), True))
print(binarySearchRec(arr, 777777, 0, len(arr), True))

print(binarySearchRec(arr, 222222, 0, len(arr), False))
print(binarySearchRec(arr, 777777, 0, len(arr), False))


def binarySearchLoop(sort: list, target: int, start: int, stop: int, value: bool):
    """binary search with while"""
    
    while start <= stop:
        mid = (start + stop) // 2
    
        if target == sort[mid]:
            if value:
                return sort[mid]
            else:
                return mid
        elif target < sort[mid]:
            stop = mid - 1
        else:
            start = mid + 1
    else:
        if value:
            return None
        else:
            return -1


arr = range(0, 1000000)[::2]

print(binarySearchLoop(arr, 222222, 0, len(arr), True))
print(binarySearchLoop(arr, 777777, 0, len(arr), True))

print(binarySearchLoop(arr, 222222, 0, len(arr), False))
print(binarySearchLoop(arr, 777777, 0, len(arr), False))

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
