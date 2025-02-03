def myfunction(a):
    b = []
    for i in range(len(a)):
        cnt = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                cnt += 1
        if cnt == 1 and a[i] not in b:
            b.append(a[i])
    return b


a = list(map(int, input().split()))

print(myfunction(a))