from math import pi
class cylinder:
    def __init__(self,radius,height):
        super().__init__(radius)
        self.height = height


    def volume(self):
      return pi * self.radius ** 2* self.height


    def area(self):
        return self.circ() * self.height

    def get_base(self):
        return super()

    def area_of_base(self):
        return super().area()