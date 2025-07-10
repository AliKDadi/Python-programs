#BSCIT-05-0836/2022
#Base class for all employees
class Employee:
    def __init__(self, emp_id, name):

#instance variables
        self.emp_id = emp_id
        self.name = name
        
#Abstract method to calculate the weekly payroll.
    def calculate_payroll(self):

        raise NotImplementedError("Subclasses must implement calculate_payroll method")


#Derived class for salary-based employees
class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):

#Inherit from Employee
        super().__init__(emp_id, name)  
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


#Derived class for hourly-based employees
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):

#Inherit from Employee
        super().__init__(emp_id, name)  
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


#Derived class for commission-based employees
class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission):

#Inherit from SalaryEmployee
        super().__init__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission


#Function to prompt the user for employee details
def get_employee_details():
    print("\n--- Employee Details ---")
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    employee_type = input("Enter Employee Type (salary/hourly/commission): ").lower()

    if employee_type == "salary":
        weekly_salary = float(input("Enter Weekly Salary: "))
        return SalaryEmployee(emp_id, name, weekly_salary)

    elif employee_type == "hourly":
        hours_worked = float(input("Enter Hours Worked: "))
        hourly_rate = float(input("Enter Hourly Rate: "))
        return HourlyEmployee(emp_id, name, hours_worked, hourly_rate)

    elif employee_type == "commission":
        weekly_salary = float(input("Enter Weekly Salary: "))
        commission = float(input("Enter Commission: "))
        return CommissionEmployee(emp_id, name, weekly_salary, commission)

    else:
        print("Invalid Employee Type. Please enter 'salary', 'hourly', or 'commission'.")
        return None


#Main function to run the program
def main():

    print("Welcome to the Simple Payroll System!")
    
    while True:
        employee = get_employee_details()
        
        if employee:
            print(f"\nEmployee ID: {employee.emp_id}")
            print(f"Name: {employee.name}")
            print(f"Weekly Payroll: Kshs {employee.calculate_payroll():.2f}")
        
        choice = input("\nProcess another employee? (yes/no): ").lower()
        if choice != "yes":
            break

    print("\nThank you for using the Simple Payroll System!")


#Run the program
if __name__ == "__main__":
    main()
