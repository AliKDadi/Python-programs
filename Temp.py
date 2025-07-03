# Temperature Converter: Celsius ↔ Fahrenheit

def celsius_to_fahrenheit(c):
    return (9/5) * c + 32

def fahrenheit_to_celsius(f):
    return (5/9) * (f - 32)

# Prompt user input
temp = input("Enter temperature (e.g., 60C or 45F): ").strip()

# Extract the value and unit
if temp[-1].upper() == 'C':
    c = float(temp[:-1])
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C is {round(f)} in Fahrenheit")
elif temp[-1].upper() == 'F':
    f = float(temp[:-1])
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F is {round(c)} in Celsius")
else:
    print("Invalid input. Please end the temperature with 'C' or 'F'.")
