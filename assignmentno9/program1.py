def maxthree(x,y,z):
    if(x>y and x>z):
        return x
    elif(y>z):
        return y
    else:
        return z
num1 =int(input("enter num1 : "))
num2 =int(input("enter num2 : "))
num3 =int(input("enter num3 : "))
maxval=maxthree(num1,num2,num3)
print(maxval)