"""create a class programmer for storing information of few programmers working at microsoft?"""

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, profile):
        self.name = name
        self.salary = salary
        self.profile = profile

    def getInfo(self):
        print(f"The name of the employee is {self.name} and the salary of the employee is {self.salary} and its profile is {self.profile}")


employee_1 = Programmer("Abhishek", 100000, 'senior Engineer')
employee_2 = Programmer('Aniket', 500000, "Software Enginner")
employee_3 = Programmer("rajnish", 500000, 'Software Engineer')

employee_1.getInfo()
employee_2.getInfo()
employee_3.getInfo()

"""write a class calculator capable of finding square, cube and square root of a number?"""

class Calculator:

    def __init__(self, number):
        self.number = number

    def squareOfNumber(self):
        print(f"The square of a {self.number} is {self.number**2}")

    def cubeOfNumber(self):
        print(f"The cube of a {self.number} is {self.number**3}")
    
    def squareRootOfNumber(self):
        print(f"The square root of a {self.number} is {self.number**0.5}")

a = Calculator(5)
a.squareOfNumber()
a.cubeOfNumber()
a.squareRootOfNumber()

"""Create a class with a class attribute a; create an object from it and set a directly using object a = 0. Does this change the class variable?"""

class Function():
    a = "abhishek"


obj = Function()
obj.a = "Aniket"
# Function.a = "rajnish" #It will change the class attribute.
print(Function.a)
print(obj.a)

"""Add a static method in problem 2 to greet the user with hello"""

class Calculator:

    def __init__(self, number):
        self.number = number

    def squareOfNumber(self):
        print(f"The square of a {self.number} is {self.number**2}")

    def cubeOfNumber(self):
        print(f"The cube of a {self.number} is {self.number**3}")
    
    def squareRootOfNumber(self):
        print(f"The square root of a {self.number} is {self.number**0.5}")

    @staticmethod
    def greet():
        print('Hello everyone!!')

a = Calculator(5)
a.greet()
a.squareOfNumber()
a.cubeOfNumber()
a.squareRootOfNumber()

"""write a class train which has methods to book a ticket, get status(no of seats) and get fare information of trains running under Indian Railways"""

class Train:
    def __init__(self, name, fare, seats):
        self.name = name 
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print("********************")
        print(f"The name of the train is {self.name}")
        print("********************")
    
    def getSeatStatus(self):
        print('*********************')
        print(f"The seats in the train are {self.seats}")
        print('**********************')
        

    def fareInfo(self):
        print(f"The fare of the train is {self.fare}")

    def bookTicket(self):
        if self.seats>0:
            print(f"Your ticket has been booked!! and your ticket number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("The seats in the train is filled. You can try tatkal")

    def cancelTicket(self):
        # if self.seats>0:
        self.seats = self.seats + 1
        print('A ticket is got cancelled.')

intersity = Train("Intersity Express 13232", 500, 10)
intersity.getstatus()
intersity.getSeatStatus()
intersity.fareInfo()
intersity.bookTicket()
intersity.bookTicket()
intersity.cancelTicket()
intersity.bookTicket()
intersity.getSeatStatus()


"""Can you change a self parameter inside a class to something else (say 'abhishek'). Try changing self to 'slf' or 'abhishek' and see the effects."""

class sample:
    def __init__(abhishek, name):
        abhishek.name = name

obj = sample("aniket")
print(obj.name)

#if we use any other name instead of self then also It will work.


    