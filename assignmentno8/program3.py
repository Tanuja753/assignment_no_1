def iseligible(age):
    if(age>0):
        if(age>=18):
            print("can vote")
        else:
            print("cannot vote")
    else:
        print("invalid age")
    
age= int(input("enter age : "))
iseligible(age)