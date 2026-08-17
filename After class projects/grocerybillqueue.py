print("=== Grocery Billing Queue ===\n")

low_priced_items = 0
medium_priced_items = 0
high_priced_items = 0

customers_served = 0
total_sales = 0

billing = True

while billing:
    name = input("Enter customers name: ")
    item_count = int(input(f"Hella {name}! How many items are you buying? "))

    if item_count <= 0:
        print("Invalid item count. Please enter a positive number.\n")
        continue

    print(f"\nBilling items for {name}:")
    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        item_name = input("Enter item name: ")
        price = int(input("Enter item price: "))
        quantity = int(input("Enter the quantity: "))

        if price <= 0 or quantity <= 0:
            print("Invalid price or Quantity. Please enter again.\n")
            continue

        item_total = price * quantity
        print(f" {item_name}: {quantity} x {price} = {item_total}")

        customer_total += item_total

        if price < 50:
            low_priced_items += quantity
        elif price <= 100:
            medium_priced_items += quantity
        else:
            high_priced_items += quantity

        item_number += 1

    customers_served += 1
    total_sales += customer_total

    print(f"\nTotal bill for {name}: {customer_total}")
    print("Billing complete!\n")

    again = input("Next customer? (yes/no): ").strip().lower()

    if again != "yes":
        billing = False


print("\n=== Grocery Category Report ===")

for slot in range(1, 4):

    if slot ==1:
        label, total = "low priced items", low_priced_items
    elif slot ==2:
        label, total = "medium priced items", medium_priced_items
    else:
        label, total = "High priced items", high_priced_items

    if total > 0:
        print(f" {label}: {total} ", end="")

        for item in range(total):
            print("*", end="")

        print()

print(f"\nCustomers served: {customers_served}")
print(f"Total sales: {total_sales}")
print("Grocery billing closed. Goodbye!")