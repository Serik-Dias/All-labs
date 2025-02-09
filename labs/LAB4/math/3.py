import math

def regular_polygon_area(n_sides, side_length):
    return (n_sides * side_length**2) / (4 * math.tan(math.pi / n_sides))

n_sides = 4
side_length = 25
print(f"\nInput number of sides: {n_sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {regular_polygon_area(n_sides, side_length)}")