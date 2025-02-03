def myfunction(a):
    a = a.replace(" ", "").lower()

    for i in range(len(a) // 2):
        if a[i] != a[len(a) - i - 1]:
            return False
    return True 


a = input("Enter: ")

if(myfunction(a)):
    print(f"{a} is palindrome")
else:
    print(f"{a} is not polindrome")