import math

def filter_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True




list1 = list(map(int, input().split()))

list2 = []

for i in list1:
    if filter_prime(i):
        list2.append(i)

print(list2)