# режимы чтения файла:
# 'r' - чтение (по умолчанию)
# 'w' - запись, старое содержимое перезаписывается, если файла нет - он создается
# 'x' - создание и запись, если файла нет. Если он есть - исключение
# 'a' - добавление информации в конец файла
# 'b' - чтение в бинарном режиме
# 't' - чтение в текстовом режиме (по умолчанию)
# '+' - чтение и запись

print('\nFile operations:\n')

file1 = open('./text.txt')  # 'rt' as default
data = file1.read()  # read from stream
file1.close()

print(type(data))  # -> str
print(data)

# for line in file1: print(line)  # read line by line

# file2 = open('./text2.txt', 'w')
# file2.write('Hello World')
# file2.close()

############################################################

# Менеджер контекста - with/as - выполняет критические функции

print('\nwith / as:\n')

with open('./text2.txt', 'wt', encoding='utf-8') as file3:
    inputData = input()
    print('inputData:', inputData)
    file3.write(str(inputData + '\n'))
    # file3.close()  # в конструкции with/as срабатывает автоматически
