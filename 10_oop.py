# объявление класса


class Person:
    """Person class"""
    # default params
    name = 'Anonymous'
    age = 0

    def setName(self, name: str) -> None:
        """set name"""
        self.name = name

    def setAge(self, age: int) -> None:
        """set age"""
        self.age = age


# Важно! Словари (dict) - это ассоциативные массивы в Python, а объекты - это только экземпляры классов!
# Обращение к свойствам словаря через скобочную нотацию myDict['propName'], а объекта - через точечную myInst.propName

p1 = Person()
print(type(p1))
print('name:', p1.name, ', age:', p1.age)

p1.setName('Vasya')
p1.setAge(30)
print('name:', p1.name, ', age:', p1.age)

# наследование в Python


class Student(Person):
    """Student extends Person"""
    # default params
    course = 1

    def setCourse(self, course: int) -> None:
        """unique student method"""
        self.course = course

    # для переопределения метода достаточно создать в наследнике метод с тем же именем
    def setAge(self, age: int) -> None:
        """override parent method"""
        self.age = age + 100


s1 = Student()
s1.setCourse(2)
s1.setAge(5)  # метод переопределен -> 105
print(type(s1))
print('name:', s1.name, ', age:', s1.age, ', course:', s1.course)

# constructor в Python


class User:
    """User class"""

    def __init__(self, name: str, age: int):
        """constructor"""
        self.name = name
        self.age = age
        # default params
        self.health = 100


u1 = User('Petya', 20)  # передаем параметры в конструктор
print(type(u1))
print('name:', u1.name, ', age:', u1.age, ', health:', u1.health)

# наследование с конструктором


class SuperUser(User):
    """SuperUser extends User"""

    def __init__(self, name: str, age: int, role: str):
        """constructor"""
        super().__init__(name, age)
        # __propName - создание приватного свойства
        self.__role = role

    def setRole(self, role: str) -> None:
        """set SuperUser role"""
        self.__role = role

    def getRole(self) -> str:
        """get SuperUser role"""
        return self.__role


su1 = SuperUser('Vasya', 30, 'user')

print(type(su1))
print('name:', su1.name, ', age:', su1.age, ', health:', su1.health)

su1.setRole('admin')
print(su1.getRole())
