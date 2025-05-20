grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0}
student_list = [ ]

def student_report(student_id):
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None

def course_schedule():
    student_id = input("Enter student_id: ")
    student = student_report(student_id)
    if student:
        print(f"Schedule for {student['student_id']}:")
        for course in student["courses"]:
            print(f"{course['name']} - Instructor: {course['instructor']} | Credits: {course['credits']}")
    else:
        print("Student not found.")

def new_grade():
    student_id = input("Enter student_id: ")
    student = student_report(student_id)
    # if not student:
    #     print("Student not found.")
    #     return
    course_name = input("Enter course name: ")
    grade = input("Enter grade point: ").upper()
    for course in student["courses"]:
        if course["name"] == course_name:
            course["grade"] = grade
            print("Grade updated.")
            return
    else:
        course["grade"]=grade
        print("Grade added")
        return 
    # print("Course not found.")

def calculate_gpa(student_id):
    # name = input("Enter student_id: ")
    student = student_report(student_id)
    if not student:
        print("Student not found.")
        return
    total_points = 0
    total_credits = 0
    for course in student["courses"]:
        if "grade" in course:
            points = grade_points.get(course["grade"], 0)
            total_points += points * course["credits"]
            total_credits += course["credits"]
    if total_credits == 0:
        print("No grades available.")
    else:
        gpa = total_points / total_credits
        print(f"GPA: {gpa:.2f}")

def student_progress():
    name = input("Enter student_id: ")
    student = student_report(student_id)
    if not student:
        print("Student not found.")
        return
    print(f"Progress for {student['name']}:")
    for course in student["courses"]:
        grade = course.get("grade", "Not graded yet")
        print(f"{course['name']} - Grade: {grade}")

student_list.append({
    "student_id": "S001",
    "courses": [
        {"name": "Backend Development", "instructor": "Mr. Mowai", "credits": 4},
        {"name": "DAS", "instructor": "Ms. Sharon", "credits": 4}
    ]
})
