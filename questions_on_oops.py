"""Create a class C2d Vector and use it to create another class representing a 3D vector."""

class C2DVec():
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f"{self.i}i + {self.j}j"

class C3DVec(C2DVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

vec1 = C2DVec(1,3)
vec2 = C3DVec(1,4,5)
print(vec1)
print(vec2)

"""Create a class pets from a class animals and further create a class Dog from pets. Add a method bark to class Dog"""

class Animals():
    pass

class Dog(Animals):
    
    @staticmethod
    def bark():
        print('Dogs keep barking')

class pets(Dog):
    pass


obj = Animals()
obj1 = Dog()
obj2 = pets()
obj1.bark()


"""Create a class Employee and add salary increment properties to it. write a method salary after increment method with a property decorator with a setter 
which changes the value of increment based on the salary"""

class Employee():
    salary = 5000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary


e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 100000
print(e.salaryAfterIncrement)
print(e.increment)

"""write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them"""

"""To show the results of a __add__, __mul__ etc. use __str__ method """


(a + bi)(c + di) = (ac -bd) + (ad + bc)i 
(a + bi) + (c + di) = (a + c) + (b + d)i
class Complex():
    def __init__(self, i, j):
        self.real = i
        self.imaginary = j 

    def __add__(self, c):
        return Complex(self.real + c.real , self.imaginary + c.imaginary)

    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImaginary = self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulReal, mulImaginary)

    def __str__(self):
        return f"{self.real}i + {self.imaginary}j"

c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1 + c2)
print(c1*c2)

""" write a class vector representing a vector of n dimension. overload the + and * operator which calculates the sum and the dot product of them"""

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 = str1 + f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        new_list = []
        for i in range(len(self.vec)):
            new_list.append(self.vec[i] + vec2.vec[i])
        return Vector(new_list)

    def __mul__(self, vec2):
        new_list = []
        for i in range(len(self.vec)):
            new_list.append(self.vec[i]*vec2.vec[i])
        return Vector(new_list)


v1 = Vector([1,4])
v2 = Vector([3,4])
print(v1+ v2)
print(v1*v2)

"""write a __str__ method to print the vector as follows: 7i + 8j + 10k. Assume vector of dimension 3 for this problem and also print length of the vector."""

class Vector:
    def __init__(self, vec):
            self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

    def __len__(self):
        return(len(self.vec))

v = Vector([7,8,10])
print(v)
print(len(v))