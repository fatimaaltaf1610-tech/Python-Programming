def calculate_change(paid, price):
    change = paid - price
    return change

ticket_price = 30
print("======PARKING TICKET PAYMENT HELPER======")
print(f"This parking ticket costs {ticket_price} units. ")
print("Accepted coins: 1, 5, 10, and 25\n")

total_insterted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin (1, 5, 10, and 25): "))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin. Please try again\n")
        continue

    total_insterted += coin
    coins_inserted += 1

    print(f"Inserted {coin}. Total inserted {total_insterted}")

    if total_insterted >= ticket_price:
        print("Enough money inserted!\n")
        break

change_due = calculate_change(total_insterted, ticket_price)

print("Printing your parking ticket")

if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units.")

print("=========PAYMENT SUMMARY===========")
print("Ticket price: ", ticket_price)
print("Coins inserted", coins_inserted)
print("Total paid", total_insterted)
print("Change given", change_due)
print("===================================")
print("Parking ticket payment complete")