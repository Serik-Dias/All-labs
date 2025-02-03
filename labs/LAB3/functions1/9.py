import math

def myfunction(a):
    v = (4 * math.pi * a**3)/3
    return v

a = float(input("Enter: "))


print(f"{myfunction(a):.2f}")