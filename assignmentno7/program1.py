age = int(input("enter age : "))
weight = float(input("enter weight : "))
hb = float(input("enter hb : "))
if(18 <= age <=65 and weight< 50 and hb <12.5):
    print("eligible for blood donation")
else:
    print("not eligible for blood donation")
