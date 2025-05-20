grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
student_list = [ ]

def find_student(name):
    for student in student_list:
        if student["name"] == name:
            return student
    return None

def view_course_schedule():
    name = input("Enter student name: ")
    student = find_student(name)
    if student:
        print(f"Schedule for {student['name']}:")
        for course in student["courses"]:
            print(f"{course['name']} - Instructor: {course['instructor']} | Credits: {course['credits']}")
    else:
        print("Student not found.")

def enter_new_grade():
    name = input("Enter student name: ")
    student = find_student(name)
    if not student:
        print("Student not found.")
        return
    course_name = input("Enter course name: ")
    grade = input("Enter grade (A-F): ").upper()
    for course in student["courses"]:
        if course["name"] == course_name:
            course["grade"] = grade
            print("Grade updated.")
            return
    print("Course not found.")

def calculate_gpa():
    name = input("Enter student name: ")
    student = find_student(name)
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

def show_progress():
    name = input("Enter student name: ")
    student = find_student(name)
    if not student:
        print("Student not found.")
        return
    print(f"Progress for {student['name']}:")
    for course in student["courses"]:
        grade = course.get("grade", "Not graded yet")
        print(f"{course['name']} - Grade: {grade}")


student_list.append({
    "name": "Alice",
    "courses": [
        {"name": "Math", "instructor": "Dr. Smith", "credits": 3},
        {"name": "History", "instructor": "Ms. Lee", "credits": 2}
    ]
})


