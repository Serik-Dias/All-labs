import itertools

def permutation(a):
    
    permutation = itertools.permutations(a)


    for i in permutation:
        print(''.join(i))


a = input("Enter: ")

permutation(a)