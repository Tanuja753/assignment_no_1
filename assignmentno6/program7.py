num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
if(num1 % 2 == 1 and num2 % 2 ==1):
    sum = num1+num2
    print(sum)
else:
    print(num1," and ",num2," both are not odd")