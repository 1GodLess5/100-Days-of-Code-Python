student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

maxScore = 0

for score in student_scores:
    if score > maxScore:
        maxScore = score

print(f"The highest score in the class is: {maxScore}")


