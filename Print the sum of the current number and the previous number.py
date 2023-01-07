ran = int(input("Enter the range :- "))
cnum =0
pnum = 0
while cnum < ran:
    print("Previous number : ",pnum,"Current Number : ",cnum,"Sum : ",cnum+pnum)
    cnum=cnum+1
    pnum=cnum-1
    