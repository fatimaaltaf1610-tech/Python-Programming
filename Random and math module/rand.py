import random
playing = True
number = str(random.randint(0,9))

print("I will generate a number between  0 and 9, and you have to guess the number one digit at a time.")
print("The game ends when you guess the random number!")

while playing:
    guess = input("give me your best guess! \n ")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess isn't right. Try again. \n")