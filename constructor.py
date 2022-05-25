class Employee:
    company = 'Google'

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print('Employee is created')

    def employeeDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")


    def getsalary(self):
        print(f"salary is {self.salary}")

    @staticmethod
    def final():
        print("Thanks everyone!!")

abhishek = Employee('abhishek', 500000, 'Data_science')
abhishek = 
abhishek.company = 'youtube'
abhishek.salary = 1000000

print(abhishek.salary)
print(abhishek.company)
abhishek.employeeDetails()
abhishek.final()