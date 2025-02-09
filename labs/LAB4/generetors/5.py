def countdown(n):
    for i in range(n, -1, -1):
        yield i  # Генерирует числа в обратном порядке

# Вводим n
n = int(input("Введите n: "))

# Выводим числа от n до 0
for num in countdown(n):
    print(num, end=" ")