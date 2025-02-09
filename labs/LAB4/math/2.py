import math

def degree_to_radian(degree):
    return round(math.radians(degree), 6)

degree = 15
print(f"Input degree: {degree}")
print(f"Output radian: {degree_to_radian(degree)}")