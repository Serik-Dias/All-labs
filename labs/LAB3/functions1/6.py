def myfunction(a):
    b = a.split()

    c = b[::-1]

    d = " ".join(c)

    return d


a = input("Enter: ")

print(myfunction(a))