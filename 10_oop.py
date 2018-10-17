class Person:
    """Person class"""
    # статические свойства класса
    name = 'Anonymous'
    age = 0

    # метод класса
    # может использовать только класс
    @classmethod
    def printType(cls) -> None:
        """class - print class type"""
        print(type(cls))

    # статический метод класса
    # может использовать и класс и инстанс
    @staticmethod
    def printInfo() -> None:
        """static - print user info"""
        print(Person.name, Person.age)

    # метод инстанса
    # может использовать только инстанс
    def setName(self, name: str) -> None:
        """set name"""
        self.name = name

    def setAge(self, age: int) -> None:
        """set age"""
        self.age = age


# Важно! Словари (dict) - это ассоциативные массивы в Python, а объекты - это только экземпляры классов!
# Обращение к свойствам словаря через скобочную нотацию myDict['propName'], а объекта - через точечную myInst.propName

print(Person.name, Person.age)
Person.printType()
Person.printInfo()

p1 = Person()
p1.setName('Vasya')
p1.setAge(30)
print(p1.name, p1.age)

############################################################

# constructor в Python


class User:
    """User class"""

    def __init__(self, name: str, age: int):
        """constructor"""
        self.name = name
        self.age = age
        # default params
        self.health = 100

    def printInfo(self) -> None:
        """print user info"""
        print(self.name, self.age)


u1 = User('Petya', 20)  # передаем параметры в конструктор
u1.printInfo()

############################################################

# наследование с конструктором


class SuperUser(User):
    """SuperUser extends User"""

    def __init__(self, name: str, age: int, role: str):
        """constructor"""
        super().__init__(name, age)
        # _propName - создание служебного свойства (доступно)
        # __propName - создание приватного свойства (скрыто)
        self.__role = role

    # переопределение метода
    def printInfo(self) -> None:
        """print user info"""
        print(self.name, self.__role)

    # геттер
    @property
    def role(self) -> str:
        """get SuperUser role"""
        return self.__role

    # сеттер
    @role.setter
    def role(self, role: str) -> None:
        """set SuperUser role"""
        self.__role = role


su1 = SuperUser('Vasya', 30, 'user')
su1.printInfo()
print(su1.role)
su1.role = 'admin'
print(su1.role)

# описание класса
print(type(su1))
print(su1.__class__)

# кортеж его классов-родителей
print(SuperUser.__bases__)

# является ли этот объект инстансом этого класса
print(isinstance(su1, SuperUser))

# является ли этот класс наследником этого родительского класса
print(issubclass(SuperUser, User))

# .mro() - вернет массив со всей иерархией наследования


def checkInstance(inst: object, cls: object) -> bool:
    '''checkInstance'''
    return cls in type(inst).mro()


def checkSubClass(child: object, parent: object) -> bool:
    '''checkSubClass'''
    return parent in child.mro()


print(checkInstance(su1, SuperUser))
print(checkSubClass(SuperUser, User))

############################################################

# "магические методы", методы-перехватчики


class PasswordChecker:
    def __init__(self):
        self.password = None

    # метод-перхватчик __getattribute__
    def __getattribute__(self, attr):
        if attr == 'secretKey' and self.password == '123':
            return 'secretValue'
        else:
            return object.__getattribute__(self, attr)

    # метод-перехватчик вызовется перед удалением объекта из памяти
    def __del__(self):
        print(self, 'will be deleted from memory')


pch = PasswordChecker()
# print(pch.secretKey)  # AttributeError
pch.password = '123'
print(pch.secretKey)

############################################################

# pattern Singleton


class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self):
        self.data = 1234567890


############################################################

# метаклассы


# создаем класс такого типа с помощью метакласса type
class SomeOne:
    '''SomeOne'''
    attr = 42


# name - имя готового класса
# bases - кортеж классов родителей
# attrs - словарь атрибутов
name, bases, attrs = 'SomeTwo', (), {'attr': 42}
SomeTwo = type(name, bases, attrs)

print(SomeOne)
print(SomeTwo)

some1 = SomeOne()
some2 = SomeTwo()

print(some1.attr)
print(some2.attr)


# 1. создаем собственный метакласс и наследуем от type
class MetaSome(type):
    '''MetaSome'''
    # создаем метод метакласса, не будет доступен в инстансе
    def somePrint(cls) -> None:
        '''somePrint'''
        print('prints something')


# 2. наследуемся от нашего метакласса (type по умолчанию)
class SomeThree(metaclass=MetaSome):
    '''SomeThree'''
    attr = 42


SomeThree.somePrint()
some3 = SomeThree()
print(some3.attr)
# some3.somePrint()  # AttributeError
