CoursesNames = []
Credits = []
LetterGrades = []
GradePoints = []

TotalCourses = int(input("How many courses this semester? "))
TotalCredits = 0
TotalQualityPoints = 0

for i in range(TotalCourses):
    print(f"\n========== COURSE {i+1} ==========")

    C_Name = input("Course Name: ")
    Credit = int(input("Credit: "))

    MID = float(input("Mid out of 100: "))
    CT = float(input("CT out of 100: "))
    ATT = float(input("Attendance out of 5: "))
    ASS = float(input("Assignment out of 10: "))
    FINAL = float(input("Final out of 100: "))

    CG = (MID / 4) + (CT / 10) + ATT + ASS + (FINAL / 2)

    if CG >= 80:
        LetterGrade = "A+"
        GradePoint = 4.00
    elif CG >= 75:
        LetterGrade = "A"
        GradePoint = 3.75
    elif CG >= 70:
        LetterGrade = "A-"
        GradePoint = 3.50
    elif CG >= 65:
        LetterGrade = "B+"
        GradePoint = 3.25
    elif CG >= 60:
        LetterGrade = "B"
        GradePoint = 3.00
    elif CG >= 55:
        LetterGrade = "B-"
        GradePoint = 2.75
    elif CG >= 50:
        LetterGrade = "C+"
        GradePoint = 2.50
    elif CG >= 45:
        LetterGrade = "C"
        GradePoint = 2.25
    elif CG >= 40:
        LetterGrade = "D"
        GradePoint = 2.00
    else:
        LetterGrade = "F"
        GradePoint = 0.00

    QualityPoints = Credit * GradePoint

    print("\n========== COURSE RESULT ==========")
    print(f"Course Name         : {C_Name}")
    print(f"Course Credit       : {Credit}")
    print(f"Overall Marks       : {CG:.2f}")
    print(f"Letter Grade        : {LetterGrade}")
    print(f"Grade Point         : {GradePoint:.2f}")
    print(f"Quality Points      : {QualityPoints:.2f}")

    TotalCredits += Credit
    TotalQualityPoints += QualityPoints

    CoursesNames.append(C_Name)
    Credits.append(Credit)
    LetterGrades.append(LetterGrade)
    GradePoints.append(GradePoint)

SGPA = TotalQualityPoints / TotalCredits

print("\n========== SEMESTER SUMMARY ==========")
print(f"{'Course Name':15} {'Credit':6} {'Grade':8} {'GP':5}")
print("-" * 40)

for i in range(len(CoursesNames)):
    print(f"{CoursesNames[i]:15} {Credits[i]:6} {LetterGrades[i]:8} {GradePoints[i]:5.2f}")

print("-" * 40)
print(f"Total Credits       : {TotalCredits}")
print(f"Total Quality Points: {TotalQualityPoints:.2f}")
print(f"Semester GPA (SGPA) : {SGPA:.2f}")
