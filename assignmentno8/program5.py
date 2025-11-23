def check(ch):
    if(len(ch)==1):
        if(65<=ord(ch)<=90 or 97<=ord(ch)<=122):
            if(ch =='a' or ch=='A' or ch =='e' or ch=='E'or ch =='i' or ch=='I' or ch =='o' or ch=='O' or ch =='u' or ch=='U'):
                print(ch," is vowel")
            else:
                print(ch," is consonant")
ch =input("enter character : ")
check(ch)