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


userName = 'Admin'

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

# итераторы и генераторы

# "итерабельные" объекты должны реализовать один или оба метода:
# __iter__(self) - возвращает объект-итератор с методом __next__()
# __getitem__() - позволяет получить значения по индексу - через [] квадратные скобки

# итератор должен реализовать метод __next__()
# если данных больше нет,
# итератор должен выбросить исключение StopIteration

# поэтому "итерабельные объекты" - многоразовые
# а "итераторы" - одноразовые

nums = [10, 20, 30]
numsIterator = iter(nums)
# print(next(numsIterator))

# перебор значений итератора через while
while True:
    try:
        value = next(numsIterator)
        # do some
        print(value)
    except StopIteration:
        break

############################################################


def iterate(iterable, callback) -> None:
    '''iterate'''
    iterator = iter(iterable)

    while True:
        try:
            value = next(iterator)
            callback(value)
        except StopIteration:
            break


def logger(value) -> None:
    '''logger'''
    print('value:', value)


iterate(range(10), logger)

############################################################


class RangeIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.value = None

    def __iter__(self):
        return self

    def __next__(self):
        pass
