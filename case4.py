prices = [100, 200, 150]
total = 0

for price in prices:
    quantity = int(input("Enter quantity: "))
    total += price * quantity

print("Total bill:", total)