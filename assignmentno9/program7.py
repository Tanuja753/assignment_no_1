def factorial(n):
    fact =1
    if(n ==0):
        return 1
    else:
        i=1
        while(i<=n):
            fact = fact*i
            i=i+1
        return fact
n = int(input("enter num : "))
retval = factorial(n)
print(retval)