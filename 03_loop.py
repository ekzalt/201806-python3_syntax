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
