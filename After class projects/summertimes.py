choice = input("Do you want to enter the temperature in (C)elcius or (F)ahrenheit?\nPlease choose 'C' for celcius or 'F' for fahrenheit: ").upper()
if choice == "C":
    celsius = float(input("Enter temperature in Celsius: "))
    if celsius > 20:
        print("You can wear light and soft clothes!")
    else:
        print("You'll have to wear a jacket and pullover.")
elif choice == "F":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    if fahrenheit > 60:
        print("You can wear light and soft clothes!")
    else:
        print("You'll have to wear a jacket and pullover.")
else:
    print("Invalid choice. Please enter C or F to decided the suitable clothing options.")