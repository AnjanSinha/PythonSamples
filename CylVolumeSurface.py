class Cylinder:

    def __init__(self,height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def Volume(self):
        return (3.14)*((self.radius)**2)*self.height

    def surfaceArea(self):
        return (2*3.14*self.radius*self.height)+(2*3.14*((self.radius)**2))

mycylinder = Cylinder(2,3)
print(mycylinder.Volume())
print(mycylinder.surfaceArea())