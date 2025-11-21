percent = int(input("enter percent : "))
score = int(input("enter score : "))
if(percent>=90 and score>=90):
    print("addmissin in elite program")
elif(percent>=80 and score>=70):
    print("addmissin in standard program")
elif(percent>=60 and score>=50):
    print("addmissin in basic program")
else:
    print("not eligible")