income = int(input("enter income : "))
tax =0
if(1<= income <=250000):
    print("no tax")
elif(250001 <= income <= 500000):
    tax = (5*income)/100
    print("tax to be paid : ",tax)
elif(500001 <= income <= 1000000):
    tax = (20*income)/100
    print("tax to be paid : ",tax)
elif( income >= 1000000):
    tax = (30*income)/100
    print("tax to be paid : ",tax)