print("Select your choice:")
print("1. Bike")
print("2. Car")
choice = int(input("Enter your choice: "))
if (choice == 1):
    print("What type of bike?")
    print("1. Scooty\n")
    print("2. Scooter\n")
    choice2 = int(input("Enter your choice2: "))
    if choice2 == 1:
        print("you have selected scooty")
    else:
        print("You have selecter scooter")
elif (choice == 2):
    print("What type of car?")
    print("1. Sedan")
    print("2. SUV")
    choice3 = int(input("Enter your choice3: "))
    if choice3 == 1:
        print("You have selected Sedan")
    else:
        print("You have selected SUV")
else:
    print("Invalid option")