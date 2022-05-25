class Employee:
    company = 'Google'
    def getsalary(self, signature):
        print(f"My company name is {self.company} and salary is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning sir")

abhishek = Employee()
abhishek.company = 'youtube'
abhishek.salary = 1000000
abhishek.getsalary('Thanks buddy!!')
print(abhishek.salary)
# print(abhishek.company)
abhishek.greet()