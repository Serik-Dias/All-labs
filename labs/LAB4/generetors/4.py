def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2  # Возвращает квадрат числа

# Вводим диапазон
a = int(input("Введите a: "))
b = int(input("Введите b: "))

# Используем генератор в цикле for
for square in squares(a, b):
    print(square, end=" ")