import math

def myfunction(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
        
    return True

mylist = list(map(int,input("Enter: ").split()))

prime_numbers = list(filter(lambda x: myfunction(x), mylist))

print(prime_numbers)
