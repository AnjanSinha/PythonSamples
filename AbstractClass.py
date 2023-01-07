#When we want a particluar method name to be same for different type of classes then we use abstract method
#Example- If we want to create a method "OpenFiles" for different type of classes that accept different types of files(csv,docx) 
#csv.OpenFiles , docx.Openfiles etc
class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):    #This method is present only to be overridden in subclass and implemented through subclass
        raise NotImplementedError("Subclass can implement this abstract method")

class Dog(Animal):
    def speak(self):    #Overriding the speak method from Superclass
        return self.name + " says woof"

class Cat (Animal):
    def speak(self):
        return self.name + " says mew"

myAnimal = Animal("Rocky")
#myAnimal.speak()       #if we call this method from Super Class/Base class itll raise an error it can only be accessed from subclass

myDog = Dog("Rocky")
myCat = Cat("Sudo")

print(myDog.speak())    #Accessing the speak method from subclass
print(myCat.speak())