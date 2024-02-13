import math

# The Shape Class is the base class for the Square and Circle classes
class Shape:
    def __init__(self, name):
        self.name = name

    def perimeter(sefl):
        raise NotImplementedError("Perimeter not implemented")
    
    def area(self):
        raise NotImplementedError("Area not implemented")

# The Square Class Inhence of Shape and Polimofysm implement the area and perimeter  
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

# The Circle Class Inhence of Shape and Polimofysm implement the area and perimeter
class Circle(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def perimeter(self):
        return 2 * math.pi * self.side

    def area(self):
        return self.side ** 2
    


examples = [Square("sq", 3), Circle("ci", 2)]
for thing in examples:
    n = thing.name
    p = thing.perimeter()
    a = thing.area()
    print(f"{n} has perimeter {p:.2f} and area {a:.2f}")