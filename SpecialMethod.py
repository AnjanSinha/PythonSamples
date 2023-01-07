class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) :     #This special "__str__" method returns String representation of the object
        return f"{self.title} by {self.author}"     #the 'f' string literal format is used to contain expressions inside curly braces which will be replaced with their values.

    def __len__(self):      #This special method returns the length of the object 
        return self.pages
    
    #def __del__(self):
        #print( "A book object has been deleted.")

b = Book("Python", "Anjan" , 23)
print(b)
#Without the special method if we print the object then it will simply return the place where the object is saved in 
# memory as a string representation
print(len(b)) 
#Without the len special method it will return an error
