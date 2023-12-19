inputString = input("Enter the site address : ")
Domain_name = ""
x = inputString.split("/")

if(x[0] == "https:" or x[0] == "http:"):
    x = x[2].split(".")

else:
    x = x[0].split(".")

if(len(x) == 2):
    Domain_name = ".".join(x[0:])

else:
    Domain_name = ".".join(x[1:3])

print(Domain_name)
