const gradePoints = { A: 4.0, B: 3.0, C: 2.0, D: 1.0, F: 0.0 };
let studentRecord = [
  {
    studentId:4545,
    name:"Qefar",
    courses: [
      { name: "Math", instructor: "Dr. Katya", creditscore: 3 },
      { name: "History", instructor: "Mr Joseph", creditscore: 2 }
    ],

    studentId:5656,
    name:"jomo",
    courses:[
        {name:"javascript",instructor:"Dr.Keshy",creditscore:3},
        
    ]

    
  }
  
];

function findStudent(studentId) {
  return studentRecord.find(student => student.studentId === studentId);
}

function viewCourseSchedule(studentId) {
  for (student in studentRecord){
    const student = findStudent(studentId);
  
  if (!student) {
    console.log("Student not found.");
    return;
  }
  console.log(`Schedule for ${student.name}:`);
  student.courses.forEach(course => {
    console.log(`${course.name} - Instructor: ${course.instructor}, Credits: ${course.creditscore}`);
  });
}
}

function enterNewGrade(name, courseName, grade) {
  const student = findStudent(name);
  if (!student) {
    console.log("Student not found.");
    return;
  }
  const course = student.courses.find(c => c.name === courseName);
  if (course) {
    course.grade = grade;
    console.log("Grade updated.");
  } else {
    console.log("Course not found.");
  }
}

function calculateGPA(name) {
  const student = findStudent(name);
  if (!student) {
    console.log("Student not found.");
    return;
  }
  let totalPoints = 0;
  let totalCredits = 0;
  student.courses.forEach(course => {
    if (course.grade) {
      const points = gradePoints[course.grade] || 0;
      totalPoints += points * course.creditscore;
      totalCredits += course.creditscore;
    }
  });
  if (totalCredits === 0) {
    console.log("No grades available.");
  } else {
    console.log("GPA:", (totalPoints / totalCredits).toFixed(2));
  }
}

function showProgress(name) {
  const student = findStudent(name);
  if (!student) {
    console.log("Student not found.");
    return;
  }
  console.log(`Progress for ${student.name}:`);
  student.courses.forEach(course => {
    console.log(`${course.name} - Grade: ${course.grade || "Not graded yet"}`);
  });
}


viewCourseSchedule(5656);
enterNewGrade(5656, "javascript", "A");
calculateGPA(5656);
showProgress(5656);
