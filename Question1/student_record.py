grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0}

student_list = [
    {
        "student_id": "S001",
        "courses": [
            {"name": "Backend Development", "credits": 4, "grade": "A"},
            {"name": "DAS", "credits": 4, "grade": "B"}
        ]
    }
]

def student_report(student_id):
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None

def show_schedule(student):
    print('\nCourse Schedule:')
    for c in student["courses"]:
        print(f"{c['name']} - Credits: {c['credits']}")

def add_grade(student, course_name, grade, credits=3):
    for c in student["courses"]:
        if c["name"].lower() == course_name.lower():
            c["grade"] = grade
            print(f"Grade for {course_name} updated to {grade}.")
            return

    student["courses"].append({"name": course_name, "credits": credits, "grade": grade})
    print(f"Course '{course_name}' added with grade {grade} and {credits} credits.")

def calculate_gpa(student):
    total_points = 0
    total_credits = 0
    for c in student["courses"]:
        if c.get("grade") in grade_points:
            total_points += grade_points[c["grade"]] * c["credits"]
            total_credits += c["credits"]
    if total_credits == 0:
        print("No grades yet.")
    else:
        print(f"GPA: {total_points/total_credits:.2f}")

def show_progress(student):
    print('\nStudent Progress:')
    for c in student["courses"]:
        grade = c.get("grade", "Not graded")
        print(f"{c['name']}: {grade}")



student_id = "S001"
student = student_report(student_id)
if not student:
    print("Student not found.")
else:
    show_schedule(student)
    add_grade(student, "New Course", "A", credits=2) 
    add_grade(student, "Backend Development", "B")   
    show_progress(student)
    calculate_gpa(student)
