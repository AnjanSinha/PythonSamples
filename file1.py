class main():
    def add(self,x,y):
        return x+y

print(f"The source file is {__name__}")

if __name__ == '__main__':
    calc = main()
    print(calc.add(45,40))