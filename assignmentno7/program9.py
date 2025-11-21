amount = int(input("enter amount : "))
discount =0
if(1 <= amount <= 1000):
    print("no discount")
elif(1000 <= amount <= 4999):
    discount=(5*amount)/100
    print("dicount applide : 5%")
    print("final amount: ",amount-discount)
elif(5000 <= amount<= 9999):
    discount=(10*amount)/100
    print("dicount applide : 10%")
    print("final amount: ",amount-discount)
elif(10000<=amount<= 20000):
    discount=(20*amount)/100
    print("dicount applide : 20%")
    print("final amount: ",amount-discount)
elif(amount>= 20000):
    discount=(30*amount)/100
    print("dicount applide : 30%")
    print("final amount: ",amount-discount)