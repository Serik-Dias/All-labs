import math
numbers = list(map(int, input("Введите числа через пробел: ").split()))
result = math.prod(numbers) #prod=product

print(f"Произведение чисел: {result}")