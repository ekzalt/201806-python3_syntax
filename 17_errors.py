# try/except/[else]/[finally] - отлов ошибок в Python

# Основные виды исключений
# ImportError - ошибка импорта модуля
# IndexError - несуществующий индекс массива
# NameError - обращение к несуществующей переменной
# SyntaxError - ошибка синтаксиса
# TypeError - ошибка типизации
# ValueError - ошибка значения

############################################################

# импорт встроенного модуля
import sys


def tryDivide(a: int, b: int) -> float:
    """divides numbers"""
    div = 0

    try:
        if a > 1000 or b > 1000:
            raise ValueError('Too much')  # вброс своего исключения со своим сообщением
        div = a / b
        return div
    except TypeError:
        print(sys.exc_info()[1])
        # типа как process.exit() в Node.js
        # sys.exit(1)
        return 0
    except ZeroDivisionError:  # множественный except
        print(sys.exc_info()[1])
        return 0
    except (IndexError, NameError):  # группировка исключений
        print(sys.exc_info()[1])
        return 0
    except Exception:  # отлов любого исключения
        print(sys.exc_info()[1])
        return 0
    # else:
        # опционально, если ошибок не было
    # finally:
        # опционально, блок сработает всегда


print(tryDivide(12, '2'))

############################################################

# Типизация ошибок - свои исключения - наследуем класс Exception

class CustomError(Exception):
    '''CustomError'''
    # custom Exception params
    pass
