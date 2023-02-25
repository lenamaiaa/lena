from math import pi
class circle:
    def __init__(self,radius):
        self.radius = radius

    def circum(self):
        circum = self.radius * 2 * pi
        return circum

    def area(self):
        area = self.radius ** 2 * pi
        return area



