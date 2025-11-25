def findavg():
    sum=0
    i=1
    while(i<=5):
        m= int(input("enter num: "))
        sum = sum+m
        i=i+1
    avg= sum/5
    return avg
retval=findavg()
print(retval)