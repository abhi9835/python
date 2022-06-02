
"""super method"""

class Person():
    country = 'India'

    def __init__(self):
        print("Initialising Person..\n")

    def takeBredth(self):
        print('I am breathing...')
        
    def getLife(self):
        print('Love your life')

class Employee(Person):
    company = 'Honda'

    def __init__(self):
        super().__init__()
        print("Initialising Employee...\n")

    def takeBredth(self):
        print('I am breathing by the company need...')

class Programmer(Employee):

    def __init__(self):
        super().__init__()
        print("Initialising Programmer...\n")

    def getSuccess(self):
        print('I am here to find myself')

P = Person()
E = Employee()
Pr = Programmer()
Pr.takeBredth()
print(E.country)


"""class method"""

class Employee():

    company = 'Morgan Stanley'
    salary = 100000
    place = 'New York'

    def updateSalary(self):
        self.salary = 500000
    
    @classmethod
    def changesalary(cls, sal):
        cls.salary = sal



e = Employee()
e.updateSalary()
e.changesalary(700000)
print(e.salary)
print(Employee.salary)








