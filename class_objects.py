class Employee:
    company = 'Google'

    def getsalary(self):
        print(f"salary is {self.salary}")

abhishek = Employee()
abhishek.company = 'youtube'
abhishek.salary = 1000000

print(abhishek.salary)
print(abhishek.company)
abhishek.getsalary() #this line is same as Employee.getsalary(abhishek): we are giving one attribute. So, we need to put self as an attribute.