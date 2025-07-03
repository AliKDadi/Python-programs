# BSCIT-05-0836/2022
# Get input from the user
students = {}

for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    height = int(input(f"Enter height of {name} in cm: "))
    students[name] = height

# Find the tallest student
tallest = max(students, key=students.get)

# Print individual height info
print("\nHeight Info:")
for name, height in students.items():
    print(f"{name} {height}cm")

# Print the result
print(f"{tallest.capitalize()} is the tallest")
