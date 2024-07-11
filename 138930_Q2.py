class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        else:
            return 0

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f'Student {student.name} added.\n')

    def display_students(self):
        if self.students:
            print("List of Students:")
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")
        else:
            print("No students found.\n")

    def get_student_average(self, name):
        for student in self.students:
            if student.name == name:
                average = student.get_average_grade()
                print(f"Average grade for {name}: {average}\n")
                return average
        print(f"Student {name} not found.\n")
        return None

    def get_class_average(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count > 0:
            class_average = total / count
            print(f"Class average for {subject}: {class_average}\n")
            return class_average
        else:
            print(f"No grades found for subject {subject}.\n")
            return None

# Example usage:
if __name__ == "__main__":
    classroom = Classroom()

    # Adding students
    student1 = Student("Alice")
    student1.add_grade("Math", 85)
    student1.add_grade("English", 90)
    classroom.add_student(student1)

    student2 = Student("Bob")
    student2.add_grade("Math", 78)
    student2.add_grade("Science", 88)
    classroom.add_student(student2)

    # Display all students
    classroom.display_students()

    # Get the average grade of a student
    classroom.get_student_average("Alice")
    classroom.get_student_average("Charlie")  # Non-existent student

    # Get the class average for a subject
    classroom.get_class_average("Math")
    classroom.get_class_average("History")  # Subject with no grades
