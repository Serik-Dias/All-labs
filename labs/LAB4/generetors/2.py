def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i  # Генерирует только чётные числа

# Вводим n
n = int(input("Введите n: "))

# Выводим числа через запятую
print(", ".join(map(str, even_numbers(n))))