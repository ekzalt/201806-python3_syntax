# списки или массивы (list) в python не типизированные

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

############################################################

# переключение значений переменных

# ВАЖНО! Число элементов спрва и слева от присваивания
# всегда должно соответствовать друг другу!

a = 10
b = 20

a, b = b, a
print(a, b)

a, b = b, a + b
print(a, b)

# то же со списками

numsToSwitch = [10, 20 , 30]
numsToSwitch[0], numsToSwitch[1] = numsToSwitch[1], numsToSwitch[0]
print(numsToSwitch)

# то же со списками словарей

usersToSwitch = [
    { 'name': 'vasya', 'age': 20 },
    { 'name': 'petya', 'age': 30 }
]
usersToSwitch[0], usersToSwitch[1] = usersToSwitch[1], usersToSwitch[0]
print(usersToSwitch)

############################################################

# срезы - item[START_ID = 0 : STOP = length : STEP = 1]

print(arr5[1:2])
print(arr5[2:-2])
print(arr5[-3:-1])
print(arr5[::2])
# реверс массива
print(arr5[::-1])

arrLink = arr5  # other link to arr5
arrCopy = arr5[:]  # copy of arr5

############################################################

# for ... in: циклы + массивы
for x in arr5:
    print(x)

# как получить индексы со значениями
for idx, value in enumerate(arr5):
    print(idx, value)

# if ... in: условные операторы + поиск внутри массива
if 'three' in arr5:
    print('three found :)')
else:
    print('three not found :(')

############################################################

# генераторы списков

# (values) = [ (expression) for (item) in (items) ]
# (values) = [ (expression) for (item) in (items) if (condition) ]

# деструктуризация list, переупаковка в list
sourceNums = [10, 20, 30, 40, 50]
targetNums = [n * n for n in sourceNums]
print(targetNums)

# mapping по списку словарей
user1 = {'name': 'alex', 'car': 'bmw'}
user2 = {'name': 'john', 'car': 'audi'}
user3 = {'name': 'max'}
users = [user1, user2, user3]

# cars = [user['car'] for user in users]  # небезопасно
cars = [user.get('car') for user in users if user.get('car')]  # безопасно
print(cars)

# filter по значениям
names = ['alex', 'john', 'max', 'denis', 'jack']
filteredNames = [name for name in names if name.startswith('j')]
print(filteredNames)

############################################################

# встроенный map, возвращает итератор


def getCar(user: dict) -> str:
    '''getCar'''
    return user.get('car', '')


# userCars = list(map(getCar, users))
userCars = list(map(lambda user: user.get('car', ''), users))
print(userCars)

# встроенный filter, возвращает итератор


def startsWithJ(string: str) -> bool:
    '''startsWithJ'''
    return string.startswith('j')


# userNames = list(filter(startsWithJ, names))
userNames = list(filter(lambda name: name.startswith('j'), names))
print(userNames)

############################################################

# Кортежи (tuple) - неизменяемые массивы, методы те же самые, кроме мутирующих

arrList = [10, 20, 30]
arrTuple = (40, 50, 60)
arrTuple2 = 70, 80, 90

print(arrTuple)
print('arrList size:', arrList.__sizeof__())
print('arrTuple size:', arrTuple.__sizeof__())

############################################################

# unpacking - "распаковка"
# деструктуризация списков (list) и кортежей (tuple)

listItem1, _, listItem3 = arrList
tupleItem1, _, tupleItem3 = arrTuple

print(listItem1, listItem3)
print(tupleItem1, tupleItem3)
