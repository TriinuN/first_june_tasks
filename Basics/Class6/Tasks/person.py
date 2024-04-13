# Create a class called "Person" with attributes for name and age.
# Add a method to the Person class that prints a greeting message with the person's name.
# Create a subclass of Person called "Student" with an additional attribute for student ID.
# Override the Person class's method in the Student subclass to include the student ID in the greeting message.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_ID):
        super().__init__(name, age)
        self.student_ID = str(student_ID)
        print(f"Hello {self.name}")
        print(f"Hello {self.name}, your student ID is {self.student_ID}")


# Greating a person
person1 = Person("John",17)
# Graating a student
student1 = Student("John", 17, 5673892)
