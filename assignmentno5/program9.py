ch = input("enter a character : ")
if((ch >='A' and ch<='Z') or (ch>='a' and ch<='z')):
    if(ch == 'a' or ch =='A' or ch == 'e' or ch =='E' or ch == 'i' or ch =='I' or ch == 'o' or ch =='O' or ch == 'u' or ch =='U'):
        print(ch," is vowel")
    else:
        print(ch," is consonant")
else:
    print("invalid character")