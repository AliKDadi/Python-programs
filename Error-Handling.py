#BSCIT-05-0836/2022
#Error and Exception Handling
def divide_numbers():
    try:
#Prompt user to enter 2 numbers
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

#Convert the two numbers into integers        
        num1 = int(num1)
        num2 = int(num2)

#Perform the division        
        result = num1 / num2

#Handle the cases
    except ValueError:
        print("\nInvalid input: Please enter numeric values only.")
    
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero. Please enter a non-zero second number.")
    
    else:
        print(f"The result of dividing {num1} by {num2} is {result}")
    
    finally:
        print("Division attempt concluded.")

#Call the function to execute it
divide_numbers()
