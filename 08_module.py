# Python поддерживет модули на языках: Python, C, C++

# import math, time, os
import math
import time
import os
import random as rand  # use alias

import my_mod as mod  # import custom module
from my_mod import printMsg as pm  # import function from module

# from my_mod import addNums, printMsg  # import list of functions from module
# from my_mod import (addNums, printMsg)  # import list of functions from module

try:
    import nomodule
except ImportError:
    print('ImportError: No module \'nomodule\'')

# число PI
print(math.pi)
# текущее время в секундах
print(time.time())
# текущая папка
print(os.getcwd())
# переменные окружения
print(os.environ)
print(os.environ['OS'])
# случайное число от 0 до 1
print(rand.random())

print('this is \'mod\' module inner properties:')
print(dir(mod))

print(mod.addNums(1, 2))
mod.printMsg('my_mod hello!')
pm('printMsg hello!')
