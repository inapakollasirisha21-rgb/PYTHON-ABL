marks = [[80, 75, 90], [60, 85, 70], [95, 90, 88]]

for i in range(len(marks)):
    total = sum(marks[i])
    average = total / len(marks[i])
    print("Student", i + 1)
    print("Total:", total)
    print("Average:", average)