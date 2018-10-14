# Словари (dict) - ассоциативные массивы (PHP), объекты (javaScript)

user1 = {
    'name': 'Vasya',
    'age': 30
}

print(user1)
# бросит ошибку, если такого ключа нет
print(user1['name'])
# вернет None, если такого ключа нет
print(user1.get('name'))
# get принимает вторым аргументом default значение
print(user1.get('sex', 'male'))
# бросит ошибку, если такого ключа нет
print(user1['sex'])

# присвоение нового свойства или перезапиcь свойства новым значением
user1['job'] = 'developer'
# удаление свойства
del user1['job']

print(user1.keys())
print(user1.values())
print(user1.items())

# dict.popitem() - удаляет пару ключ-значение
# dict.setdefault(key, default) - возвращает значение, если есть, или устанавливает, если его нет
# dict.update([other]) - обновляет словарь, добавляя пары ключ-значение из [other]. Существующие ключи перезаписываются
# dict.copy() - возвращает копию словаря (ссылка на другую ячейку памяти)

user2 = dict(name='Petya', age=20)

user3 = dict([('name', 'Masha'), ('age', 10)])

user4 = dict.fromkeys(['name', 'message'], 'default')
print(user4)
user4.clear()
print(user4)

# собираем словарь из списков ключей и значений
user5 = dict(zip(['name', 'age'], ['Igor', 40]))
print(user5)

############################################################

# генераторы списков - итерация по словарю

filteredKeys = [key for (key, value) in user5.items() if value is not None]
filteredValues = [value for (key, value) in user5.items() if value is not None]
print(filteredKeys)
print(filteredValues)

############################################################

# JSON

import json

player1 = {
    'nickname': 'Lex',
    'rank': 10,
}

player2 = {
    'nickname': 'Pit',
    'rank': 15,
}

players = [player1, player2]

# пишем в JSON

pathToJson = './players.json'
writeStream = open(pathToJson, 'w', encoding='utf-8')
json.dump(players, writeStream)
writeStream.close()

# читаем из JSON

readStream = open('./players.json', 'r', encoding='utf-8')
playersData = json.load(readStream)

for player in playersData:
    print(player['nickname'])
