class main():
    def LuckyNum(self,number):
        luckydig = ['4','7']
        number = str(number)
        for i in number:
            if i not in luckydig:
                return False
        return True
        
    def almostLucky(self,num):
        if num < 0:
            return False
        elif self.LuckyNum(num):
            return False
    
        arr =[]
        for i in range(1,(num//2)+1):
            if num % i == 0:
                arr.append(i)
            
        for i in arr:
            if self.LuckyNum(i) == True:
                return True
        return False
    
if __name__ == "__main__":
    obj = main()
    n = int(input())
    result = obj.almostLucky(n)
    print(result)
    