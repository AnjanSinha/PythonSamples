class Circle ():
    #Class object attribute
    pi = 3.14

    #Special INIT method, always called during creation of an instance(Object)
    def __init__(self,radius = 1):      #default value of the radius parameter is 1 but it can be overridden
        self.radius = radius
        self.area = radius **2 * self.pi    #As pi is a class object attribute we can reference
                                            #it using className.pi in this case Circle.pi , its easy to understand for other who are using your code

    #Method
    def get_circumference(self):
        return  self.radius * self.pi * 2

MyCircle = Circle(30)       #Overriding default value by giving arguments
print(MyCircle.pi)
print(MyCircle.get_circumference())
print(MyCircle.area)