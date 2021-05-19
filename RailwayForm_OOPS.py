import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

vickysApplication = RailwayForm()
vickysApplication.name = "Vicky"
vickysApplication.train = "Mahalakshmi Express"
vickysApplication.printData()