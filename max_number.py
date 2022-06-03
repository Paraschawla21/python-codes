marks = input("\nEnter the marks of students separated by a space: ").split(" ")
for i in range(0, len(marks)):
    marks[i] = int(marks[i])
# print(f"\nMaximum marks is: {max(marks)}")
maximum_marks = 0
for maximum in marks:
    if maximum > maximum_marks:
        maximum_marks = maximum
print("\nMaximum Marks is : " + str(maximum_marks))