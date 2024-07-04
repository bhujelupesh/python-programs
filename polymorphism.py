class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

shapes = [Circle(5), Rectangle(8, 5)]

for shape in shapes:
    print(shape.area())

circle = Circle(6)    
print(circle.area())