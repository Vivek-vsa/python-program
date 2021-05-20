class Employee:
    company = "Google"
    salary = 1000

vicky = Employee()
rajni = Employee()
vicky.salary = 300
rajni.salary = 400 #if we dont give here this salary it will give us 1000 salary in output which is present in class employee

print(vicky.company)
print(rajni.company)
Employee.company = "YouTube"
print(vicky.company)
print(rajni.company)
print(vicky.salary)
print(rajni.salary)