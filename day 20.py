#day 20
'''

print("===== Captial university=====")


class person:
    def __init__(self, name, age, blood_group, gender):
        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Blood Group: {self.blood_group}")
        print(f"Gender: {self.gender}")


class student(person):

    student_count = 0

    def __init__(self, name, age, blood_group, gender, roll_no, department):
        super().__init__(name, age, blood_group, gender)
        self.roll_no = roll_no
        self.department = department
        student.student_count += 1

    def display_students(self):
        self.display()
        print(f"Roll No: {self.roll_no}")
        print(f"Department: {self.department}")
        print()


class faculty(person):

    def __init__(self, name, age, blood_group, gender, emp_id, department):
        super().__init__(name, age, blood_group, gender)
        self.emp_id = emp_id
        self.department = department

    def display_faculty(self):
        self.display()
        print(f"Emp ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print()



stu1 = student('prem', 22, 'AB+', 'M', 101, 'CSE')
stu2 = student('bhushan', 22, 'O+', 'M', 102, 'CSD')

fac1 = faculty('ravi', 34, 'AB+', 'M', 1102, 'CSE')
fac2 = faculty('Sai', 30, 'A+', 'M', 1104, 'CSM')


print("\n----- STUDENT DETAILS -----")
stu1.display_students()
stu2.display_students()


print("----- FACULTY DETAILS -----")
fac1.display_faculty()
fac2.display_faculty()


print("Total Students:", student.student_count)


'''
class University:
    university_name = "CODEGNAN UNIVERSITY"

    def display_university(self):
        print(f"University Name : {University.university_name}")


class Person(University):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person(self):
        self.display_university()
        print(f"Name            : {self.name}")
        print(f"Age             : {self.age}")
        print(f"Gender          : {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, department):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print("\n----- STUDENT DETAILS -----")
        self.display_person()
        print(f"Student ID      : {self.student_id}")
        print(f"Department      : {self.department}")


class Faculty(Person):
    def __init__(self, name, age, gender, faculty_id, subject):
        super().__init__(name, age, gender)
        self.faculty_id = faculty_id
        self.subject = subject

    def display_info(self):
        print("\n----- FACULTY DETAILS -----")
        self.display_person()
        print(f"Faculty ID      : {self.faculty_id}")
        print(f"Subject         : {self.subject}")


class LabAssistant(Person):
    def __init__(self, name, age, gender, employee_id, lab_name):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.lab_name = lab_name

    def display_info(self):
        print("\n----- LAB ASSISTANT DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")
        print(f"Lab Name        : {self.lab_name}")


class Librarian(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(name, age, gender)
        self.employee_id = employee_id

    def display_info(self):
        print("\n----- LIBRARIAN DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")


class Watchman(Person):
    def __init__(self, name, age, gender, employee_id, shift):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.shift = shift

    def display_info(self):
        print("\n----- WATCHMAN DETAILS -----")
        self.display_person()
        print(f"Employee ID     : {self.employee_id}")
        print(f"Shift           : {self.shift}")


# Objects
s1 = Student("Bhushan", 22, "Male", "S101", "CSE")
f1 = Faculty("prem", 40, "Male", "F101", "Python")
l1 = LabAssistant("anil", 30, "Male", "L101", "Python Lab")
lb1 = Librarian("sai", 35, "Female", "LB101")
w1 = Watchman("Ravi", 45, "Male", "W101", "Night")

# Display
s1.display_info()
f1.display_info()
l1.display_info()
lb1.display_info()
w1.display_info()




















