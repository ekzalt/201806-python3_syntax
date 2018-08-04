# объявление класса


class Person:
    # default params
    name = 'Anonymous'
    age = 0

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age


# наследование


class Student(Person):
    course = 1

    def setCourse(self, course):
        self.course = course

    # для переопределения метода достаточно создать в наследнике метод с тем же именем
    def setAge(self, age):
        self.age = age + 100


# constructor в Python


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Важно! Словари (dict) - это ассоциативные массивы в Python, а объекты - это только экземпляры классов!
# Обращение к свойствам словаря через скобочную нотацию myDict['propName'], а объекта - через точечную myInst.propName

p1 = Person()
print(type(p1))
print('name:', p1.name, ', age:', p1.age)

p1.setName('Vasya')
p1.setAge(30)
print('name:', p1.name, ', age:', p1.age)

s1 = Student()
s1.setCourse(2)
s1.setAge(5)  # метод переопределен -> 105
print(type(s1))
print('name:', s1.name, ', age:', s1.age, ', course:', s1.course)

u1 = User('Petya', 20)  # передаем параметры в конструктор
print(type(u1))
print('name:', u1.name, ', age:', u1.age)
