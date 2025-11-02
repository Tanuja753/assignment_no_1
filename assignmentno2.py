#Q1
x = 15
y = 4
print("Addition : ",x+y)        #Addition :  19
print("Substraction : ",x-y)        #Substraction :  11
print("Multiplication : ",x*y)      #Multiplication :  60
print("Division : ",x/y)        #Division :  3.75
print("Modulus : ",x%y)     #Modulus :  3
print("Floor Division : ",x//y)     #Floor Division :  3
print("Exponention : ",x**y)    #Exponention :  50625

#Q2
num = 50
num += 10
print("Addition Assignment : ",num)     #Addition Assignment :  60
num -= 5
print("Substraction Assignment : ",num)     #Substraction Assignment :  55
num *= 2
print("Multiplication Assignment : ",num)       #Multiplication Assignment :  110
num /= 4
print("Division Assignment : ",num)     #Division Assignment :  27.5
num %= 5
print("Modulus Assignment : ",num)  #Modulus Assignment :  2.5
num = 50
num //= 3
print("Floor Division Assignment : ", num)   #Floor Division Assignment :  16git

#Q3
a = 25
b = 30
print("is a equals to b :",a==b)    #is a equals to b : False
print("is a  not equals to b :",a!=b)   #is a  not equals to b : True
print("is a less than equals to b :",a<=b)  #is a less than equals to b : True
print("is a greater than equals to b :",a>=b)   #is a greater than equals to b : False
print("is a less than to b :",a<b)  #is a less than to b : True
print("is a greater than to b :",a>b)   #is a greater than to b : False

#Q4
l= 10
m = 20 
n = 30
print(l)    #10
print(m)    #20
print(n)    #30
print(l<m and m < n)    #True
print(l>m or m < n) #True
print(not(l==m))    #True

#Q5
v= 100
w = 100
print(v)    #100
print(w)    #100
print(id(v))    #140725340606472
print(id(w))    #140725340606472
print("v is w : ",v is w)   #v is w :  True
print("v is not w : ",v is not w)   #v is not w :  False

list1= [1,2,3]
list2 = [1,2,3]
print(list1)    #[1,2,3]
print(list2)    #[1,2,3]
print(id(list1))    #2253178626368
print(id(list2))    #2253178774976
print("list1 is list2 : ",list1 is list2)   #list1 is list2 :  False
print("list1 is not list2 : ",list1 is not list2)   #list1 is not list2 :  True
print("list1 == list2 : ",list1 == list2)   #list1 == list2 :  True


#Q6
colors = ["red","blue","green","yellow"]
print("blue in colors : ","blue" in colors) #blue in colors :  True
print("purple in colors : ","purple" in colors) #purple in colors :  False
print("pink not in colors : ","pink" not in colors)#pink not in colors :  True
print("red not in colors : ","red" not in colors)   #red not in colors :  False

#Q7
j = 12 
k = 10
print(j)    #12
print(k)    #10
print("j & k (Bitwise and) : ",j & k)   #j & k (Bitwise and) :  8
print("j | k (Bitwise or) : ",j | k)    #j | k (Bitwise or) :  14
print("j ^ k (Bitwise ex or) : ",j ^ k) #j ^ k (Bitwise ex or) :  6
print("j << 2 (Bitwise left shift) : ",j << 2)  #j << 2 (Bitwise left shift) :  48
print("j >> 2 (Bitwise right shift) : ",j >> 2) #j >> 2 (Bitwise right shift) :  3
print("~j  (Bitwise not) : ",~j)    #~j  (Bitwise not) :  -13

#Q8
intval = 10
floatval = 5.5
stringval = "python" 
print(" original values : ")    #original values :
print("intval : ",intval)   #intval :  10
print("type",type(intval))  #type <class 'int'>
print("floatval : ",floatval)   #floatval :  5.5
print("type",type(floatval))    #type <class 'float'>
print("stringval : ",stringval) #stringval :  python
print("type",type(stringval))   #type <class 'str'>

print("intval + floatval : ",intval+floatval,type(intval+floatval)) #intval + floatval :  15.5 <class 'float'>
print("intval * floatval : ",intval*floatval,type(intval*floatval)) #intval * floatval :  55.0 <class 'float'>
print("floatval / inttval : ",floatval/intval,type(floatval/intval))    #floatval / inttval :  0.55 <class 'float'>
print("stringval * 2 : ",stringval *2,type(stringval *2))   #stringval * 2 :  pythonpython <class 'str'>

#Q9
first = "Hello"
second = "World"
print("first : ",first) #first :  Hello
print("second : ",second)   #second :  World
print("concatenation(first + ' '+second)",first + ' '+second)   #concatenation(first + ' '+second) Hello World
print("repitition (first * 3) : ",first *3) #repitition (first * 3) :  HelloHelloHello
print("repitition(second * 2) : ",second *2)    #repitition(second * 2) :  WorldWorld
print("combined((first+' ')*2+second) : ",(first+' ')*2+second) #combined((first+' ')*2+second) :  Hello Hello World

#Q10
p = 10
q = 5
r = 3
print(p)    #10
print(q)    #5
print(r)    #3
print("p+q*r : ",p+q*r) #p+q*r :  25
print("(p+q)*r : ",(p+q)*r) #(p+q)*r :  45
print("p**q : ",p**q)   #
print("p<q and q>r or p == 10",p<q and q>r or p == 10)  #p<q and q>r or p == 10 True




