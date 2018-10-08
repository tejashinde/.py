# Name : Tejas Shinde
#Symbiosis Institute of Computer Studies and Research
#28th Aug 2018
class Person:
    'Base class'

    def __init__(self,firstName,middleName,lastName):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.subjects = ['0','1']
        self.teacherDetails = {}

        # pass
    def displayName():
        print("Full name : %s . %s . %s" % (firstName,middleName,lastName))

class Student(Person):




    'Child class'

    def __init__(self,firstName,middleName,lastName,subject,marks):
        super().__init__(firstName,middleName,lastName)
        self.subject = subject;
        self.marks = marks;

    def addSubject(self,subject,marks):
        for i in range(2,(len(self.subjects) + 1)):
            self.subjects[i] = subject
            self.subjects[i+1] = marks

    def printDetails(self):
        print("\n\tName : " + self.firstName + " " + self.middleName + " " + self.lastName +"\n\t\t")
        print("\t\tSubject : " + self.subject + "\n\t\t")
        print("\t\tMarks : " + str(self.marks) + " ")


class Teacher(Person):
    'Child class'

    def __init__(self,designation,firstName,middleName,lastName,phone):
        super().__init__(firstName,middleName,lastName)
        self.designation = designation
        self.phone = phone

    def addTeacherDetails(self,designation,phone):
        self.designation = designation
        self.phone = phone

    def printDetails(self):
        print("\n\tName : " + self.designation + ". "+ self.firstName + " " + self.middleName + " " + self.lastName +"\n\t\t")
        print("\t\tPhone : " + str(self.phone) + " ")


#Student Objects
s1 =Student('Tejas','Ashok','Shinde','History',99)
s2 =Student('Azhar','Anwar','Sheikh','Math',120)
s3 =Student('Marclus','Tejas','Lopes','English',33)
s4 =Student('Johncy','Elair','Fernandes','Python',63)
s5 =Student('Bill','Surrinder','Gates','Windows',88)
s6 =Student('Nath','Josh','Philips','Geography',25)
s7 =Student('Stanley','Twig','Lucifer','Linux',51)
s8 =Student('Priyanka','Sunil','Chopra','Social studies',46)
s9 =Student('Arjun','Sikender','Kapoor','Math',91)
s10 =Student('Tejal','Jasvinder','Dayal','Math',76)

#Teacher Objects
t1 = Teacher('Mrs','Aruna','Ashok','Shinde',9635845632)
t2 = Teacher('Mr','Ashok','Bhojraj','Shinde',8546232574)

#Student Print

print("Students :")
s1.printDetails()
s2.printDetails()
s3.printDetails()
s4.printDetails()
s5.printDetails()
s6.printDetails()
s7.printDetails()
s8.printDetails()
s9.printDetails()
s10.printDetails()

print("Teachers :")
#Teacher Print
t1.printDetails()
t2.printDetails()
