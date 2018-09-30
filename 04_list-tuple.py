# списки или массивы (list) в python не типизированные

print('\nlist (array):\n')

arr1 = ['zero', 'one']
print(len(arr1))  # arr length

print(arr1[0])  # print first
print(arr1[-1])  # print last

arr1[1] = 'ONE'  # init new value by id

arr1.append('two')  # add to the end
print(arr1)

arr2 = [3, 4]
arr1.extend(arr2)  # concat arr2 to the end
print(arr1)

arr1.insert(4, 'four')  # insert by index
print(arr1)

# del arr1[4]  # remove by id
arr1.remove(4)  # remove by value
print(arr1)
arr1.pop()  # remove and return by index or last one
print(arr1)

print(arr1.index('two'))  # return index of value
print(arr1.count('two'))  # return count of value

arr3 = [4, 1, 10, 6]
arr3.sort()
# arr3.sort(reverse=True)  # сортировка в обратном порядке
print(arr3)

arr3.reverse()
print(arr3)

arr3.clear()
print(arr3)

# автогенерация массива
arr4 = list(range(0, 10, 2))
print(arr4)
# return max and min values
print(max(arr4))
print(min(arr4))

print(sum(arr4))  # встроенная функция суммы

# положительные и отрицательные индексы

arr5 = ['zero', 'one', 'two', 'three', 'four', 'five']
print(arr5[1])  # -> 'one'
print(arr5[-2])  # -> 'two'

# for ... in: циклы + массивы

for x in arr5:
    print(x)

# как получить индексы со значениями

for i, x in enumerate(arr5):
    print(i, x)

# срезы - item[START_ID = 0 : STOP = length : STEP = 1]

print(arr5[1:2])
print(arr5[2:-2])
print(arr5[-3:-1])
print(arr5[::2])

arrLink = arr5  # other link to arr5
arrCopy = arr5[:]  # copy of arr5

# if ... in: условные операторы + поиск внутри массива

if 'three' in arr5:
    print('three found :)')
else:
    print('three not found :(')

# Кортежи (tuple) - неизменяемые массивы, методы те же самые, кроме мутирующих

arrList = [10, 20, 30, 40, 50]
arrTuple = (10, 20, 30, 40, 50)

print(arrTuple)
print('arrList size:', arrList.__sizeof__())
print('arrTuple size:', arrTuple.__sizeof__())
