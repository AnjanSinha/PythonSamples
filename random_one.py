def covert_seconds(seconds):
    hours=(seconds//3600)
    minutes=(seconds-hours*3600)//60
    r_seconds=(seconds-hours*3600-minutes*60)
    return hours,minutes,r_seconds

h,m,s= covert_seconds(5000)
print(h,m,s)