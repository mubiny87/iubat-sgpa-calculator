import streamlit as st

st.set_page_config(page_title="IUBAT SGPA & CGPA Calculator")

st.title("🎓 IUBAT SGPA & CGPA Calculator")

num_courses = st.number_input(
    "How many courses this semester?",
    min_value=1,
    step=1
)

courses = []
total_credits = 0
total_quality_points = 0


def calculate_grade(marks):
    if marks >= 80:
        return "A+", 4.00
    elif marks >= 75:
        return "A", 3.75
    elif marks >= 70:
        return "A-", 3.50
    elif marks >= 65:
        return "B+", 3.25
    elif marks >= 60:
        return "B", 3.00
    elif marks >= 55:
        return "B-", 2.75
    elif marks >= 50:
        return "C+", 2.50
    elif marks >= 45:
        return "C", 2.25
    elif marks >= 40:
        return "D", 2.00
    else:
        return "F", 0.00


for i in range(int(num_courses)):
    st.subheader(f"Course {i+1}")

    course_name = st.text_input(
        f"Course Name {i+1}",
        key=f"name_{i}"
    )

    credit = st.number_input(
        f"Credit {i+1}",
        min_value=1,
        step=1,
        key=f"credit_{i}"
    )

    mid = st.number_input(
        f"Mid Marks {i+1}",
        min_value=0.0,
        max_value=100.0,
        key=f"mid_{i}"
    )

    ct = st.number_input(
        f"CT Marks {i+1}",
        min_value=0.0,
        max_value=100.0,
        key=f"ct_{i}"
    )

    attendance = st.number_input(
        f"Attendance {i+1}",
        min_value=0.0,
        max_value=5.0,
        key=f"att_{i}"
    )

    assignment = st.number_input(
        f"Assignment {i+1}",
        min_value=0.0,
        max_value=10.0,
        key=f"ass_{i}"
    )

    final = st.number_input(
        f"Final Marks {i+1}",
        min_value=0.0,
        max_value=100.0,
        key=f"final_{i}"
    )

    marks = (mid / 4) + (ct / 10) + attendance + assignment + (final / 2)

    grade, gp = calculate_grade(marks)

    quality_points = credit * gp

    total_credits += credit
    total_quality_points += quality_points

    courses.append(
        {
            "Course": course_name,
            "Credit": credit,
            "Marks": round(marks, 2),
            "Grade": grade,
            "GP": gp
        }
    )

if st.button("Calculate SGPA"):

    sgpa = total_quality_points / total_credits

    st.success(f"Semester GPA (SGPA): {sgpa:.2f}")

    st.subheader("Course Summary")
    st.table(courses)

    st.write(f"Total Credits: {total_credits}")
    st.write(f"Total Quality Points: {total_quality_points:.2f}")

    st.subheader("CGPA Calculator")

    previous_cgpa = st.number_input(
        "Previous CGPA",
        min_value=0.0,
        max_value=4.0,
        value=0.0
    )

    previous_credits = st.number_input(
        "Previously Completed Credits",
        min_value=0,
        value=0
    )

    if previous_credits > 0:
        cgpa = (
            (previous_cgpa * previous_credits)
            + total_quality_points
        ) / (previous_credits + total_credits)

        st.success(f"Updated CGPA: {cgpa:.2f}")
