# Стандартные потоки ввода/вывода

# sys.stdin
# sys.stdout
# sys.stderr

############################################################

# Streams

# режимы чтения файла:
# 'r' - чтение (по умолчанию)
# 'w' - запись, старое содержимое перезаписывается, если файла нет - он создается
# 'x' - создание и запись, если файла нет. Если он есть - исключение
# 'a' - добавление информации в конец файла
# 'b' - чтение в бинарном режиме
# 't' - чтение в текстовом режиме (по умолчанию)
# '+' - чтение и запись

pathToReadFile = './text.txt'
readStream = open(pathToReadFile)  # 'rt' as default
data = readStream.read()  # read from stream

# читаем частями но n (1024) байт, 1kb, полезно для пайпа
# data2 = readStream.read(1024)
# data3 = readStream.read(1024)
# data4 = readStream.read(1024)

print(data)
# после всех операций закрываем stream
readStream.close()

############################################################

# получим массив строк

readStream = open('./text.txt', 'r')
lines = readStream.readlines()
readStream.close()

print(lines)

############################################################

# read line by line

readStream = open('./text.txt')  # 'rt' as default

for line in readStream:
    print(line.strip())  # обрежем пробелы и переводы строк

readStream.close()

# получим дополнительно индексы строк

readStream = open('./text.txt')  # 'rt' as default

for i, line in enumerate(readStream):
    print(i, line.strip())

readStream.close()

############################################################

# запись в файл

pathToWriteFile = './output.txt'
writeStream = open(pathToWriteFile, 'w')
writeStream.write('Hello World')
writeStream.close()

# pipe streams - read to write - читаем и пишем

pathToReadFile = './text.txt'
pathToWriteFile = './output.txt'

readStream = open(pathToReadFile, mode='r', encoding='utf-8')
writeStream = open(pathToWriteFile, mode='w', encoding='utf-8')

for i, line in enumerate(readStream, 1):
    # do some with data
    writeStream.write(str(i) + ' : ' + line.strip() + '\n')

readStream.close()
writeStream.close()

############################################################

# Менеджер контекста - with/as - выполняет критические функции

print('\nwith / as:\n')

with open('./text2.txt', 'wt', encoding='utf-8') as file3:
    inputData = input()
    print('inputData:', inputData)
    file3.write(str(inputData + '\n'))
    # file3.close()  # в конструкции with/as срабатывает автоматически
