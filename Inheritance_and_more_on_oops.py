#single_Inheritance

class Employee:
    company = 'Google'

    def showDetails(self):
        print('This is my life')

    
class student(Employee):
    company = 'YouTube'

    def showDetails(self):
        print('I want an another life')

obj = student()
print(obj.company)
obj.showDetails()

#Multiple_Inheritance

class Person():

    def takeBredth(self):
        print('I am breathing...')
        
    def getLife(self):
        print('Love your life')
    

class Employee():

    def takeBredth(self):
        print('I am breathing by the company need...')
 

class Programmer(Employee, Person):

    def getSomething(self):
        print('Everything is happening')

P = Person()
E = Employee()
Pr = Programmer()
Pr.takeBredth()

#Multi_Level_Inheritance

class Person():
    country = 'India'

    def takeBredth(self):
        print('I am breathing...')
        
    def getLife(self):
        print('Love your life')

class Employee(Person):
    company = 'Honda'

    def takeBredth(self):
        print('I am breathing by the company need...')

class Programmer(Employee):

    def getSuccess(self):
        print('I am here to find myself')

P = Person()
E = Employee()
Pr = Programmer()
Pr.takeBredth()








