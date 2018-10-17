'''simple module description here'''

# нативная типизация функций в Python 3.5+


def addNums(a: int, b: int) -> int:
    '''calculate sum'''
    return a + b


def printMsg(msg: str) -> None:
    '''prints message'''
    print(msg)


# этот блок вызовется, если файл запустить на исполнение напрямую
if __name__ == '__main__':
    print('This script will run only while calling this file, not while this file was imported as module')
    n1 = 2
    n2 = 4
    printMsg(str(str(n1) + ' + ' + str(n2) + ' = ' + str(addNums(n1, n2))))
