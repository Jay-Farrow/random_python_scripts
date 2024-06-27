# Task: Write a program that determines the average height for a group
# of students from a list. 

print("Enter the heights of the students separated by a space: ")
student_heights = input().split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

number_of_students = len(student_heights)
total = 0

for height in student_heights:
    total += height

average_height = total / number_of_students

print(f"total height = {total}")
print(f"number of students = {number_of_students}")
print(f"average height = {round(average_height)}")