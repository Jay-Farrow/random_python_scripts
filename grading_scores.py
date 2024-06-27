# Task: Write a program that converts the student's scores to grades. By the 
# end of your program, you should have a new dictionary called student_grades 
# that should contain student names for keys and their grades for values. 

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key, score in student_scores.items():
    if score > 90 and score <= 100:
        student_grades[key] = "Outstanding"
    elif score > 80 and score <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70 and score <= 80:
        student_grades[key] = "Acceptable"
    elif score > 0 and score <= 70:
        student_grades[key] = "Fail"

print(student_grades)