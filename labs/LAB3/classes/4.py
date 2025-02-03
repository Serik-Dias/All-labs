import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    
    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance 

a = float(input("Enter x: "))
b = float(input("Enter y: "))

p1 = Point(a, b)
p2 = Point(a, b) 

p1.show()


k = float(input("x1: "))
p = float(input("y1: "))
p1.move(k, p)
p1.show()

distance = p1.dist(p2)
print(f"Distance between point1 and point2: {distance}.")