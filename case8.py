prepared = int(input("Meals prepared: "))
served = int(input("Meals served: "))

leftover = prepared - served
percentage = leftover / prepared * 100

print("Leftover meals:", leftover)
print("Wastage percentage:", percentage, "%")