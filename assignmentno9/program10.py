def checkperfect(n):
    i=1
    sum =0
    while(i<n):
        if(n%i==0):
            sum =sum+i
        i=i+1
    if(sum == n):
        print(n," is perfect number")
    else:
        print(n," is not perfect number")
n = int(input("enter num : "))
checkperfect(n)