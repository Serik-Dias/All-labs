def square_generator(n):
    for i in range(n+1):
        yield i ** 2
n=int(input("put the number:"))
for square in square_generator(n):
    print(square,end=" ")
