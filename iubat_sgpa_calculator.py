CoursesNames = []
Credits = []
LetterGrades = []
GradePoints = []

TotalCredits = 0
TotalQualityPoints = 0


def input_info():
    print("\n========== COURSE ==========")

    C_Name = input("Course Name: ")
    Credit = int(input("Credit: "))

    MID = float(input("Mid out of 100: "))
    CT = float(input("CT out of 100: "))
    ATT = float(input("Attendance out of 5: "))
    ASS = float(input("Assignment out of 10: "))
    FINAL = float(input("Final out of 100: "))

    return C_Name, Credit, MID, CT, ATT, ASS, FINAL


def calculate_marks(MID, CT, ATT, ASS, FINAL):
    CG = (MID / 4) + (CT / 10) + ATT + ASS + (FINAL / 2)
    return CG


def calculate_grade(CG):
    if CG >= 80:
        return "A+", 4.00
    elif CG >= 75:
        return "A", 3.75
    elif CG >= 70:
        return "A-", 3.50
    elif CG >= 65:
        return "B+", 3.25
    elif CG >= 60:
        return "B", 3.00
    elif CG >= 55:
        return "B-", 2.75
    elif CG >= 50:
        return "C+", 2.50
    elif CG >= 45:
        return "C", 2.25
    elif CG >= 40:
        return "D", 2.00
    else:
        return "F", 0.00


def calculate_quality_points(Credit, GradePoint):
    return Credit * GradePoint


def print_result(C_Name, Credit, CG, LetterGrade, GradePoint, QualityPoints):
    print("\n========== COURSE RESULT ==========")
    print(f"Course Name         : {C_Name}")
    print(f"Course Credit       : {Credit}")
    print(f"Overall Marks       : {CG:.2f}")
    print(f"Letter Grade        : {LetterGrade}")
    print(f"Grade Point         : {GradePoint:.2f}")
    print(f"Quality Points      : {QualityPoints:.2f}")


def print_summary(CoursesNames, Credits, LetterGrades, GradePoints,
                  TotalCredits, TotalQualityPoints):
    SGPA = TotalQualityPoints / TotalCredits

    print("\n========== SEMESTER SUMMARY ==========")
    print(f"{'Course Name':15} {'Credit':6} {'Grade':8} {'GP':5}")
    print("-" * 40)

    for i in range(len(CoursesNames)):
        print(
            f"{CoursesNames[i]:15} {Credits[i]:6} "
            f"{LetterGrades[i]:8} {GradePoints[i]:5.2f}"
        )

    print("-" * 40)
    print(f"Total Credits       : {TotalCredits}")
    print(f"Total Quality Points: {TotalQualityPoints:.2f}")
    print(f"Semester GPA (SGPA) : {SGPA:.2f}")


# ================= MAIN PROGRAM =================

print("========== IUBAT SGPA & CGPA CALCULATOR ==========")

TotalCourses = int(input("How many courses this semester? "))

if TotalCourses <= 0:
    print("Number of courses must be greater than 0.")
    exit()
    
for i in range(TotalCourses):

    print(f"\n========== COURSE {i+1} ==========")

    C_Name, Credit, MID, CT, ATT, ASS, FINAL = input_info()

    CG = calculate_marks(MID, CT, ATT, ASS, FINAL)

    LetterGrade, GradePoint = calculate_grade(CG)

    QualityPoints = calculate_quality_points(Credit, GradePoint)

    print_result(
        C_Name,
        Credit,
        CG,
        LetterGrade,
        GradePoint,
        QualityPoints
    )

    TotalCredits += Credit
    TotalQualityPoints += QualityPoints

    CoursesNames.append(C_Name)
    Credits.append(Credit)
    LetterGrades.append(LetterGrade)
    GradePoints.append(GradePoint)

print_summary(
    CoursesNames,
    Credits,
    LetterGrades,
    GradePoints,
    TotalCredits,
    TotalQualityPoints
)

# ================= CGPA CALCULATOR =================

choice = input("\nDo you want to calculate CGPA? (Y/N): ").strip().upper()

if choice == "Y":

    PreviousCGPA = float(input("Enter Previous CGPA: "))
    PreviousCredits = int(input("Enter Previously Completed Credits: "))

    SGPA = TotalQualityPoints / TotalCredits

    CGPA = (
        (PreviousCGPA * PreviousCredits)
        + TotalQualityPoints
    ) / (PreviousCredits + TotalCredits)

    print("\n========== CGPA RESULT ==========")
    print(f"Previous CGPA         : {PreviousCGPA:.2f}")
    print(f"Previous Credits      : {PreviousCredits}")
    print(f"Current Semester SGPA : {SGPA:.2f}")
    print(f"Current Credits       : {TotalCredits}")
    print(f"Updated CGPA          : {CGPA:.2f}")

print("\nThank you for using IUBAT SGPA & CGPA Calculator!")
