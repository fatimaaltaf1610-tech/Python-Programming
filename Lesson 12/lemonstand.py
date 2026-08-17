def greet_customer():
    print("Welcome to the Lemonade stand!")
    print("Fresh Lemonade made just for you.")

greet_customer()

price_per_cup = float(input("Enter the price per cup in dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))

def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Total cost: ", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(cups):
    if cups >= 5:
        return "Wow, big order! Thank you for your support!"
    else:
        return "Thank your for stopping by the stand!"

closing_message = thank_you_message(cups_sold)

print(" ")
print("==== LEMONADE STAND RECIPT ====")
print("Price per cup: ", price_per_cup)
print("Cups sold: ", cups_sold)
print("Total cost: ", rounded_total)
print("Amount paid: ", amount_paid)
print("Change due: ", rounded_change)
print(closing_message)
print("===============================")