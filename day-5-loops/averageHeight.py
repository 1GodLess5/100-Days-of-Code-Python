student_heights = input("Input a list of student heights ").split()

for i in range(0, len(student_heights)):
  student_heights[i] = int(student_heights[i])

heightSum = 0
studentNumber = 0

for student in student_heights:
    heightSum += student
    studentNumber += 1

print(round(heightSum/studentNumber))
