class Employee:
    company = "Google"
    salary = 100

vicky = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# vicky.salary = 300
# rajni.salary = 400
vicky.salary = 45
print(vicky.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 