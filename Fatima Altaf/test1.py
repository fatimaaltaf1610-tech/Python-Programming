import math

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide a number with 0.")
    return a / b

print("\nWelcome to the Calculator!")

while True:

    print("\n----CHOOSE AN ACTION----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("\nEnter your choice: ")

    try:
        if choice in ["1", "2", "3", "4"]:

            num1 = float(input("\nEnter your first number: "))
            num2 = float(input("Enter your second number: "))

            if choice == "1":
                answer = add(num1, num2)

            elif choice == "2":
                answer = subtract(num1, num2)

            elif choice == "3":
                answer = multiply(num1, num2)

            elif choice == "4":
                answer = divide(num1, num2)

            print("Answer is", answer)

        else:
            print("\nInvalid choice. please choose between 1-4.")
            continue

    except ValueError as error:
        print("error:", error)

    except Exception as error:
        print("\nSomething went wrong:", error)