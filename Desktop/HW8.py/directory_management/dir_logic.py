import os

# Создаем папку, если её нет
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Папка создана")

# Список файлов в текущей директории
print("Файлы в папке:", os.listdir("."))

# Узнать текущий путь
print("Я сейчас тут:", os.getcwd())