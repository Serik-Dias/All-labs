import random

name = input("Hello what is your name?: ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

num = random.randint(1, 20)

while True:
    guess = int(input("Take a guess: "))

    if guess < num:
        print("Your guess is too low.")
    elif guess > num:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in 3 guesses!")
        break
