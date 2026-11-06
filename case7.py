email = input("Enter email: ")

if "@" in email and "." in email:
    print("Email format looks valid")
else:
    print("Invalid email format")