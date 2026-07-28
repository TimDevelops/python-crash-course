# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price


total_price = 0.00
drink_count = 0

while True:
    customers_name = input("What is your name? ").lower()

    if customers_name == 'done':
        break

    drink_order = input("What would you like to drink? ").lower()
    drink_count += 1

    if drink_order == 'latte':
        total_price += 3.50
    elif drink_order == 'americano':
        total_price += 3.00
    elif drink_order == 'espresso':
        total_price += 2.50
    else:
        print(f"Sorry we don't make {drink_order}'s here.")
        drink_count -= 1
        continue

    print(f"total price: {total_price:.2f} & drink count: {drink_count}")

print(f"Total number of drinks made: {drink_count}\nTotal price: {total_price:.2f}")