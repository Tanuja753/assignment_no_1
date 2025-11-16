angle1 = int(input("enter angle 1: "))
angle2 =int(input("enter angle 2: "))
angle3 = int(input("enter angle 3: "))
if(angle1+angle2+angle3 == 180):
    if(angle1 == 90 or angle2 ==90 or angle3 == 90):
        print("it is a right angle triangle")
    else:
        print("it is not right angle triangle")
else:
    print("it is not triangle")