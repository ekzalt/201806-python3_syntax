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
