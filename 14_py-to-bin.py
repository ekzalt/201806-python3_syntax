# Конвертирование .py в Linux bin

# 1.Устанавливаем и обновляем библиотеки Пайтона:
# sudo apt-get install --reinstall python-pkg-resources
# sudo apt-get install build-essential python-dev

# 2.Качаем PyInstaller:
# wget https://github.com/pyinstaller/pyinstaller/releases/download/v3.2/PyInstaller-3.2.tar.gz

# 3.Раcпаковываем PyInstaller:
# tar -xvf PyInstaller-3.2.tar.gz

# 4.Заходим в распакованный PyInstaller:
# cd PyInstaller-3.2

# 5.Устанавливаем PyInstaller:
# ./pyinstaller.py setup.py

# 6.Конвертим ваш .py файл:
# ./pyinstaller.py --onefile myscript.py

# Ваш бинарный байл будет в /PyInstaller-3.2/myscript/dist
