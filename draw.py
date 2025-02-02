import random

name = input("Hello what is your name?: ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

num = random.randint(1, 20)
sum_of_guesses = 0

while True:
    guess = int(input("Take a guess: "))
    sum_of_guesses += 1

    if guess < num:
        print("Your guess is too low.")
    elif guess > num:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in {sum_of_guesses} guesses!")
        break
