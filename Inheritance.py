#Base Class
class Animal():

    def __init__(self):
        print("Animal class instance is created.")

    def WhoAmI(self):
        print("I am animal")

    def Eat (self):
        print("I am eating.")

#Derived Class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)       #another insatance created of animal class in dogclass
        print("Dog class instance Created")

    def WhoAmI(self):       #overriding base class method of "WhoAmI()"
        print("I am a Dog.")

    def Bark(self):
        print("Woof!")

myAnimal = Animal()     #Base class init method will be executed at the time of object creation so it'll print "Animal is created."
myDog = Dog()       #base class init method will executed here too coz creating instance for derived class that has inherited base class
myDog.Eat()     #inheriting the base class method
myDog.WhoAmI()      #Calling the overridden method 
myAnimal.WhoAmI()   #Calling the Base class method 
myDog.Bark()        #A new method that resides in inherited class but not present in the base class
