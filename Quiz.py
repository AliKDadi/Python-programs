#BMI calculator program
#Prompt user to enter weight and height
weight=float(input("Enter your weight in kilograms:"))
height=float(input("Enter your height in metres:"))

#Checking for non-positive values to prevent negative BMI
if weight<=0 or height<=0:
    print("\nWeight and Height must be positive values.")

#Calculate BMI
BMI=weight/(height**2)

#Classify BMI and display result
print(f"\nYour BMI is: {BMI:.2f}")

if BMI<18.5:
    print("Category: Underweight")
elif 18.5<=BMI<=24.9:
    print("Category: Normal weight")
elif 25<=BMI<=29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")
