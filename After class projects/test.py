import random

secret = random.randint(1, 50)
attempts = 0
lives = 5

print("Welcome to the guessing game. Guess the random number between 1 and 50. You have 5 Lives.")

while attempts < 5:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print("Congrats! You guessed the number!")
        break

    else:
        difference = abs(secret - guess)

        if difference > 20:
            print("🧊 ice cold")
        elif difference > 10:
            print("🥶 cold")
        elif difference > 5:
            print("🌡️ warm")
        else:
            print("🔥 hot")

        lives -= 1

        if lives > 0:
            print("Remaining lives: ", end="")
            for i in range(lives):
                print("❤️", end="")
            print("\n")

if attempts == 5 and guess != secret:
    print("You lost.")
    print("The secret number was ", secret)