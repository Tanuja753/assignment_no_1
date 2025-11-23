def average(*value):
    sum = 0
    for val in value:
        sum = sum +val
    avg= sum/len(value)
    print("average of your numbers is : ",avg)
average(10,20,30,40,50)

def outer():
    return "Hello,I'm inner function!"
ans = outer()
print(ans)