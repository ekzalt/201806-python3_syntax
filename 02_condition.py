# условные операторы

print('\nconditional operators:\n')

myInt = 100  # int
myBoolTrue = True  # bool
myBoolFalse = False  # bool

if myBoolTrue:
    print('start operation')
    # do some
    print('end operation')  # многострочный блок в Python

if myBoolFalse:
    print('myBoolFalse is false :)')
else:
    print('myBoolFalse is true o_O')

if myInt > 50:
    print('myInt more 50, it is', myInt)

    if (myInt > 75):  # вложенный блок в Python
        print('It is more 75')
    else:
        print('It is less than 75')
elif myInt == 50:
    print('myInt is equal to 50', myInt)
elif (myInt < 50) and (myInt >= 0):  # использование and / or в условных операторах
    print('myInt is less than 50', myInt)
else:
    print('myInt is less than 0', myInt)


# тренарный оператор

userInput = input('Enter your name: ')

userName = userInput if userInput else 'Anonymous'

print(userName)
