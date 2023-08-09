# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

def grader(studentScores: dict):
    studentGrades = {}

    for key in studentScores:
        if studentScores[key] >= 91:
            studentGrades[key] = "Outstanding"
        elif 81 <= studentScores[key] <= 90:
            studentGrades[key] = "Exceeds Expectations"
        elif 71 <= studentScores[key] <= 80:
            studentGrades[key] = "Acceptable"
        else:
            studentGrades[key] = "Fail"

    return studentGrades


studentScores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


studentResults = grader(studentScores)
print(studentResults)
