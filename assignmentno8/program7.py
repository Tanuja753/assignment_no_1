def findmax(n1,n2):
    if(n1>n2):
        print(n1," is greater")
    elif(n1==n2):
        print("both are equal")
    else:
        print(n2," is greater")
num1 =int(input("enter num1 : "))
num2 =int(input("enter num2 : "))
findmax(num1,num2)