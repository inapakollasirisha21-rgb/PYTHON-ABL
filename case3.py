balance = 1000

while True:
    print("1.Deposit 2.Withdraw 3.Balance 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        balance += int(input("Deposit amount: "))
    elif choice == 2:
        amount = int(input("Withdraw amount: "))
        if amount <= balance and amount > 0:
            balance -= amount
        else:
            print("Invalid amount or insufficient balance")
    elif choice == 3:
        print("Balance:", balance)
    elif choice == 4:
        break
    else:
        print("Invalid choice")