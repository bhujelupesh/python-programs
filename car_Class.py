class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"
    
    def display(self):
        print(f"{self.year} {self.make} {self.model} is the given informations")
    
car1 = Car("BMW","R1",2005,"Red")
print(car1)
car1.color = "Yellow"
del car1.color 
car1.display()