class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width 
    def area(self):
        return self.length * self.width
    
a = float(input("Enter: "))
b = float(input("Enter: "))
a_rectangle = Rectangle(a,b)


print(f"Area of the Rectangle:",a_rectangle.area())