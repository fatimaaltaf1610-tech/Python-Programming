wallet = float(input("Enter the amount of money in your wallet: "))
price = float(input("Enter the item price: "))
if wallet >= price:
    print("Purchase successful!")
    print("Remaining money: ", wallet - price)
else:
    print("Not enough money.")