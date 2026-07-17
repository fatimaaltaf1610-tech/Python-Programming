given_number = int(input("Enter the base number: "))
n_power = int(input("Enter how many powers you want to calculte: "))
for i in range(1, n_power + 1):
    x = given_number ** i
    print(f"{given_number} raised to the power of {i} is {x}")