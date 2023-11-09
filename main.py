class Student:
    def __init__(self, name, age, gender, level, grade = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grade = grade or {}
        
    def setGrade(self, course, grade):
        self.grade[course] = grade

    def getGrade(self, course):
        return self.grade[course]

    def getGPA(self):
        return sum(self.grade.values()) / len(self.grade)

student1 = Student("John", 12, "Male", 6, {"Math": 3.3})
student2 = Student("Mary", 12, "Female", 7, {"Physics": 3.3})