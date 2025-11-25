def checkprime(n):
    if(n>1):
        i =2
        while(i<n):
            if(n%i==0):
                print("not prime")
                break
            i=i+1
        else:
            print("prime")
            
num = int(input("enter num : "))
checkprime(num)
