import math

class Circle:
    #constructor
    def __init__(self, radius):
        self.radius = radius

#function to calculate area of a circle
    def getArea(self):
        return math.pi * self.radius ** 2

#function to calculate the circumference of a circle
    def getCircumference(self):
        return 2 * math.pi * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print(f"Area of the circle: {circle.getArea():.2f}")
print(f"Circumference of the circle: {circle.getCircumference():.2f}")
