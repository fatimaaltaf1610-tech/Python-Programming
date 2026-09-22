import random 
import math 

lucky_number = random.randint(1,10)
print("Your lucky number is: ", lucky_number)

fun_choices = ["video games", "crocheting", "coding", "baking"]
random_activity = random.choice(fun_choices)
print("Random activity for today: ", random_activity)

print("\nGuess the secret number from 1 to 5!")
secret_number = random.randint(1, 5)

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct! your guessed the secret number!")
        break
    else:
        print("Wrong guess. Try again!")

decimal_number = float(input("Enter a decimal number: "))

print("Ceiling value", math.ceil(decimal_number))
print("Floor value", math.floor(decimal_number))

x = 10
y = -5
print("Copy sign result:", math.copysign(x,y))

negative_number = int(input("Enter a negative number: "))
print("Absolute value:", math.fabs(negative_number))

num1 = int(input("Enter first number for GCD: "))
num2 = int(input("Enter a second number for GCD: "))

print("GCD is:", math.gcd(num1, num2))

print("\n====== FUN CALCULATOR SUMMARY =====")
print("Lucky number:", lucky_number)
print("Random activity:", random_activity)
print("Secret Number:", secret_number)
print("=====================================")