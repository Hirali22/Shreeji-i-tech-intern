# Number guessing game.using for
import random
no = random.randint(1, 100)
guess = int(input("Enter your guess: "))

for i in range(1, 10):
    if guess == no:
        print("You guessed it right in", i, "attempts")
        break
    elif guess < no:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    guess = int(input("Enter your guess: "))
else:
    print("You guessed it wrong in 10 attempts")
