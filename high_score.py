# Task: write a program that calculates the highest score from a list of scores.
# We can do this by using for loops.

print("Enter a list of scores separated by a space: ")
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])    # Converts the list of scores from str to int. 

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
    
print(f"The highest score in the class is: {highest_score}")