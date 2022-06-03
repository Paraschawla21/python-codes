students_height = input("\nEnter the height of students: ").split(",")
print(f"\nHeight of students are: {students_height}")
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
total_height = 0
for height in students_height:
    total_height += height
print(f"\nTotal height of students is: {total_height}")
no_of_students = 0
for students in students_height:
    no_of_students += 1
print(f"\nTotal no of students are: {no_of_students}")
print(f"\nSo, Average height of students is: {float(total_height / no_of_students)}")