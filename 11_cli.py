# аргументы командной строки

import sys

# массив - имя файла и остальные аргументы
print(sys.argv)

if len(sys.argv) > 1:
    print(sys.argv[1:])
else:
    print('no args')
    sys.exit(1)  # завершение процесса с кодом ошибки

############################################################

# запуск bash комманд с помощью Python

import os

os.system('ls')
