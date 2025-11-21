units = int(input("enter  units : "))
if(1<= units <= 100):
    print("total bill: ",units*5)
elif(101 <= units <= 200):
    print("toatl bill: ",units*7)
elif(201 <= units <= 300):
    print("toatl bill: ",units*10)
elif(units< 300):
    print("toatl bill: ",units*15)