temp = int(input("enter temprature : "))
if(temp <0):
    print("freezing cold")
elif(0<= temp <= 10):
    print("very cold")
elif(11 <= temp <= 20):
    print("cold")
elif( 21 <= temp <= 30):
    print("warm")
elif( 31 <= temp <= 40):
    print("hot")
elif( temp< 40):
    print("extreme hot")
