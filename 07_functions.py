# Функции (def, lambda)


def typeChecker(arg):  # объявление функции
    print('typeChecker: type:', type(arg), ', value:', arg)
    pass  # -> None , в других языках - return void


print(typeChecker(123))

# использование assert для проверки значений аргументов
# выбросит AssertionError


def logger(msg: str) -> None:
    '''logger'''
    assert msg != ''
    # может принимать второй аргумент - сообщение об ошибке
    # assert number > 0, 'Integer shold be more than zero'
    print(msg)
    pass


logger('hello')
logger('')

############################################################

# closure - замыкания в Python


def closureSum(a=0):  # аргументы по умолчанию
    def add(b=0):
        return a + b
    return add


print(closureSum(2)(3))


# *args - tuple
def iterateArgs(*rest):
    '''iterateArgs'''
    print('type:', type(rest), ', value:', rest)
    result = 0

    for val in rest:
        result += val

    return result


# *rest - альтернатива ...rest Array оператора в JavaScript
print(iterateArgs(1, 2, 3))
# деструктуризация list, переупаковка в tuple
print(iterateArgs(*[1, 2, 3]))


# **kwargs (key-value-args) - dict
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
print(decorated(20, 5))  # -> 4

print(decorate(tryDivide)(15, 3))  # -> 5

# аннотация декораторов как в Angular :)


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
