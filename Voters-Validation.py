# BSCIT-05-0836/2022
# Get age input from the user
age = int(input("Enter your age: "))
country = input("Enter your country of citizenship: ").lower()

citizen=["tanzania", "kenya", "uganda"]

# Check eligibility
if age >= 18 and country in citizen:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")
    if age < 18:
        print("You must be at least 18 years old.")
    if country not in citizen:
        print("You must be a citizen of Tanzania, Kenya, or Uganda.")
