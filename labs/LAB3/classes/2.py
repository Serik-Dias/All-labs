class Shape:
    def area(self): # <- method of the class Shape
        return 0
class Square(Shape): # класс Square наследник Shape
    def __init__(self,length): # <- Конструктор для задания длины стороны
        self.length = length
    def area(self):
        return self.length ** 2
    
a = float(input("Enter: "))
a_square = Square(a) # <- create the object

print("area of a square: ", a_square.area())
a_shape = Shape() # <- it's also object

print("Another shape: ", a_shape.area())