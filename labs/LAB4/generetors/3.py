def multiples_of_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i  # Генерирует числа, делящиеся на 3 и 4

# Вводим n
n = int(input("Введите n: "))

# Выводим все найденные числа
for num in multiples_of_3_and_4(n):
    print(num, end=" ")