held = int(input("Classes held: "))
attended = int(input("Classes attended: "))

percentage = attended / held * 100
print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")