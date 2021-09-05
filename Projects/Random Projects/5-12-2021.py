import random


def gradefinder(grade):
    global studentsA
    global studentsB
    global studentsC
    global studentsD
    global studentsF
    if grade < 50:
        studentsF = studentsF + 1
        return "F"
    if grade < 70:
        studentsD = studentsD + 1
        return "D"
    if grade < 80:
        studentsC = studentsC + 1
        return "C"
    if grade < 90:
        studentsB = studentsB + 1
        return "B"
    studentsA = studentsA + 1
    return "A"


studentsA = 0
studentsB = 0
studentsC = 0
studentsD = 0
studentsF = 0

names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]

for i in range(0, len(names)):
    xScore = random.randrange(10, 90)
    xGrade = gradefinder(xScore)
    print(f"{names[i]} got a score of {xScore}/100 and got a grade of {xGrade}")

print(f"{studentsA} students got an A. {studentsB} students got a B. {studentsC} students got a C. {studentsD} "
      f"students got a D. {studentsF} students got an F.")
