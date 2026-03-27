from abc import ABC, abstractmethod

# 🔹 Abstraction
class Person(ABC):
    
    def __init__(self, name):
        self.name = name   # Encapsulation (public)

    @abstractmethod
    def role(self):
        pass


# 🔹 Inheritance
class Student(Person):
    
    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks   # Encapsulation (private)

    # 🔹 Method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

    # 🔹 Polymorphism
    def role(self):
        print("I am a Student")


class Teacher(Person):
    
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def role(self):
        print("I am a Teacher")


# 🔹 Objects
s1 = Student("Hanny", 90)
t1 = Teacher("Rahul Sir", "Math")

# Method call
s1.display()

# 🔹 Polymorphism (same method, different output)
for person in (s1, t1):
    person.role()