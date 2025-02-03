def myfunction(numheads,numlegs):
    rabbits = (numlegs - 2 * numheads) // 2

    chickens = numheads - rabbits

    return rabbits,chickens


a = int(input("Number heads: "))
b = int(input("Number legs: "))

rabbits,chickens = myfunction(a,b)

print("Number of Chickens:" , chickens , ", Number of Rabbits:", rabbits)


    