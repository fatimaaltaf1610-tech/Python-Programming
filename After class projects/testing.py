import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero.")
    return a / b

print("\nWelcome to the Python Calculator!")

while True:

    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")

    choice = input("Enter your choice: ")

    try:

        if choice == "5":
            number = float(input("Enter a number: "))

            if number < 0:
                raise ValueError("Cannot find the square root of a negative number.")

            answer = math.sqrt(number)
            print("Answer:", answer)

        elif choice in ["1", "2", "3", "4"]:

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                answer = add(num1, num2)

            elif choice == "2":
                answer = subtract(num1, num2)

            elif choice == "3":
                answer = multiply(num1, num2)

            elif choice == "4":
                answer = divide(num1, num2)

            print("Answer:", answer)

        else:
            print("Invalid choice. Please choose 1–5.")
            continue

    except ValueError as error:
        print("Error:", error)

    except Exception as error:
        print("Something went wrong:", error)

    again = input("\nDo you want to calculate something else? (yes/no): ")

    if again.lower() == "no":
        print("\nThank you for using the calculator!\n")
        break