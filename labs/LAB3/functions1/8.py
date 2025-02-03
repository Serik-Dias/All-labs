def myfunction(a):
    c = [0, 0, 7]
    b = 0

    for i in a:  
        if i == c[b]:
            b += 1
            if b == len(c):
                return True
    
    return False



a = list(map(int,input("Enter: ").split()))

print(myfunction(a))