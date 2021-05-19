class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

vicky = Employee()
vicky.salary = 100000
vicky.getSalary() # Employee.getSalary(vicky)