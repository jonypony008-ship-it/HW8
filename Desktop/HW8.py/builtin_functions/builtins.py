# Примеры встроенных функций
nums = [1, 2, 3, 4, 5]

# map - возводит всё в квадрат
squared = list(map(lambda x: x**2, nums))
# filter - оставляет только четные
evens = list(filter(lambda x: x % 2 == 0, nums))

print(f"Квадраты: {squared}")
print(f"Четные: {evens}")

# zip - объединяет два списка
names = ["Alice", "Bob"]
scores = [85, 90]
combined = list(zip(names, scores))
print(f"Объединение: {combined}")