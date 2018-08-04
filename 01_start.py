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

# name = input('What is your name? ')
# print('Hello', name)

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

# условные операторы

print('\nconditional operators:\n')

if myBoolTrue:
    print('yes')
    print('yes')  # многострочный блок

if myBoolFalse:
    print('no')
else:
    print('nooo!!!')

if myInt > 50:
    print('myInt more 50, it is', myInt)

    if myInt > 75:
        print('It is more 75')
    else:
        print('It is less than 75')
elif myInt == 50:
    print('myInt is equal to 50', myInt)
else:
    print('myInt is less than 50', myInt)

# тренарный оператор

# userInput = input('Enter your name: ')
userInput = ''
userName = userInput if userInput else 'Anonymous'
print(userName)

############################################################

# циклы

print('\ncycles while, for:\n')

i = 0
while i < 5:
    print('i:', i)
    if i == '10':
        break
    i += 1
else:  # опциональный else
    print('No 10 in while')

for j in userName:
    # print(j.upper(), end = '')
    if j == 'n':
        continue
    # if j == 'y': break
    if j == 'd':
        break
    print(j.upper())
else:  # опциональный else
    print('No \'d\' in string:', userName)

for v in range(5):
    print('range:', v)

############################################################

# списки или массивы (list) в python не типизированные

print('\nlist (array):\n')

arr1 = ['zero', 'one']
arr1.append('two')  # add to the end
print(arr1)

arr2 = [3, 4]
arr1.extend(arr2)  # concat arr2 to the end
print(arr1)

arr1.insert(4, 'four')  # insert by index
print(arr1)

arr1.remove(4)  # remove first found elem
print(arr1)

arr1.pop()  # remove by index or last one
print(arr1)

print(arr1.index('two'))  # return index of value
print(arr1.count('two'))  # return count of value

arr3 = [4, 1, 10, 6]
arr3.sort()
print(arr3)

arr3.reverse()
print(arr3)

arr3.clear()
print(arr3)

# положительные и отрицательные индексы

arr1 = ['zero', 'one', 'two', 'three']
print(arr1[1])  # -> 'one'
print(arr1[-2])  # -> 'two'

# срезы - item[START = 0 : STOP = length : STEP = 1]

print(arr1[1:2])
print(arr1[::2])

# Кортежи (tuple) - неизменяемые массивы, методы те же самые, кроме мутирующих

arrList = [10, 20, 30, 40, 50]
arrTuple = (10, 20, 30, 40, 50)

print(arrTuple)
print('arrList size:', arrList.__sizeof__())
print('arrTuple size:', arrTuple.__sizeof__())

############################################################

# Словари (dict) - ассоциативные массивы (PHP), объекты (javaScript)

print('\ndict (associative arrays, objects):\n')

user1 = {'name': 'Vasya', 'age': 30}
print(user1)
print(user1['name'])
print(user1.keys())
print(user1.values())
print(user1.items())

# dict.popitem() - удаляет пару ключ-значение
# dict.setdefault(key, default) - возвращает значение, если есть, или устанавливает, если его нет
# dict.update([other]) - обновляет словарь, добавляя пары ключ-значение из [other]. Существующие ключи перезаписываются
# dict.copy() - возвращает копию словаря

user2 = dict(name='Petya', age=20)

user3 = dict([('name', 'Masha'), ('age', 10)])

user4 = dict.fromkeys(['name', 'message'], 'default')
print(user4)
user4.clear()
print(user4)

############################################################

# Множества (set и frozenset) - нет повторяющхся элементов, выводятся в случайном порядке

print('\nset:\n')

set1 = set('aabbcc')
set1.add('d')  # add 'd' to set1
print(set1)
print('set1 length:', len(set1))
print('is \'a\' in set1:', 'a' in set1)

set1Equal = set('abcd')
print('is set1 equal to set1Equal:', set1 == set1Equal)

set2 = set([1, 1, 2, 2, 3, 3])
print(set2)
print('no equal elems in both sets:', set1.isdisjoint(set2))

# set1.intersection_update(set2) -> intersection set
# set1.difference_update(set2) -> difference set
# set1.symmetric_difference_update(set2)

set3 = {'e', 'f', 'g', 'h', 'i', 'j'}
print(set3)
set3.remove('j')  # remove 'g' from set3 - return Error if no 'g' in set3
set3.discard('i')  # remove 'f' from set3, no errors
print('remove and return random elem from set3:', set3.pop())
print(set3)

set1.update(set3)
print('set1 was updated with set3:', set1)

set4 = {i ** 2 for i in range(5)}
print(set4)
set4.clear()
print(set4)

frozenset1 = frozenset([10, 20, 30])
print(frozenset1)

############################################################

# Функции (def, lambda)

print('\nfunctions:\n')


def typeChecker(arg):  # объявление функции
    print('typeChecker: type:', type(arg), ', value:', arg)
    pass  # -> None , в других языках - return void


print('type of def function:', type(typeChecker))
print('value of def function:', typeChecker)
print(typeChecker(123))

# closure - замыкания в Python


def closureSum(a=0):  # аргументы по умолчанию
    def add(b=0):
        return a + b
    return add


print(closureSum(2)(3))


def iterateArgs(*tup):  # type 'tup' = tuple (frozen array) - одна *
    print('type:', type(tup), ', value:', tup)
    res = 0

    for i in tup:
        res += i

    return res


print(iterateArgs(1, 2, 3))


def getUser(**obj):  # type 'obj' = dict (JS Object) - две **
    print('type:', type(obj), ', value:', obj)
    return obj


print(getUser(name='Vasya', age=30))

# lambda - короткие анонимные функции

print('type of lambda function:', type(lambda a, b: a + b))
print('value of lambda function:', lambda a, b: a + b)

print((lambda a, b: a * b)(3, 4))
print((lambda *tup: tup)(3, 4, 5))
print((lambda **obj: obj)(name='Masha', age=10))

############################################################

# try/except/[else]/[finally] - отлов ошибок в Python


def tryDivide(a, b):
    res = 0

    try:
        n1 = int(a)
        n2 = int(b)
        res = n1 / n2
        return int(res)
    except ValueError:
        print('one of arguments is not a number:', a, b)
        return 0
    except ZeroDivisionError:
        print('one of arguments is 0:', a, b)
        return 0
    # else:  # опционально, если except не сработал
    # finally:  # опционально, блок сработает всегда


print(tryDivide(12, 2))  # -> 6

############################################################

# Декораторы (замедляют вызов функций)


def decorate(func):
    def wrapper(a, b):
        print('code before function')
        res = func(a, b)
        print('code after function')
        return res
    return wrapper


decorated = decorate(tryDivide)
print(decorated(20, 5))  # -> 4

print(decorate(tryDivide)(15, 3))  # -> 5

# аннотация декораторов как в Angular :)


@decorate  # @decoratorName
def multiple(a, b):
    return a * b


print(multiple(10, 4))  # -> 40

# К одной функции можно применять несколько декораторов
# @decorator1
# @decorator2
# @decorator3
# def funcToDecore(): ...
