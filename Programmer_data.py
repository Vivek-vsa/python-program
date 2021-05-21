class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


vicky = Programmer("vicky", "Skype")
alka = Programmer("Alka", "GitHub")
vicky.getInfo()
alka.getInfo()
