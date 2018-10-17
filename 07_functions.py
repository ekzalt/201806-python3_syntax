# Функции (def, lambda)


def typeChecker(arg):  # объявление функции
    print('typeChecker: type:', type(arg), ', value:', arg)
    pass  # -> None , в других языках - return void


print(typeChecker(123))

# использование assert для проверки значений аргументов
# выбросит AssertionError


def logger(msg: str) -> None:
    '''logger'''  # это многострочный комментарий docstring - хранится в атрибуте функции .__doc__
    assert msg != ''
    # может принимать второй аргумент - сообщение об ошибке
    # assert number > 0, 'Integer shold be more than zero'
    print(msg)
    pass


logger('hello')
logger('')

############################################################

# глобальная область видимости

сounter = 0


def increment() -> None:
    '''increment'''
    # так будет ошибка - UnboundLocalError!
    # создаст локальную переменную!
    # сounter += 1

    # указываем, что изменяем глобальную переменную
    global сounter
    сounter += 1


increment()
print(сounter)

############################################################

# closure - замыкания в Python


def closureSum(a=0):  # аргументы по умолчанию
    def add(b=0):
        return a + b
    return add


print(closureSum(2)(3))


# изменим переменную из замыкания
# лучше использовать класс Cell для хранения состояния
def cell(value=None):
    '''cell'''

    def getCell():
        '''getCell'''
        return value

    def setCell(update):
        '''setCell'''
        # обращаемся к перемнной из замыкания
        nonlocal value
        value = update

    return getCell, setCell


getCell, setCell = cell()
setCell(10)
print(getCell())

############################################################

# *args, **kwargs


# *args - tuple
def iterateArgs(*args):
    '''iterateArgs'''
    print('type:', type(args), ', value:', args)
    result = 0

    for val in args:
        result += val

    return result


# *args - альтернатива ...rest Array оператора в JavaScript
print(iterateArgs(1, 2, 3))
# деструктуризация list, переупаковка в tuple
print(iterateArgs(*[1, 2, 3]))


# **kwargs - dict
def getUser(**obj):
    '''getUser'''
    print('type:', type(obj), ', value:', obj)
    return obj


# альтернатива ...rest Object оператора в JavaScript
print(getUser(name='Vasya', age=30))
# деструктуризация dict, переупаковка в dict
print(getUser(**{'name': 'Vasya', 'age': 30}))

############################################################

# нативная типизация функций в Python 3.5+


def addNums(a: int, b: int) -> int:
    """calculate sum"""  # add definition
    return a + b


def printMsg(msg: str) -> None:
    """prints message"""
    print(msg)


############################################################

# lambda - короткие анонимные функции

print('type of lambda function:', type(lambda a, b: a + b))
print('value of lambda function:', lambda a, b: a + b)

print((lambda a, b: a * b)(3, 4))
print((lambda *tup: tup)(3, 4, 5))
print((lambda **obj: obj)(name='Masha', age=10))

############################################################

# try/except/[else]/[finally] - отлов ошибок в Python

# импорт встроенного модуля
import sys


def tryDivide(a: int, b: int) -> float:
    """divides numbers"""
    div = 0

    try:
        div = a / b
        return div
    except TypeError:
        print('one of arguments is not a number:', a, type(a), b, type(b))

        # типа как process.exit() в Node.js
        print(sys.exc_info()[1])
        # sys.exit(1)

        return 0
    except ZeroDivisionError:
        print('one of arguments is 0:', a, b)
        print(sys.exc_info()[1])
        return 0
    # else:
        # опционально, если except не сработал
    # finally:
        # опционально, блок сработает всегда


print(tryDivide(12, '2'))

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
print(decorated(20, 5))
print(decorate(tryDivide)(15, 3))


@decorate  # @decoratorName
def multiple(a, b):
    return a * b


print(multiple(10, 4))  # -> 40

# К одной функции можно применять несколько декораторов
# @decorator1
# @decorator2(args) - декораторы тоже принимают аргументы :)
# @decorator3
# def funcToDecore(): ...

############################################################

# Генераторы


def countdown(n: int) -> int:
    '''generator countdown'''
    while n != 0:
        n -= 1
        yield n


gen1 = countdown(2)
print(next(gen1))
print(next(gen1))
# print(next(gen))  # StopIteration error

# итераторы и генераторы
for n in countdown(4):
    print(n)

# создание генератора из списка
listGen = (x for x in [10, 20, 30])

for x in listGen:
    print(x)


# создание генератора для чтения файла
def getLine(filePath: str) -> str:
    '''getLine'''
    readStream = open(filePath, 'r')

    for line in readStream:
        yield line.strip()

    readStream.close()


for line in getLine('./text.txt'):
    print(line)


# генератор Фибоначи
def fiboGen(a=1, b=2, limit=10) -> int:
    '''fiboGen'''
    for _ in range(limit):
        a, b = b, a + b
        yield b


print(list(fiboGen()))


# генератор счетчик
def counterGen(limit=10) -> int:
    '''counterGen'''
    i = 0

    while True:
        yield i
        i += 1

        if i > limit:
            raise StopIteration()


# создание генераторов из итерируемых типов

genStr = iter('hello world')
genSet = iter({40, 50, 60})

nums = [10, 20, 30]
genList1 = iter(nums)
genList2 = nums.__iter__()

user = {'name': 'vasya', 'age': 30}
genDict1 = iter(user)
genDict2 = user.__iter__()


# yield from - делегирование вызова другому генератору
def chain(*iterables):
    '''chain'''
    for iterable in iterables:
        yield from iterable


############################################################

# coroutines in Python


# генератор также может принимать данные
def genGrep(pattern: str):
    '''genGrep'''
    print('pattern:', pattern)

    while True:
        try:
            line = yield

            if pattern in line:
                print(line)
        except Exception as error:
            print(str(error))


gen = genGrep('oops')
# перематываем до принимающего yield
next(gen)
gen.send('hello world')
gen.send('oops i did this again')
# также в генератор можно вброcить исключение
gen.throw(ValueError, 'some error message here')

import functools


# создаем coroutine decorator - теперь next не нужно вызывать
def coroutine(genFunc):
    '''coroutine'''

    @functools.wraps(genFunc)
    def wrapper(*args, **kwargs):
        '''wrapper'''
        gen = genFunc(*args, **kwargs)
        next(gen)
        return gen

    return wrapper


@coroutine
def grep(pattern: str):
    '''grep'''
    print('pattern:', pattern)
    while True:
        try:
            line = yield
            if pattern in line:
                print(line)
        except Exception as error:
            print(str(error))


gen = grep('oops')
gen.send('hello world')
gen.send('oops i did this again')
gen.throw(ValueError, 'some error message here')
