
a) Base Class: Person
The Person class is the first (top-level) class.
It contains basic attributes:
name
age
It also contains a method to display the name and age.
Example behavior:
If a Person object has name = "Amit" and age = 20,
the display method will show:
Name: Amit, Age: 20
b) Derived Class: Student (inherits Person)
The Student class extends (inherits from) the Person class.
Along with name and age, it adds a new attribute:
course (like BCA, B.Tech, etc.)
This class can also display the student’s course along with inherited details.
Meaning:
A Student is also a Person, so it automatically has:
name
age
And additionally has:
course
c) Derived Class: Exam (inherits Student)
The Exam class extends Student.
It includes:
marks of 3 subjects (for example: m1, m2, m3)
It has a method to compute:
total marks = m1 + m2 + m3
It also displays marks and the total.
Meaning:
An Exam object has:
Person details → name, age
Student details → course
Exam details → three subject marks + total
d) Creating an Exam Object & Displaying Details
When an object of Exam class is created, it will contain all data:
Name
Age
Course
Marks of subject1, subject2, subject3
Total marks
Calling the display method should show the complete result:
Example Output (conceptual):


Name: Rahul Kumar
Age: 19
Course: BCA
Marks:
  Subject 1: 85
  Subject 2: 90
  Subject 3: 88
Total Marks: 263
