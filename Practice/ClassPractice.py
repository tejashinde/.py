class Person:
    'Base class for all the Persons'

    def __init__ (self,name,age):
        self.name = name
        self.age = age
        self.subjects =  {}
        pass

    def displayDetails(self):
        print ("The student name is : %s \nStudent age is : %s" % (self.name,self.age))

class Student(Person):
    'Deriver from person class'
    def __init__ (self,name,age,division,marks):
        super().__init__(name,age)
        self.division = division
        self.marks = marks

    def addSubject(self,subjectName,marks):
        self.subjects[subjectName] = marks

    def printSubjects(self):
        print(self.subjects)

        #Method Overriding
    def displayDetails(self):
        print ("The name is : %s\nAge is : %d\nDivision is : %c\nMarks are : %d" % (self.name,self.age,self.division,self.marks))

student = Student("C",55,"A",98)
student.displayDetails()
student.addSubject("History",98)
student.printSubjects()
