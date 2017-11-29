# Bonus Missions
# These classes are a bit more involved than the ones above. You’ll need to design and implement a 
# working Student class before the Course class can work appropriately. Make sure to use your Student 
# object within the Course object when it is appropriate to do so!

# Student
# A student has a name and student ID number. A student can record grades and will track how many 
# credits they have taken as well as their GPA. A student can also report what their class standing is 
# (Freshman, Sophomore, Junior, Senior, Graduated) based on the number of credits they have taken.

class Student:
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
        self.grade_points = 0
        self.credits = 0
        self.gpa = 0
        self.standing = "Freshman"

    def __repr__(self):
        return "Student ID: " + str(self.student_id)

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def get_grades(self):
        return str(self.grades)

    def get_credits(self):
        return self.credits

    def get_gpa(self):
        return self.gpa

    def get_standing(self):
        return self.standing
    
    def record_grade(self, course, grade):
        self.grades[course.name] = (grade, course.credits)
        self.grade_points += self.calc_grade_points(grade, course.credits)
        self.credits += course.credits
        self.gpa = self.calc_gpa()
        self.standing = self.calc_standing()

    def calc_grade_points(self, grade, credits):
        if grade.lower() == "a":
            return 4.0 * credits
        elif grade == "a-" or grade == "A-":
            return 3.7 * credits
        elif grade == "b+" or grade == "B+":
            return 3.33 * credits
        elif grade.lower() == "b":
            return 3.0 * credits
        elif grade == "b-" or grade == "B-":
            return 2.7 * credits
        elif grade == "c+" or grade == "C+":
            return 2.30 * credits
        elif grade.lower() == "c":
            return 2.0 * credits
        elif grade == "c-" or grade == "C-":
            return 1.70 * credits
        elif grade == "d+" or grade == "D+":
            return 4.0 * credits
        elif grade.lower() == "d":
            return 1.30 * credits
        elif grade == "d-" or grade == "D-":
            return 1.0 * credits
        elif grade.lower() == "f":
            return 0.7 * credits

    def calc_gpa(self):
        return round(self.grade_points / self.credits, 3)

    def calc_standing(self):
        if self.credits < 30:
            return "Freshman"
        elif 30 <= self.credits < 60:
            return "Sophomore"
        elif 60 <= self.credits < 90:
            return "Junior"
        elif 90 <= self.credits < 120:
            return "Senior"
        else:
            return "Graduated"

# Course
# A course has a name and course number. A course has a certain number of seats - once those seats are 
# filled, it is not possible for anyone else to take the course. A course has a roster of students (use your 
# student object!). A course can add a student (if there are open seats) or drop a student. A course can 
# report the average GPA of all students currently enrolled in the course.

class Course:

    def __init__(self, name, course_num, credits, total_seats):
        self.name = name
        self.course_num = course_num
        self.credits = credits
        self.total_seats = total_seats
        self.seats_filled = 0
        self.roster = {}
        self.avg_gpa = 0

    def __repr__(self):
        return self.name + " (" + self.course_num + ")"

    def get_name(self):
        return self.name

    def get_course_num(self):
        return self.course_num

    def get_credits(self):
        return self.credits

    def get_total_seats(self):
        return self.total_seats

    def get_seats_filled(self):
        return self.seats_filled

    def get_roster(self):
        return self.roster

    def get_avg_gpa(self):
        return self.avg_gpa

    def seats_available(self):
        return self.seats_filled < self.total_seats

    def add_student(self, student):
        if self.seats_available():
            self.seats_filled += 1
            self.roster[student.name] = student
        else:
            print("There are no more spots left for this course.")
    
    def drop_student(self, student):
        if student.name in self.roster:
            del self.roster[student.name]
            self.seats_filled -= 1
    
    def calc_avg_gpa(self):
        gpa_total = 0
        for student in self.roster:
            gpa_total += self.roster[student].gpa
        return round(gpa_total / len(self.roster), 3)


def main():
    al = Student("Al", 14570)
    bob = Student("Bob", 14232)
    cat = Student("Cat", 13909)
    history = Course("History", "HIST 101", 3, 30)
    math = Course("Math", "MATH 110", 4, 20)
    science = Course("Science", "SCI 320", 4, 25)
    art = Course("Art", "ART 112", 3, 15)
    al.record_grade(history, "A")
    al.record_grade(math, "B-")
    al.record_grade(science, "C+")
    al.record_grade(art, "A-")
    bob.record_grade(history, "C")
    bob.record_grade(math, "A-")
    bob.record_grade(science, "C-")
    bob.record_grade(art, "c-")
    cat.record_grade(history, "D")
    cat.record_grade(math, "A")
    cat.record_grade(science, "B-")
    cat.record_grade(art, "c+")
    print(al.name + "'s grades include: " +al.get_grades())
    print(al.name + "'s GPA is " + str(al.get_gpa()))
    print(al.name + " has taken " + str(al.get_credits()) + " credits and is therefore a " + al.standing)
    print("The " + history.name + " course contains the following students: " + str(history.get_roster()))
    history.add_student(al)
    history.add_student(cat)
    print("After adding a student,\nthe " + history.name + " course contains the following students:\n" + str(history.get_roster()))
    print(history.seats_filled)
    history.add_student(bob)
    print(history.seats_filled)
    print(bob.get_gpa())
    print(cat.get_gpa())
    print(history.calc_avg_gpa())
    print("After adding a student,\nthe " + history.name + " course contains the following students:\n" + str(history.get_roster()))
    history.drop_student(al)
    print("After dropping a student,\nthe " + history.name + " course contains the following students:\n" + str(history.get_roster()))
    print(history.seats_filled)

if __name__ == "__main__":
    main()