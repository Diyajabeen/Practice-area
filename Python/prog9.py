
import math

'''Base class'''
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area() method")
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()method")

'''deriver clss circle'''
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * (self.radius**2)
    def perimeter(self):
        return 2* math.pi*self.radius

'''derived class rectangle'''
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)

'''polymorphic function'''
def print_shape_info(shape):
    print(f"Shape type:{shape.__class__.__name__}")
    print(f"area:{shape.area():.2f}")
    print(f"perimeter:{shape.perimeter():.2f}")
    print("-"*30)

circle=Circle(5)
rectangle=Rectangle(4,6)

print_shape_info(circle)
print_shape_info(rectangle)