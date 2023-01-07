class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return ( self.name  +" says Woof!")

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):        #Same method name in different class
        return (self.name +" says Mew!")

mydog = Dog("Lalu")
mycat = Cat("Billi")

def petType(type):
    print(type.speak())

#Working differently on different arguements means Dog class calling its method so as the Cat class though they have the same name.
petType(mycat)
petType(mydog)