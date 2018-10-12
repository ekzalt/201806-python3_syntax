# 201806-python3_syntax

https://www.python.org/

PIP - пакетный менеджер Python
PyPi - репозиторий библиотек Python

```bash

# check python version
python --version

```

## Информация на русском

Инфа для изучения языка
https://habrahabr.ru/post/150302/

Интерактивный учебник основам программироания на Python
http://pythontutor.ru/

## Направления

### Python Web Frameworks

- Django,
- Flask,
- Web2Py,
- CherryPy,
- Pyramid,
- Tornado,
- TurboGears

### AWS development

- Boto 3

https://boto3.readthedocs.io/en/latest/
https://github.com/boto/boto3
https://aws.amazon.com/ru/sdk-for-python/

### Приложения для научных расчетов

- NumPy,
- SciPy

### Приложения для Decktop

- tkinter,
- PyQt,
- wxPython

### Мобильные приложения

- kivy

### Приложения для игр

- PyGame

*PyGame* - Приложение для написания игр и мультимедиа приложений. Базируется на мультимедийной библиотеке *SDL*.
https://www.pygame.org/news

## PIP - пакетный менеджер Python

- `pip` - общая справка
- `pip help <commandName>` - справка о конкретной команде
- `pip search <key words>` - поск в репозиториях *pip* по ключевым словам
- `pip list` [ -o | --outdated ] - список установленных пакетов
- `pip show <packageName>` - основная информация про пакет
- `pip check` - проверка не установленных зависимостей
- `pip freeze > requirements.txt` - вывод установленных зависимостей
- `pip install <packageName>` - установка пакета по имени
- `pip install -r requirements.txt` - установка пакетов по именам из файла
