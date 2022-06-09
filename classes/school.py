from ast import For
from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self,student_data):
        #need to 
        self.students.append(Student(**student_data))
        
    def delete_student(self, school_id):
        # for student in self.students:
        #     if student.school_id == school_id:
        #         del student
        for i in range(len(self.students)):
            student = self.students[i]
            if school_id == student.school_id:
                self.students.pop(i)
                break
        