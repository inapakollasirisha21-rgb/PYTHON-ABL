products = [("Pen", 10, 20), ("Book", 50, 10),
            ("Bag", 500, 5)]

for name, price, stock in products:
    print(name, "Price:", price, "Stock:", stock)
    print("Inventory value:", price * stock)