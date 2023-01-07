count=0
Sum=0
print('Before',count,Sum)
for value in [9,41,12,3,74,15]:
    count=count+1
    Sum=Sum+value
    print(count,Sum,value)
print('After',count,Sum,Sum/count)
0