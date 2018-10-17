# матеметические операции
print(6 + 2)
print(6 - 2)
print(6 / 2)
print(6 // 2)  # деление без остатка
print(6 * 2)
print(6 ** 2)  # возведение в степень
print(7 % 2)  # остаток от деления

############################################################

# типы данных

# в Python нет примитивов,
# все типы данных являются объектами,
# наследниками общего класса object

# объявление переменой
myInt = 100  # int
myFloat = 99.99  # float
myString = 'Text'  # str
myBoolTrue = True  # bool
myBoolFalse = False  # bool
myList = [1, 2, 3]  # list
myTuple = (11, 22, 33)  # tuple
myDict = {'number': 123}  # dict
mySet = set()  # set
myFrozenset = frozenset([10, 20, 30])  # frozenset

print(myInt, myFloat, myString, myBoolTrue,
      myBoolFalse, myList, myTuple, myDict, mySet, myFrozenset)

# узнать тип данных

print('\nreturn type:\n')

print('myInt type:', type(myInt))  # -> <class 'int'>

# удаление переменой

del myFloat

# преобразование типов: int(), float(), str()

print('\nconvert types:\n')

print(int('3') + int('2'))  # += -= *= /=
print(bool(123))
print(list('list'))
print(tuple('tuple'))

myString *= 5  # сконкатенирует строку 5 раз

print(myString)

# сравнения типов

print(myInt == 100)  # > < >= <= !=
print(myInt != 100)

############################################################

# Строки

firstName = 'vasya'
lastName = 'pupkin'
# конкатенация строк
fullName = 'vasya' + ' ' + 'pupkin'
# методы строк
print(fullName.upper())
print(fullName.title())
print(fullName.capitalize())

# %s - string
# %d - integer
# %f - float
print('Hi, %s %s' % (firstName, lastName))

# форматированная строка
print('Hi, {} {}'.format(firstName, lastName))
# именные аргументы
print('Hi, {first} {last}'.format(first=firstName, last=lastName))
# обращаемся к массиву аргументов по индексам
print('{0} {1} {1} {0}'.format(firstName, lastName))
# поддерживает словари

# строки так же поддерживают обращение по индексу и срезы
pyStr = 'python'
print(pyStr[0])
print(pyStr[1:-1])

# строки поддерживают оператор in
res = '{"status": "400", "message": "Error"}'
isError = 'error' in res.lower()

if isError:
    print('Got error from server')

# байтовые строки (бинарные данные)
byteStr = b'byte string'
print(byteStr.decode('utf-8'))
