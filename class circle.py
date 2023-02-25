from math import pi
class circle:
    def __init__(self,radius):
        self.radius = radius

    def circum(self):
        circum = self.radius * 2 * pi
        return circum

c1 = circle(6)
c2 = circle(8)
print(c1.circum())
















