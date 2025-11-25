def sumBenRange(n1,n2):
    i=n1
    sum=0
    while(i<=n2):
        sum = sum+i
        i=i+1
    return sum
num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
retval=sumBenRange(num1,num2)
print(retval)