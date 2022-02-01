import math

class Circle:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value")

        if 0 > radius and radius > 1000:
            raise ValueError("Radius must be in the range of 0 to 1000")

        self.radius = radius

    def diameter(self):
        return round(2 * self.radius, 2)

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)




        