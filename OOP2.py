class Dog():
    #class object attribute, same for any instance of the class
    #class object is something that going to true for any instance of the class
    species = "Mammal"

    def __init__(self, breed, name):
        self.breed = breed      #assigning breed parameter value to breed attribute (class variables) using the self keyword
        self.name = name

    def bark(self, age):
        print("WooF! My name is {} and my age is {}".format(self.name,age)) 
        #for age we are not using the 'self' keyword coz the user is providing it during function call
        #we are not referencing some particular attribute for that instance of class like we did in name

myDog = Dog('Lab','Rocky')      
#during creatig of an object we need to pass the arguements if any parameter is present in the init method 
#because when we create an instance of a class it calls the init method 
print(myDog.breed)
print(myDog.name)
print(myDog.species)    #this attribute not connected to any particular instances or self so its a class object attribute
myDog.bark(12)    #calling the bark method 