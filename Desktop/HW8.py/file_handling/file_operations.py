# Запись и чтение файла
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python!\nThis is Practice 6.")

with open("test.txt", "r", encoding="utf-8") as f:
    print("Содержимое файла:")
    print(f.read())

# Добавление (append) текста
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("\nNew line added.")