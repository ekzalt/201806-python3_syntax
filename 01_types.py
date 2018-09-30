# вызов функции
print('\nmath operations:\n')

print(6 + 2)
print(6 - 2)
print(6 / 2)
print(6 // 2)  # деление без остатка
print(6 * 2)
print(6 ** 2)  # возведение в степень
print(7 % 2)  # остаток от деления

############################################################

# объявление переменой

print('\ndefine variables:\n')

# типы данных

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
