ang1 = int(input("enter angle 1 : "))
ang2 = int(input("enter angle 2 : "))
ang3 = int(input("enter angle 3 : "))
if(ang1+ang2+ang3 == 180):
    if(ang1<90 and ang2 <90 and ang3 <90):
        print("triangle is acute")
    elif(ang1 >90 or ang2>90 or ang3>90):
        print("triangle is obtuse")
else:
    print("invalid triangle")