def checkcomposite(n):
    if(n>1):
        i =2
        while(i<n):
            if(n%i==0):
                print("composite")
                break
            i=i+1
        else:
            print("not composite")
            
num = int(input("enter num : "))
checkcomposite(num)
