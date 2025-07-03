#BSCIT-05-0836/2022
#Class Program
class Employee:
#Class variable
    company_name="TechSolutions Ltd"

#Constructor with default position
    def __init__(self, name, position="Junior Developer"):
        self.name=name
        self.position=position

#Method to display emmployee details
    def display_details(self):
        print("Employee Name:", self.name)
        print("Position:", self.position)
        print("Company:", Employee.company_name)
        print()

#Create employee objects
emp1=Employee("Ali", "Project Manager")
emp2=Employee("Dadi") #Default position

#Call display_details
emp1.display_details()
emp2.display_details()




