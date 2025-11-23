def table(n):
    print("table of : ",n)
    i =1
    while(i<=10):
        print(n,"*",i," = ",n*i)
        i = i+1


num = int(input("enter a number : "))
table(num)