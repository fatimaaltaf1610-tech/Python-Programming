try:
    number = int(input("Enter your Age: "))
    print("The number entered is: ", number)
except ValueError as ex:
    print("Exception:", ex)