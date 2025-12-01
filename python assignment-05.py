# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Derived class Student from Person
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)      # Calling base class constructor
        self.course = course

    def display_student(self):
        print("Course:", self.course)


# Derived class Exam from Student
class Exam(Student):
    def __init__(self, name, age, course, m1, m2, m3):
        super().__init__(name, age, course)   # Call Student constructor
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.total = 0

    def compute_total(self):
        self.total = self.m1 + self.m2 + self.m3

    def display_exam(self):
        print("Marks:")
        print(" Subject 1:", self.m1)
        print(" Subject 2:", self.m2)
        print(" Subject 3:", self.m3)
        print("Total Marks:", self.total)


# ---------------------------
# Creating object of Exam class
# ---------------------------

e1 = Exam("Happy Sharma", 20, "BCA (AI & DS)", 85, 90, 88)

# Compute total marks
e1.compute_total()

# Display all information
print("\n--- Student Details ---")
e1.display_person()
e1.display_student()
e1.display_exam()