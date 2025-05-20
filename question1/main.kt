fun main(){
    var student1=Student("1209")
    println(student1.gradepoints(arrayOf(1,23), arrayOf("maths","english")))
println(student1.courseSchedule(arrayOf("english","maths")))
println(student1.gpacalculation(arrayOf(1,2,3),arrayOf(2,4,5)))}
class Student(studentId: String) {
    fun gradepoints(gradepoints: Array<Int>, courses: Array<String>): Int {
        for (course in courses) {
            for (gradepoint in gradepoints) {
                if (gradepoint >= 90) {
                    return 4
                } else if (gradepoint in 80..90) {
                    return 3
                } else if (gradepoint in 70..80) {
                    return 2
                } else if (gradepoint in 60..70) {
                    return 1
                } else {
                    return 0
                }
            }
        }

        return 0
    }
    fun courseSchedule(courses: Array<String>) {
        for (course in courses) {
            when (course){
                "English"->println("course will be given at 2:00pm")
            }
        }
    }
    fun gpacalculation(gradepoints: Array<Int>, credithours: Array<Int>): Int{
        var sum=0
        var total=0
        for(gradepoint in gradepoints){
            sum+=gradepoint

        }
        for(credithour in credithours){
            total+=credithour
        }
       var final=total*sum/sum
        return final
    }
}