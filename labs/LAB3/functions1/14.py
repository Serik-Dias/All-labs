import random 

random_number = random.randint(1, 20)

c = 0

print("Hello! What is your name?")
a = input("Name: ")

print(f"Well, {a}, I am thinking of a number between 1 and 20.\nTake a guess.")
b = int(input("Enter: "))
while(True):
    c += 1

    if b < random_number:
        print("Your guess is too low.\nTake a guess.")
    elif b > random_number:
        print("Your guess is too high.\nTake a guess.")
    else:
        print(f"Good job, {a}! You guessed my number in {c} guesses!")
        break 

  
    b = int(input("Enter: "))