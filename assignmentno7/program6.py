ch = input("enter character : ")
if(len(ch)==1):
    if(65<=ord(ch)<=90):
        print("uppercase letter")
    elif(97<=ord(ch)<=122):
        print("lowercase letter")
    elif(48<=ord(ch)<=57):
        print("digit")
    else:
        print("special character")
    