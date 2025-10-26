"""
print(int(123.456))
#print(int(10+20j))
print(int(True))
print(int(False))
print(int("100"))
#print(int("100.78"))
#print(int("Hello"))
print(int(0b1111))
print(int('0b1111'))

print(float(10))
print(float(True))
print(float(False))
print(float('12'))
print(float('12.89'))
#print(float('Hello'))
#print(float('0b1111'))
print(float(0b1111))
#print(float(10+5j))

print(complex(10,-2))
print(complex(10.45,5))
print(complex(True,False))

print(bool(0))
print(bool(10))
print(bool(20.7))
print(bool(0.0))
print(bool(1+0j))
print(bool(10+20j))
print(bool(0+0j))
print(bool("True"))
print(bool("False"))
print(bool("QACircle"))
print(bool(""))
print(bool(" "))

print(str(10))
print(str(10.5))
print(str(10+5j))
print(str(True)) """

"""a=257
b=257
print(a is b)
print(a == b)

a=10+5j
b=10+5j
print(a is b)
print(a == b) 

a=10
b=2

print("a+b =",a+b)
print("a-b =",a-b)
print("a*b =",a*b)
print("a/b =",a/b)
print("a**b =",a**b)
print("a//b =",a//b)
print("a%b =",a%b)


s1="QACircle "
s2="Python Training"

#print(s1+" "+s2)
print(s1+s2)
# print(s1+a) ==>TypeError: can only concatenate str (not "int") to str
#print(s1*s2) ==>TypeError: can't multiply sequence by non-int of type 'str'
print(s1*5) 

a=10
b=20
print("a==b =",a==b)
print("a!=b =",a!=b)
print("a>b =",a>b)
print("a<b =",a<b)
print("a>=b =",a>=b)
print("a<=b =",a<=b)

print("*********************************")
a="QACircle"
b="QACircle"
print("a==b =",a==b)
print("a!=b =",a!=b)
print("a>b =",a>b)
print("a<b =",a<b)
print("a>=b =",a>=b)
print("a<=b =",a<=b)
print(id(a), id(b))

print("*********************************")

a="QACircle"
b="qACircle"
print("a==b =",a==b)
print("a!=b =",a!=b)
print("a>b =",a>b)
print("a<b =",a<b)
print("a>=b =",a>=b)
print("a<=b =",a<=b)
print(id(a), id(b))

#Program 1
a="QACircle"
b="qACircle"

if a>b:
    print("a value is bigger than b")
else:
    print("b value is bigger than a")

print("***************Chaining Operation **********")
print(10<20<30<40<50)
print(10<20<30<40>50)  

#and
x=10
y=20
print(x and y)

a=100
b=0
print(a and b)

#OR
a=100
b=0
print(a or b)

x=10
y=20
print(x or y)

#Not
x=10
print(not x)
y=0
print(not y)


print("QACircle" and "QACircle")
print("" and "QACircle")
print(" " and "QACircle")

print("QACircle" or "QACircle")
print("" or "QACircle")
print(" " or "QACircle")

print(not "")
print(not "QACircle")


print(10 & 4)
print(10|4)
print(~-10)
print(~11)
print(10^4)
print(10<<2)
print(10>>2)



y=10
x=10
y+=100  # ==>y =y+100
print(y) 

x=100
print(x)
x+=1000 #==> x= x+1000 ==>100+1000 ==> 1100
print(x)
x-=20
print(x)
x*=2
print(x)
x/=5
print(x)
x//=10
print(x)
x%=10
print(x)
x**=2
print(x)





a=100
b=200
a+=b #==> a=a+b ==>100+200
print(a)

#WAP using ternary operator
a, b = 100, 20
x = a if a > b else b
print(x)

#Read 2 numbers from keyboad and print the minimum values
x = int(input("Enter the first value"))
y = int(input("Enter the second value"))
z = x if x < y else y
print("The minimum value is =", z)
print(type(z))

#Nested Ternary Operator
#Read 3 numbers from keyboad and print the minimum values
x = int(input("Enter the first value"))
y = int(input("Enter the second value"))
z = int(input("Enter the third value"))

minimum = x if x < y and x < z else y if y < z else z
print("The minimum value is =", minimum) 

# x = 100
# y = 100
# print(id(x))
# print(id(y))
# print(x is y)
# print(x is not y)
#
# a=200
# b=400
# print(a is not b)
#
# s="QACircle"
# s1="QACircle1"
# print(s is s1)
#
# l1=["Hello","Good Morning","Wake up"," Attend Python Class"]
# l2=["Hello","Good Morning","Wake up"," Attend Python Class"]
# print(id(l1))
# print(id(l2))
# print(l1 is l2)
# print(l1==l2)


l1=["Hello","Good Morning","Wake up","Attend Python Class"]

print("Python" in l1)
print("Attend Python Class" in l1)

s1="Welcome to the Python Class"
print("Welcome" in s1)
print("Java" not in s1) 

ename = input("Enter the employee name")
enum= input("Enter the employee ID")
esal= float(input("Enter the employee Salary"))
eadd= input("Enter the Employee Address")
married=bool(input("Enter the Employee marriage status?True|False"))

print("The employee Name is =", ename)
print("The employee number is =",enum)
print("The employee salary is =",esal)
print("The employee address is =",eadd)
print("The employee marriage status =",married)


#Case 1 ==> Print statement
print("Hello QACircle")

#case 2 ==> print statement and variable
age=76
print("Hello my age is ",age)

a,b,c=100,200,300
print("The values are =", a,b,c)
print("The values are =", a,b,c,sep=":")
print("The values are =", a,b,c,sep="")

#Case 3
print("Hello",end=" ")
print("QACircle",end=' ')
print("Training Academy")

#case 4 (string , variable list)
s="Basava"
age=30
s1="Python"
s2="Java"
print("Hello",s,"your age is",age)
print("You are teaching the following subjects like",s1,"and",s2)

#case 5 ==>print("formated string"%(Variable list))
a=100
s="Basavanagouda"
print("a value is %i"%a)
print("s name is %s"%s)

num=int(input("Enter the value :"))

add=num+5
print("The sum is %d"%add)

#case 6 replacement operator {}
name="QACircle"
age=4
TrainedCandidates=1000
NoofTrainers=10
print("Hello {} your age is {} and the No of Trained candidates {} "
      "with No of trainers count {}".format(name,age,TrainedCandidates,NoofTrainers))

print("Hello {x} your age is {y} and the No of Trained candidates {z} "
      "with No of trainers count {a}".format(a=NoofTrainers,x=name,y=age,z=TrainedCandidates)) """

# i=10
# if (i<15):
#     print("10 is less than 15")
#
# name=input("Enter the name")
# if name=="QACircle":
#     print("Welcome to",name,"Training Academy")
# print("Who are you")
#
# print("Python For Loop inside a For Loop")
# for i in range(1, 4):
#    for j in range(1,4):
#        print(i,j, end='  ')
#    print()
#
# name=input("Enter the name")
# if name=="QACircle":
#     print("Hello",name,"Good Morning")
# else:
#     print("Hello Guest Good Morning")
#
# print("How are you !!!!")
#
# brand = input("Enter your favorite brand :")
# if brand == "Teachers":
#     print("Its children's brand")
# elif brand =='KF':
#     print("It's not that much kick")
# elif brand == 'Becks Ice':
#     print("Its ok to test")
# elif brand == "FO":
#     print("Buy one get one free")
# else:
#     print("Other brands are not allowed ")
#
#
# n1=100
# n2=10
# n3=400
#
# if n1>n2 and n1>n3:
#     print("The bigger number is =",n1)
# elif n2>n3:
#     print("The bigger number is =", n2)
# else:
#     print("The bigger number is =", n3)
#
# #Write a program to print the characters present in the given string
#
# s1="QACircle Software Training Academy"
# for i in s1:
#     print(i)
#
#
# #Write a program to print the characters present in the given string along with index ( +ve and -ve)
# s2="Basavanagouda"
# i=0
# n=len(s2)
# print(n)
# for x in s2:
#     print("The Character ",x,"Present at the +ve index is",i,"and the -ve index is",(i-n))
#     i=i+1
#
# #write a program to print number from 0 t 10
# for x in range(11):
#     print(x)
#
# print("************************************")
# #WAP to print only Odd numbers from the range
# for i in range(101):
#     if i%2!=0:
#         print(i)
# print("************************************")
#
# #WAP to print only Even numbers from the list
# l=[10,12,13,15,17,19,18]
# for i in l:
#     if i%2==0:
#         print(i)
#
# print("************************************")
# #WAP to display from 10 to 1 in descending order
# for i in range(10,0,-1):
#     print(i)

# print("******************")
# #WAP to print the sum of numbers present in the list
# l=eval(input("Enter the list"))
# sum=0
# print(type(l))
# for x in l:
#     sum=sum+x
# print(sum)
#
# print("******************")
# #WAP to print dictionary objects using for loop
# d={'x':123,'y':345}
# print(d)
#
# for i in d:
#     print("%s  %d" %(i,d[i]))
#     print(i, d[i])
#
# #print only values from dictionary
# for x in d.values():
#     print(x)
#
# #print only keys from dictionary
# #Approach 1
# for x in d.keys():
#     print(x)
#
# #Approach 2
# for x in d:
#     print(x)

# print("Python for loop inside a another for loop")
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j,end="   ")
#     print()
#
# print("Write a Python program with tuple using for loop")
# t=10,20,30,40,50
# print(type(t))
# for i in t:
#     print(i)
#
# print("Write a Python program with tuple using for loop")
# t1=(1,2),(3,4),(5,6)
# print(type(t1))
# #Approach 1
# for x in t1:
#     print(x)
#
# #Approach 2
# for x,y in t1:
#     print(x," ",y)

# print("******************Program 19*************")
# print("Write a Python program using while loop")
# i=1
# while i<=5:
#     print("QACircle Training Academy")
#     i=i+1
#
# print("******************Program 20*************")
# print("Write a Python program using while loop")
# count=0
# while count<3:
#     print(count)
#     count=count+1
#
# print("******************Program 21*************")
# print("Write a Python program with list using while loop")
# count=0
# while count<3:
#     print(count)
#     count=count+1

# print("******************Program 22*************")
# print("Write a Python program to print sum of first n numbers using while loop")
# num=int(input("Enter the number"))
# sum=0
# i=1
# while i<=num:
#     sum=sum+i
#     i=i+1
#
# print("The sum of first ",num, "numbers is =",sum)

# print("******************Program 23*************")
# print("Write a Python program to prompt the user to enter some name until confirmation using while loop")
# #Approach 1
# name=""
# while name!="QACircle":
#     name=input("Enter the name")
# print("Thank you for the confirmation")
#
# #Infinite Loops
# while True:
#     print("Good Morning")

#Nested Loops
#Sometimes we can take loop inside another loop, which is also known as nested loop.
# print("******************Program 24*************")
# print("Write a Python program to display *'s in Right Angle Triangle form")
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*" ,end='')
#     print()

#print("******************Program 25*************")
#WAP using break statements
# for x in range(10):
#     if x==7:
#         print("Please stop printing 7 and above values")
#         break
#     print(x)
#
# print("******************Program 26*************")
# #WAP using break statements
# cart=[10,20,40,80,150,299,600,499,501]
# for item in cart:
#     if item>500:
#         print("Please stop placing the order if the product price is greater then 500")
#         break
#     print(item)


# print("******************Program 27*************")
# #WAP using Continue Statement
# cart=[10,20,40,80,150,299,600,499,501]
# for item in cart:
#     if item>500:
#         print("Please stop placing the order if the product price is greater then 500 ===:",item)
#         continue
#     print(item)
#
# print("******************Program 28*************")
# #WAP using Continue Statement
# number=[10,20,30,0.0,40,50,0]
# for n in number:
#     if n==0:
#         print("Hey we can't divide with zero..just skipping it")
#         continue
#     print(n)
#     print("100/{} = {}".format(n,100/n))


# print("******************Program 29*************")
cart=[10,20,40,80,150,299,499,500]
# for item in cart:
#     if item>500:
#         print("Please stop placing the order if the product price is greater then 500 ===:",item)
#         break
#     print(item)
# else:
#     print("Congratulations you have successfully placed all the items order")

#Ex1
for i in cart:
    pass

#Ex2
def m1():
    pass

#Ex3
if True:pass

#Ex4
# x=400
# for i in range(1,100):
#     if i%9==0:
#         print(i,x)
#     else:
#         pass
#
# del x



# #None Statement
# s1="QACircle"
# print(s1)
# s1=None
# print(s1)
#
#
# #del Statement
# s="QACircle"
# del s  #==>Valid
# print(s)  #===>We get an error
# print(s[0]) #===> We get an error


#Creation of a list
#1 We can create empty list objects as follows
# l = []
# print(l)

#2 Create a list with dynamic inputs
# l1=eval(input("Enter the list"))
# print(l1)
# print(type(l1))

#3 Create list with list() function
# l2=list(range(0,20,2))
# print(l2)
#
# s="QACircle"
# l3=list(s)
# print(l3)
#
# s4=set(l3)
# print(s4)
#
# #4 split() function
# s1="Learning Python is very very easy !!!"
# l4=s1.split()
# print(l4)
#
# l5=s.split()
# print(l5)
#
# #Nested list ==>list inside another list we call it has nested list
# l6=[100,200,300,[120,420,520]]
# print(l6)
# print(l6[3][0])

#How to access the list
# 1====> By indexing

# 2 ====> By using slice operator
"""
Syntax ===> list2 = list1[start:stop:step]

start ===> It indicates that index where slice has to start ===> default value is 0
stop  ===> It indicates that index where slice has to end ===>Default value is max allowed 
           index of the list i.e, length of the list
step  ===>Increment Value ===> default is 1 
"""
# l=[1,2,3,4,5,6,8,120,700,540,465,10]
# print(len(l))
# print(l[:4]) # 0 to 3 index it has printed the O/P ==> end -1 ==> 4-1==>3
# print(l[4:])
# print(l[8:10])
# print(l[0:11:2])
# print(l[0:11:1])
# print(l[1:11:1])
# print(l[-4:])
# print(l[:-4])
# print(l[:-41])
# print(l[-41])

# print("******************Program 30*************")
# #Using while and for loops for accessing the list
# #While Loop
# l=[1,2,3,4,5,6,8,120,700,540,465,10]
# i=0
# while i<len(l):
#     print(l[i])
#     i=i+1
#
# print("******************Program 31*************")
# #For Loop
# l=[1,2,3,4,5,6,8,120,700,540,465,10]
# for i in l:
#     print(i)
#
# print("******************Program 32*************")
# #reverse the list using for loop
# print(l[::-1])
#
# print("******************Program 33*************")
# #For Loop with reverse direction
# l=[1,2,3,4,5,6,8,120,700,540,465,10]
# for i in l[::-1]:
#     print(i)
#
# print("******************Program 34*************")
# #While Loop revers order
# l=[1,2,3,4,5,6,8,120,700,540,465,10]
# i=-1
# while i>-len(l):
#     print(l[i])
#     i=i-1

# #To fetch the length of the list
# #1. len() ==> returns the number of elements present in the list
# l=[100,200,300,100]
# print(len(l))
#
# #2. count() ==>returns the number of occurrences of specified item in the list
# print(l.count(100))
#
# #3. index() ==>returns the index of first occurrence of specified item
# print(l.index(300))
# #print(l.index(10)) ===> Will get ValueError: 10 is not in list
#
# #4. List manipulation
# #4.1 append() function
# l.append("QACircle")
# print(l)
# l.append(250.0)
# print(l)

#print("******************Program 35*************")
#WAP to add all the elements to the list upto 100 which divisible by 10
# l2=[]
# for i in range(1,101):
#     if i%10==0:
#         l2.append(i)
# print(l2)
#
# print("******************Program 36*************")
# #WAP to print even numbers from the list
# l2=[]
# for i in range(1,101):
#     if i%2==0:
#         l2.append(i)
# print(l2)

#insert() function ==> we can insert the item at the specified index position
# l3=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print("Before Inserting ===>",l3)
# l3.insert(1,400)
# print("After Inserting ===>",l3)

#extend() function ==> We can add one list to the another list
# l1=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# l2=["Rajesh","Sushma","Suresh","Rohit","Mahesh"]
# print(l1)
# print(l2)
# l1.extend(l2)
# print(l1)

#remove() function ==>This function will remove the specified item from the list. if the item
#present multiple times then only first occurrence will be removed

# l1=[10,60, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(l1)
# l1.remove(60)
# print(l1)

"""
pop() function ==>
        1.it removes and returns the last element of the list
        2.This is the only function which manipulates the list and return some elements
"""
# l1=[10,60, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(l1)
# print(l1.pop())
# print(l1)
# print(l1.pop())
# print(l1)
# print(l1.pop())
# print(l1)
# print(l1.pop(3))

# #reverse() ==>We can use this to reverse the order of the elements
# l1=[10,60, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(l1)
# l1.reverse()
# print(l1)

# #sort() function  +> we use this function to sort the elements according
# # to default natural sorting order
# l1=[10,60, 20,100,1,21 ,30, 40, 50,33,15,11 ,60, 70, 80, 90, 100]
# print(l1)
# l1.sort()
# print(l1)
#
# s=["Dog","Banana","Cat","Apple","Animal"]
# print(s)
# s.sort()
# print(s)
# s.sort(reverse=True)
# print(s)
# s.sort(reverse=False)
# print(s)


# x=[10,20,30,40]
# y=x
# print(x)
# print(id(x))
# print(y)
# print(id(y))
#
# del x
# print(y)

# #slice Operator
# x = [10, 20, 30, 40]
# y=x[:]
# print(x)
# print(id(x))
# print(y)
# print(id(y))
# y[1]=1000
# print(y,"=========",x)
#
# #By using Copy() Function
# x = [100, 200, 300, 400]
# y=x.copy()
# print(x)
# print(id(x))
# print(y)
# print(id(y))
# x[1]=2000
# print(y,"=========",x)

# print("******************Program 37*************")
# #List concatenation
# a = [10, 20, 30, 40]
# b = [100, 200, 300, 400]
# c=a+b
# print(c)
# #c=a+[4000] ==> Valid
# #c=a+4000 ==> Invalid , Type Error ==> can only concatenate list (not int)
#
# print("******************Program 38*************")
# #list multiplication
# a = [10, 20, 30, 40]
# b = [100, 200, 300, 400]
# y=a*10
# print(y)

# print("******************Program 39*************")
# #List Comparison
# x=["Dog","Cat","Rat"]
# a=["Dog","Cat","Rat"]
# z=['DOG',"CAT","RAT"]
# print(x==a)
# print(x==z)
# print(x!=z)

# n=[10,20,30,40]
# print(100 in n)
# print(10 in n)
# print(400 not in n)
# print(n)
#
#
# #clear() function to remove all the elements from the list
# n.clear()
# print(n)
#
# print("******************Program 40*************")
# #Nested list
# l=[[10,20,30],[40,50,60],[70,80,90]]
# print(l)
# print(l[2][2])
# print("Elements in row wise")
# for r in l:
#     print(r)
#
# print("Elements by matrix style")
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j],end='  ')
#     print()


# print("******************Program 41*************")
# #list Comprehension
# l=[i*i for  i  in  range(1,11)]
# print(l)
#
# print("******************Program 42*************")
# #list Comprehension
# l=[i*4 for  i  in  range(1,10)]
# print(l)
#
# print("******************Program 43*************")
# #list Comprehension
# l=[i for  i  in  range(1,100) if i%2==0]
# print(l)
#
# print("******************Program 44*************")
# #list Comprehension
# words=["Sudeep","Yash","Shivanna","Ravichandra","Shankernag"]
# s=[w[0] for w in words]
# print(s)

#print("******************Program 45*************")
# #list Comprehension
# num1=[10,20,30,40]
# num2=[30,40,50,60]
#
# #I want to print numbers present in num1 list and not in num2 list ==> 10,20
# num3=[i for i in num1 if i not in num2]
# print(num3)
#
# #I want to print numbers present in num2 list and not in num1 list ==> 50,60
# num3=[i for i in num2 if i not in num1]
# print(num3)
#
# #I want to print numbers present in num2 and num1 list common objects ==> 30 , 40
# num3=[i for i in num2 if i in num1]
# print(num3)

# print("******************Program 46*************")
# #WAP to split the sting and get the length of each words and also convert each word in to upper case
# words="Learning python is very easy".split()
# print(words)
# l=[[w.upper(),len(w)] for w in words]
# print(l)
#
# print("******************Program 47*************")
# #WAP to split the sting and get the length of each word and also convert each word in to lower case
# words="LEARNING PYTHON IS VERY EASY".split()
# print(words)
# l=[[w.lower(),len(w)] for w in words]
# print(l)
#
# print("******************Program 48*************")
# #Write a program to display unique vowels present in a given word
# vowels=['a','e','i','o','u']
# name=input("Enter the name to search for vowels")
# found=[]
#
# for letter in name:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# print(found)
# print("The number of different vowels present in",words,"is",len(found),"===",found)

# #Create tuple
# t=10,20,30
# print(type(t))
#
# t1=()
# print(type(t1))
#
# t2=(10)
# print(type(t2))
#
# t3=(10,)
# print(type(t3))
#
# """ Which of the following are valid tuple
# 1. t=10,20,30,40  ==>Valid
# 2. t=20  ====> Invalid
# 3. t=100, ====>Valid
# 4. t=(1000)  ==>Invalid
# 5. t=(10,20,30,40)===>Valid
# """
#
# #using tuple() function
# l=[10,20,30,40]
# t=tuple(l)
# print(t)
#
# #Range
# t5=tuple(range(10,50,4))
# print(t5)
#
# #Accessing the tuple elements/objects {index, slice)
#
# #By using index
# t=(10,20,30,40,50,60)
# print(t[0])
# print(t[-4])
# print(t[-1])
# #print(t[100]) ==>IndexError: tuple index out of range
#
# #By using slice
# t=(10,20,30,40,50,60)
# print(t[2:5])
# print(t[::-1])
#
# #tuple is immutable we can't change the value
# #t[1]=200 ==>TypeError: 'tuple' object does not support item assignment
# print(t)
#
# #Mathematical Operation on tuple
# #Concatenation
# t1=(10,20,30)
# t2=(100,200,300)
# t3=t1+t2
# print(t3)
#
# #Multiplication
# t4=t1*10
# print(t4)
#
# #len() ==>returns the length of the tuple
# print(len(t4))
#
# #count() ==>Returns the number of occurrences of given element in tuple
# print(t4.count(20))
#
# #idex() ==>return the index of first occurrence of the given element
# print(t4.index(30))
# #print(t4.index(300)) ==>ValueError: tuple.index(x): x not in tuple
#
# #sorted()
# t=(20,10,40,1,23,800,50,600)
# t1=sorted(t)
# print(t)
# print(t1)
# t1=sorted(t,reverse=True)
# print(t1)
#
#
# #min() , max() function ==> Minimum and maximummvalues it will return based on sorting order
# print(min(t))
# print(max(t))
#
# #tuple packing and unpacking
# #Packig===>creating a tuple by packing group of variables
# a=10
# b=20
# c=40
# d=50
# t=a,b,c,d
# print(t)
#
# #Unpacking==>reverse of packing , assigning tuple objects to individual variables
# t=10,20,40,50
# x,y,z,w=t
# print("x =",x,"y =",y,"z =",z,"w =",w)
#
# #Tuple comprehension is not possible in python
# t=(x*2 for x in range(1,6))
# #print(type(t)) ==> since we get generator O/P <class 'generator'>

# print("******************Program 49*************")
# #write a python program to take tuple from keyboard and print sum as well as average values
# t6=eval(input("Enter the tuple elements"))
# l=len(t6)
# sum_val=0
# for i in t6:
#     sum_val=sum_val+i
# print("The sum of values is =",sum_val)
# print("The Average value is =",sum_val/l)

# #Creating Set Objects :
# #Ex 1
# s={10,20,30,40,50}
# print(s)
# print(type(s))
#
# #Ex 2
# #s=set(any sequence)
# l=[10,20,30,40,50]
# s1=set(l)
# print(s1)
#
# #Ex 3
# s2=set(range(10,100,4))
# print(s2)
#
# #Important functions
# # 1. add(x) ==> Add and item to the set
# s={10,20,30}
# print(s)
# s.add(40)
# print(s)
#
# # 2. update(x,y,z)==>To add multiple items to the set ==>Arguments are not individual elements
# # and these are iterable Objects like List, range etc.
# #All the elements present in the given iterable objects will be added to the set.
# s3={100,300,400,500}
# l2=[1000,2000,3000]
# print(s3)
# s3.update(l2,range(5))
# print(s3)
#
# #What is the difference between add() and update() function ?
#
# #3. copy() function ==> return the copy of set . it is a cloned object
#
# s4={100,300,400,500}
# print(id(s4))
# s5=s4.copy()
# print(s5)
# print(id(s5))
#
# #4 pop() ==> Remove and return random element from the set
# s4={100,300,400,500}
# print(s4.pop())
# print(s4)
#
# #5 remove() ==> Remove the specified element from the set
# #If the specified element is not present in the set then we get Key Error
#
# s4={100,300,400,500}
# s4.remove(100)
# print(s4)
# #s4.remove(50) #KeyError: 50
#
# #5 discard(x) :  It removes the specified element from the set
# #If the specified element is not present in the set then we will not get Key Error
# s4={100,300,400,500}
# s4.discard(100)
# print(s4)
# s4.discard(50)
#
# #What is the difference between remove() and discard() function in the set() ?
# #What is the difference between pop(), remove(),discard() function from the set() ?
#
# # 6. Clear() ==> To remove all the elements from the set
# s={10,20,30,40}
# print(s)
# s.clear()
# print(s)
#
# #Mathematical Operations on the Set :
# #1. union()==> We can use this function to return all the elements present in both the set
# x={10,20,30,40,50}
# y={30,40,50,60,70}
#
# #x.union(y) OR x|y
# print(x.union(y))
# print(x|y)
#
#
#
# #2. intersection() ==> Return the common elements present in both x & Y
# x={10,20,30,40,50}
# y={30,40,50,60,70}
# print(x.intersection(y))
# print(x&y)
#
# #3. difference() ==>x.difference(y) OR x-y
# print(x.difference(y))
# print(x-y)
# print(y.difference(x))
#
# #4. symmetric_difference()  ==> it is going to return the elements either in x or y not in both
# # x.symmetric_difference(y)  OR x^y
# x={10,20,30,40,50}
# y={30,40,50,60,70}
# print(x.symmetric_difference(y))

#Membership Operator : in , not in
# s=set("QACircle")
# print(s)
# print("B" in s)
# print("Q" in s)
# print("G" not in s)
# print("e" not in s)

# #Set Comprehension : It is possible
# print("******************Program 50*************")
# #Write a program to get square of a numbers?
# s={x*x for x in range(1,11)}
# print(s)
#
# print("******************Program 51*************")
# #Write a program to multiply 4 with each number from the given set?
# x={10,20,30,40,50}
#
# s1={4*i for i in x}
# print(s1)
#
# print("******************Program 52*************")
# #Write a program to get the power of 4 the value from each number from the given set?
# x={10,20,30,40,50}
#
# s1={i**4 for i in x}
# print(s1)
#
# print("******************Program 53*************")
# #Write a program to eliminate duplicates from the list
# #Approach 1
# l=[10,1,10,1,20,20,30,40,20,30,2,2,3,4,5,3,4,5,1,3,1,4,2,3,5]
# s=set(l)
# print(s)
#
# #Approach 2
# l=[10,1,10,1,20,20,30,40,20,30,2,2,3,4,5,3,4,5,1,3,1,4,2,3,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
#
# print("******************Program 54*************")
# #Write a program to print different Vowels present in the given word :
# w="qacircle"
# s=set(w)
# v={'a','e','i','o','u'}
# d=s.intersection(v)
# print("The different vowels present in the given word",w," are",d)

#How to Create Dictionary:
# Ex 1
#d={} #==> Creates an empty dictionary
# d1=dict() #==> Creates an empty dictionary
#
# #We can add key-value pairs based on our requirements
# print(d,"    ",id(d),"    ",type(d))
# print(d1,"    ",id(d1),"    ",type(d1))
#
# d[100]="QACircle"
# d[200]="Training"
# d[300]="BG"
# print(d)
# d[100]="Welcome"
# print(d)
#
# #d1={"Key":"value","Key":"Value"}
# d1={100:"QACircle",100:"Welcome"}
# print(d1)
#
# #How to update dictionary
# #d[key]=value
# d[100]="QACircle"
# d[200]="Training"
# d[300]="BG"
# print(d)
# d[100]="Welcome"
# print(d)
#
# #How to delete the particular element from the dictionary
# #del d[key] ===> It deletes the entry associated with specified key
#                 # if the key is not available then we will get key error
#
# print(d)
# del d[200]
# print(d)
#
# #Clear() ==> Remove all the elements from the dictionary
# d.clear()
# print(d)
#
# #del d # here we are deleting total dictionary. we can't access after deleting
# print(d)
#
# #len() ==> Returns the number of items present in the dictionary
# print(len(d))
# #get() ===> returns the value associated with key
# d[100]="QACircle"
# d[200]="Training"
# d[300]="BG"
# print(d)
# print(d.get(300))
#
# #pop(key) ==> it removes the entry associated with specified key and returns the corresponding value
#
# #if the specified key is not available then we get key error.
# print(d)
# print(d.pop(100))
# print(d)
#
# #popitem() ==>
# #it removes both key and value (Arbitrary) from the dictionary and returns it.
# d={10:"Ravi",20:"Shiva","Hello":"QACircle"}
# print(d)
# print(d.popitem())
# print(d.popitem())
# print(d.popitem())
# #print(d.popitem())
#
# #keys()
# #it returns all the keys associated with dictionary
# d={10:"Ravi",20:"Shiva","Hello":"QACircle"}
# print(d.keys())
# for i in d.keys():
#     print(i)
#
# #values()
# #it returns all the values associated with dictionary
# d={10:"Ravi",20:"Shiva","Hello":"QACircle"}
# print(d.values())
# for i in d.values():
#     print(i)
#
# #items() ==> It returns the list of tuple elements in the form key-value pairs
# #[(k,v),(k,v),(k,v)]
# d={10:"Ravi",20:"Shiva","Hello":"QACircle"}
# for x,y in d.items():
#     print(x," === ",y)
#
# """
# 10 === Ravi
# 20 === Shiva
# Hello === QACircle """
#
# #copy() ==> d.copy() ==> To create cloned copy
#
# #setdefault()
# d={10:"Ravi",20:"Shiva","Hello":"QACircle"}
# print(d.setdefault(10,"pavan"))
# print(d)
# print(d.setdefault(400,"Arun"))
# print(d)
#
# #dictionary comprehension is possible
# squares={x:x*x for x in range(1,6)}
# print(squares)
# doubles={x:x*2 for x in range(1,6)}
# print(doubles)
#
# print("******************Program 55*************")
# #write a program to take dictionary from the keyboard and print the sum of values
# # d=eval(input("Please enter the dictionary"))
# # print(d)
# # print(sum(d.values()))
#
# print("******************Program 56*************")
# #Write a program to find the number of occurrence of each letter present in the given string
# word=input("Enter the word :")
# d={}
# for x in word:
#     #print(x)
#     d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print(k,":",v)
#
# print("******************Program 57*************")
# #Write a program to find the number of occurrence of each vowel present in the given string
# word=input("Enter the word :")
# vowels={'a','e','i','o','u'}
# d={}
#
# for x in word:
#     if x in vowels:
#         d[x]=d.get(x,0)+1
#
# for k,v in d.items():
#     print(k,":",v)
#
# # for k,v in sorted(d.items()):
# #     print(k,":",v)
#
# print("******************Program 58*************")
# #Write a program to find the number of occurrence of each vowel present in the given string in ascending order
# word=input("Enter the word :")
# vowels={'a','e','i','o','u'}
# d={}
#
# for x in word:
#     if x in vowels:
#         d[x]=d.get(x,0)+1
#
# for k,v in sorted(d.items()):
#     print(k,":",v)

#String multiline with symbols
#s='This is a' single quote symbol' ==>Invalid

# s='This is a \' single quote symbol' #==>Valid
# print(s)
#
# s='This is a \" double quote symbol' #==>Valid
# print(s)
#
# s="The 'Python Notes' by 'QACircle' is very helpful" #==>Valid
# print(s)
#
# #s="The "Python Notes" by "QACircle" is very helpful" #==>In-Valid
# print(s)
#
# s="The \"Python Notes\" by \"QACircle\" is very helpful" #==>Valid
# print(s)
#
# print(len(s))

# print("******************Program 59*************")
# #Write a program to access each character of String in backword and forward direction by using loops
# #Approach 1 ==>Using While Loop
# s="Learning Python is very easy !!!"
# n=len(s)
# i=0
# print("Forward Direction")
# while i<n:
#     print(s[i], end='')
#     i=i+1
# print()
# print("Backward Direction")
# i=-1
# while i>=-n:
#     print(s[i], end='')
#     i=i-1
# print()
# #Approach 2 ==>Using for Loop
# s="Learning Python is very easy !!!"
# print("Forward Direction")
# for i in s:
#     print(i, end='')
#
# print()
# s="Learning Python is very easy !!!"
# print("Backward Direction")
# for i in s[::-1]:
#     print(i, end='')
# print()

# #Checking Membership of a sub string
# s="Learning Python is very easy !!!"
# sub="Python"
# print(sub in s)
# print(sub not in s)
#
# #Comparison of String
# s1=input("Enter the first String")
# s2=input("Enter the Second String")
#
# if s1==s2:
#     print("Both Strings are equal")
# elif s1<s2:
#     print("First String is Less than second String")
# else:
#     print("First String is greater than second String")

#Removing of Space
#rstrip() ==> Remove the spaces in the right hand side
#lstrip() ==>Remove the space in the left hand side
#strip() ==> To remove spaces both the side

# scity=input("Enter your  city name")
# city=scity.strip()
# if city=="Hyderabad":
#     print("Hello Hyderabadi ")
# elif city=="Chennai":
#     print("Hello Madrasi")
# elif city =="Bangalore":
#     print("Hello Kannadiga")
# else:
#     print("You have entered invalid city")

#find() ==>s.find(substring)
# #Returns the index of first occurrence of the given substring. if it is not available then we will get -1
# s="Learning Python is very easy !!!"
# print(s.find("Python"))
# print(s.find("JAVA"))
#
# #find() ==>s.find(substring,begin,end)
# s="Learning Python is very easy !!!"
# print(s.find("Python",9,30))
# print(s.find("Learn",5,30))
#
# #index() ==>index() method exactly same as find() method except that if the specified substring
# # is not available then we will value error
# s="Learning Python is very easy !!!"
# print(s.index("Python",9,30))
# print(s.index("Java")) ==>ValueError: substring not found

#print("******************Program 60*************")
# #Program 1
# #Write a Program to display all the positions of substring in a given string from the main string
# s="Learning Python is very easy !!!"
# sub="java"
# n=len(s)
# pos=-1
# flag=False
# while True:
#     pos=s.find(sub,pos+1,n)
#     if pos==-1:
#         break
#     print("Fond at position",pos)
#     flag=True
# if not flag:
# #if flag==False:
#     print("Sub string not found")
#
# #Program 2
# s="ababbdhabbbajdhbabbababbahhdbbabbababsjbbababababbababa"
# sub="a"
# n=len(s)
# pos=-1
# flag=False
# while True:
#     pos=s.find(sub,pos+1,n)
#     if pos==-1:
#         break
#     print("Fond at position",pos)
#     flag=True
# if not flag:
# #if flag==False:
#     print("Sub string not found")

#Counting the substring in the given string
#We can find the number of occurrence of substring in the main string by using count() method
#count(substring) ==> It will search through the string
#count(substring,begin,end) ==>It will search from begin index to end-1 index

# #cound(substring)
# s="ababbsbbhababdjhhaabababbbbbabbabbbbbaaaabbbabbabb"
# print(s.count("a"))
# print(s.count("aaaa"))
# print(s.count("bb"))
#
# #count(substring,begin,end)
# print(s.count("bb",2,10))

# print("******************Program 61*************")
# #Replacing a String with another String :
# #s.replace(Old String,new String)
# s1="Learning Python is very easy !!!"
# print(s1)
# print(id(s1))
# s2=s1.replace("easy","Difficult")
# print(s2)
# print(id(s2))

# print("******************Program 62*************")
# """
# We can split the string according to the specified seperator by using split() method.
# l=s.split()
#
# The default separator is space. The return type of split() method is list
# """
# s="QACircle Technologies"
# l=s.split()
# print(l)
#
# print("******************Program 63*************")
# #Joining of a string
# #We can join a group of strings (list or tuple) wrt the given seperator.
# #s1=seperator.join(group of strings)
# #Ex 1
# t=("Sunny","Hello","Good Morning", "Bad Morning")
# s=":".join(t)
# print(s)
# s="==".join(t)
# print(s)
# s=" ".join(t)
# print(s)

# #Changing the Cases of a String :
# """
# We can change case of a string by using following methods
# upper() ==>To concert all char to upper case
# lower() ==>To concert all char to lower case
# swapcase() ==>Convert all lower case characters to upper case and
# all upper case characters  to lower case.
# title() ==>To convert all char to title case.==>first char in every word
# should be upper case and all remaining characters should be lower case.
# capitalize() ==>Only the first char will be converted to upper case and all
# the remaining characters will be converted to lower case.
#
# """
# s="learning Python is Very Easy"
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())
#
# #Checking starting and ending part of string
# s="learning Python is Very Easy"
# print(s.startswith("learning"))
# print(s.endswith("easy"))
# print(s.endswith("easy"))
# print(s.endswith("Easy"))
#
# print("***********************************")
# #To check type of characters present in a given string :
# s=" "
# print(s.isspace())
# print("learningPythonisVeryEasy".isalpha())
# print("Learning Python Is Very Easy".isascii())
# print("QACircle123".isalnum())
# print("QACircle".istitle())
# print("Qacircle".istitle())
# print("qacircle".islower())
# print("qacircle".isupper())
# print("1234".isdigit())

# print("******************Program 64*************")
# #Demo program to get the required output :
# s=input("Enter any character")
# if s.isalnum():
#     print("Alpha Numeric Character")
#     if s.isalpha():
#         print("Alphabet Character")
#         if s.islower():
#             print("Lower Case Alphabet Character")
#         else:
#             print("Upper Case Alphabet Character")
#     else:
#         print("It is a digit")
# elif s.isspace():
#     print("It is a space character")
# else:
#     print("Non space SpecialCharacter")

#Formatting of a String
"""
We can format the string with variable values by using 
-replacement operator {} and format() method
"""
#Ex 1
# name="Arun"
# salary=10000.00
# age=48
#
# print("Hi {} your salary is {} and your age is {}".format(name,salary,age))
# #print("Hi {} your salary is {} and your age is {}".format(salary,age,name)) ==>In valid O/P
# print("Hi {x} your salary is {y} and your age is {z}".format(y=salary,z=age,x=name))

# print("******************Program 65*************")
# #Write a program to reverse the given string
# s="QACircle"   #O/P ==>"elcriCAQ"
# #Approach 1:
# print(s[::-1])
#
# #Approach 2:
# print("".join(reversed(s)))
#
# #Approach 3:
# i=len(s)-1
# target=''
# while i>=0:
#     target=target+s[i]
#     i=i-1
# print(target)

# print("******************Program 66*************")
# s1="Learning Python is Very Easy"  #O/P ==>Easy Very is Python Learning
# l=s1.split()
# print(l)
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# print(l1)
# l2=" ".join(l1)
# print(l2)

# print("******************Program 67*************")
# #Write a program to reverse the internal content of each word
# s1="QACircle Technologies"
# #O/P ==>elcriCAQ  seigolonhceT
# l=s1.split()
# print(l)
# l1=[]
# i=0
# while i<len(l):
#     l1.append(l[i][::-1])
#     i=i+1
# print(l1)

# print("******************Program 68*************")
# #Write a program to print the character present at odd position and even position:
# #1st Approach
# name = input("Enter the name")
# print("Character present at even position :",name[0::2])
# print("Character present at Odd position :",name[1::2])
#
# #2nd Approach
# i=0
# name = input("Enter the name")
# print("Character present at Even position")
# while i<len(name):
#     print(name[i],end='')
#     i=i+2
# print()
#
# i=1
# name = input("Enter the name")
# print("Character present at Odd position")
# while i<len(name):
#     print(name[i],end='')
#     i=i+2
# print()

# print("******************Program 69*************")
# #Write a program to merge characters of 2 string into single string by taking characters alternatively
# s1="QCrl Tcnlge"
# s2="Aice ehoois"
# output=""
# #O/P ==> QACircle Technologies
# i,j=0,0
# while i<len(s1) or j<len(s2):
#     if  i<len(s1):
#         output=output+s1[i]
#         i=i+1
#     if j<len(s2):
#         output = output + s2[j]
#         j=j+1
# print(output)

# print("******************Program 70*************")
# """
# Write a program to sort the characters of a string and first alphabet symbols
# - followed by numeric value
# input="B4A1HN234"
# output="ABHN12344"
# """
# s1=s2=output=""
# input1="B4A1HN234"
# for x in input1:
#     if x.isalpha():
#         s1=s1+x
#     else:
#         s2=s2+x
# print(s1,"=====",s2)
# for x in sorted(s1):
#     output=output+x
# for x in sorted(s2):
#     output=output+x
# print(output)

# print("******************Program 71*************")
# """
# s=a4b3c2
# O/P ==>aaaaabbbbccc
# """
# x=input("Enter some String")
# output=""
# for i in x:
#     if i.isalpha():
#         output=output+i
#         previous=i
#     else:
#         output=output+previous*(int(i))
# print(output)

# print("******************Program 72*************")
# #Write a program to remove duplicate characters from the given string
# #Approach 1
# s="ABCDABABACADABACADABADACBDBDCABCDAADCBEFBACDFE"
# print(s)
# #O/P ==> ABCDEF
# s1=set(s)
# s2=sorted(s1)
# output="".join(s2)
# print(output)
#
# #Approach 2
# s="ABCDABABACADABACADABADACBDBDCABCDAADCBEFBACDFE"
# l=[]
# for i in s:
#     if i not in l:
#         l.append(i)
# print(l)
# l1=sorted(l)
# output="".join(l1)
# print(output)

#print("******************Program 73*************")
#Write a Python program to find the number of occurrence of each character present
#===>in the given string
# def removeduplicate():
#         s="ABCDABCDABCDABEDACDE"
#         d={}
#         for i in s:
#             if i in d.keys():
#                 d[i]=d[i]+1
#             else:
#                 d[i]=1
#         print(d)
#         for k,v in d.items():
#             print(k," Occurred ",v," times ")
#
# removeduplicate()

# def wish(name):
#     print("Hello",name," Good Morning")
#
# wish("QACircle")
# wish("Arshita")
# wish("Nanda")

# print("******************Program 74*************")
# #Write a python program to get square of number using function
# def squareofnum(number):
#     """ I am performing multiplication"""
#     print("The square of number",number,"is",number*number)
#
# squareofnum(5)
# squareofnum(1000)

# def add(x,y):
#     return x+y
#
# result=add(100,200)
# print("The sum is =",result)
# print("The sum is =",add(1000,2000))

# def f1():
#     print("Hello")
#
# f1()
# print(f1())

# print("******************Program 75*************")
# #Write a program to find a factorial of a number ===> 6 ==> 6*5*4*3*2*1 =>720
#
# num=eval(input("Enter the number"))
# result=1
# while num>=1:
#     result=result*num
#     num=num-1
# print("The Factorial of given number is ",result)
#
# print("******************Program 76*************")
# #Write a program to find a factorial of a number using function ===> 6 ==> 6*5*4*3*2*1 =>720
#
# def fact(num):
#     result = 1
#     while num >= 1:
#         result = result * num
#         num = num - 1
#     return result
#
# print("The Factorial of given number is ",fact(5))

# print("******************Program 77*************")
# """
# Write a program to return multiple values from a function:
# ===>In other Programming Language like C , C++ and Java , function can return
#     atmost one value.but in python, a function can return any number of values
# """
# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
# x,y=sum_sub(100,50)
# print("The sum is ",x)
# print("The Subtraction is :",y)
#
# print("******************Program 78*************")
# #Write a program to return multiple values from a function:
# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a-b
#     return sum,sub,mul,div
# t=calc(1000,500)
# print(t)
# print("The Results are ")
# for i in t:
#     print(i)

# def wish(name,msg):
#     print("Hello",name,msg)
#
# wish(name="Basavanagouda",msg="Good Morning")  #==>Valid
# wish(msg="Good Morning",name="Basavanagouda")  #==>Valid
# wish("Basavanagouda",msg="Good Morning")
# #wish(msg="Good Morning","Basavanagouda") #Invalid we will get Syntax Error

# def wish(name="Guest"): #Default name
#     print("Hello",name,"Bad Morning")
#
# wish()
# wish("QACircle")
#
# def wish(name="Guest",msg="Good Morning"):
#     pass
#
# wish()
#
# def wish(name,msg="Good Morning"):
#     pass
# wish("QAC")
#
# def wish(name="Guest",msg): #SyntaxError: parameter without a default follows parameter with a default
#     pass

# def addition(*n):
#     total=0
#     for i in n:
#         total=total+i
#     print("The sum is=",total)
#
# addition()
# addition(10)
# addition(10,20)
# addition(10,20,30,40,50)
# addition(100,200,300,400,500,600)
#
#
# #We can pass mix variable length arguments with positional arguments
# def f1(x,*n):
#     print(x)
#     for s1 in n:
#         print(s1,end=' ')
#
#
# f1(10)
# f1(10,20,30,40)
# f1(10,"A",20,30,40,"B")

# print("******************Program 79*************")
# #Write a program with keyword variable length arguments
# def display(**kwargs):
#     for k,v in kwargs.items():
#         print(k,"==",v)
#
#
# display()
# display(n1=10,n2=200,n3=400)
# display(Rno=1000,name="Sushma",marks=34,subject="Python")

# def  f1(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)
#
# #f1() ==> Error ==> Syntax Error
# f1(10,20)
# f1(25,50,arg4=100)
# f1(arg4=2,arg1=3,arg2=4)
#f1(4,5,arg2=6)  #TypeError: f1() got multiple values for argument 'arg2'

#Global Variables
# a=10 #Global Variable
# def f1():
#     print(a)
#     global b
#     b=100
#     print(b)
#
# def f2():
#     print(a)
#     b=1000
#     print(b) #Error we can't access it
#
# f1()
# f2()

# print("******************Program 81*************")
# #Can we replace global variable value inside a function when both are having same name
# a=120 #Global Variable
# x=100
# def f1():
#     a=777 #Local Variable
#     print(a)
#     a=500
#     print(x)
#     globals()['a']=100
#     print(globals()['a'])
#     print(a)
#
# f1()
# print(a)

# print("******************Program 82*************")
# #Write a python program to find the factorial of number using recursive function
# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result
#
# print("The factorial of number 4 is",factorial(4))
# print("The factorial of number 6 is",factorial(6))

# print("******************Program 83*************")
# #WAP to create a lambda function to find the square of a given number
# s=lambda  n: n*n
# print("The Square of 4 is ", s(4))
# print("The Square of 12 is ", s(12))
#
# print("******************Program 84*************")
# #WAP to create a lambda function to find the sum of 2 given numbers
# s=lambda  a,b: a+b
# print("The Sum of 10,20 is ", s(10,20))
# print("The Sum of 100,200 is ", s(100,200))
#
# print("******************Program 85*************")
# #WAP to create a lambda function to find biggest value from the given number (2 Numbers)
# s=lambda  a,b: a if a>b else b
# print("The biggest of 10,20 is ", s(10,20))
# print("The biggest of 100,200 is ", s(100,200))
#
# print("******************Program 86*************")
# #WAP to create a lambda function to find biggest value from the given number (3 Numbers)
# s=lambda  a,b,c: a if a>b and a>c else b if b>c else c
# print("The biggest of 10,20,30 is ", s(10,20,30))
# print("The biggest of 100,200,400 is ", s(100,200,400))

# print("******************Program 87*************")
# #WAP to filter only even numbers from the list by using filter() function?
# #Without lambda function
# l=[0,1,2,3,4,5,11,12,13,14,15,16,25,38,39]
#
# def iseven(x):
#     if x%2==0:
#         return True
#     else:
#         return False
#
# l1=list(filter(iseven,l))
# print(l1)
#
# l2=(filter(iseven,l))
# print(l2)
# for i in l1:
#     print(i)
#
# #With lambda function
# l=[0,1,2,3,4,5,11,12,13,14,15,16,25,38,39]
# l3=list(filter(lambda i:i%2==0,l))
# print(l3)
#
# print("******************Program 88*************")
# #WAP to filter the vowels from the given sequence
#
# sequence=['b','a','s','g','e','e','d','s','p','r']
#
# def fun(variable):
#     letter=['a','e','i','o','u']
#     if variable in letter:
#         return True
#     else:
#         return False
#
# filtered=(filter(fun,sequence))
# print(filtered)
#
# print("The filtered values")
# for i in filtered:
#     print(i)
#
# print("******************Program 88*************")
# #Try with lambda function and get the output

# print("******************Program 89*************")
# #WAP to get double of numbers
# #Without using lambda
# l=[1,2,3,4,5]
#
# def double(x):
#     return 2*x
#
# l1=list(map(double,l))
# print(l1)
#
# #With using lambda
# l=[1,2,3,4,5]
# l2=list(map(lambda x:2*x,l))
# print(l2)
#
# print("******************Program 90*************")
# #WAP to get square of numbers
# l=[1,2,3,4,5]
#
# def square(x):
#     return x*x
#
# l1=list(map(square,l))
# print(l1)

#With using lambda
# l=[1,2,3,4,5]
# l2=list(map(lambda x:x*x,l))
# print(l2)

#print("******************Program 91*************")
#WAP to multiply 2 list elements and get new list of values using map and lambda
# l1=[1,2,3,4]
# l2=[2,3,4,5]
# l3=list(map(lambda x,y:x*y,l1,l2))
# print(l3)

# print("******************Program 92*************")
# #Write a program using reduce function to get the sum of Values
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x+y,l)
# print(result)
#
# print("******************Program 93*************")
# #Write a program using reduce function to get the product of Values
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x*y,l)
# print(result)

# def wish(name):
#     print("Hello",name,"Good Morning")
#
# wish("QACircle")
# print(id(wish))
# print(wish)
# print("***************")
#
# greeting=wish #Aliasing
#
# greeting("QACircle")
# print(id(greeting))
# print(greeting)

# def outer():
#     print("Outer function started execution")
#     def inner():
#         print("Inner function started execution")
#     print("Outer function is calling inner function")
#     inner()
# outer()
# print("*************************************")
# #Note : A function can return another function
# def outer():
#     print("Outer function started execution")
#     def inner():
#         print("Inner function started execution")
#     print("Outer function is calling inner function")
#     return inner
#
#
# f1=outer()
#
# f1()
# f1()
# f1()
# print("*************************************")
# f2=outer
# f2()
#
# class Test:
#     pass
#
# t=Test()

# #using module name importing the members of one module to another module
# import qacircle
# print(qacircle.x)
# qacircle.add(100,200)
# qacircle.product(200,400)
# print(qacircle.h.y)
# qacircle.h.f1()
#
# # Without using module name import the members
# from qacircle import *
# product(100,100)
# add(100,100)
# print(x)
# print(h.y)
# h.f1()
#
# # Without using module name import the particular member
# from qacircle import product
# product(100,200)
#
# import qacircle
# qacircle.info()

# from random import *
# for i in range(10):
#     print(random())


# from random import *
# for i in range(10):
#     print(randint(1,100))

# from random import *
# for i in range(5):
#     print(randrange(1,11,2))

#randrange(10)==> generate 0 to 9 random numbers
# randrange(1,10) ⇒generates random numbers between 1 to 9
# randrange(1,11,2) ⇒generate numbers 1,3,5,7,9
# l=["Sushma","Rohit","Suresh","Nanad","Arun","Kishore","Mahesh","Aparna","Dhruti"]
# print(len(l))
# from random import *
# for i in range(5):
#     print(choice(l))

# import Tests.Test1
# import Tests.Test2
# import Tests.Automation.Auto1
# import Tests.Automation.Auto2
# import Tests.Automation.Test1

# print("******************Program 94*************")
# """
# #Write a program to print 10 stars in single line shown below
# **********
#
# """
# #Approach 1
# for i in range(10):
#     print("*",end='')
#
# print()
# #Approach 2
# print("*"*10)

# print("******************Program 95*************")
# """ Write a python program to print below pattern
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
#
# """
# n=int(input("Enter the number of rows"))
# for i in range(n):
#     print("*"*n)

# print("******************Program 96*************")
# """ Write a python program to print below pattern
# 1111111111
# 2222222222
# 3333333333
# 4444444444
# 5555555555
# 6666666666
# 7777777777
# 8888888888
# 9999999999
# 10101010101010101010
# """
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end='')
#     print()

# print("******************Program 97*************")
# """ Write a python program to print below pattern
# 12345678910
# 12345678910
# 12345678910
# 12345678910
# 12345678910
# 12345678910
# 12345678910
# 12345678910
# 12345678910
# 12345678910
# """
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end='')
#     print()

# print("******************Program 98*************")
# """ Write a python program to print below pattern
# AAAAAAAAAA
# BBBBBBBBBB
# CCCCCCCCCC
# DDDDDDDDDD
# EEEEEEEEEE
# FFFFFFFFFF
# GGGGGGGGGG
# HHHHHHHHHH
# IIIIIIIIII
# JJJJJJJJJJ
# """
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end='')
#     print()

# print("******************Program 99*************")
# """ Write a python program to print below pattern
# ABCDEFGHIJ
# ABCDEFGHIJ
# ABCDEFGHIJ
# ABCDEFGHIJ
# ABCDEFGHIJ
# ABCDEFGHIJ
# ABCDEFGHIJ
# ABCDEFGHIJ
# ABCDEFGHIJ
# ABCDEFGHIJ
# """
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+j),end='')
#     print()


# print("******************Program 100*************")
# """ Write a python program to print below pattern
# 10101010101010101010
# 9999999999
# 8888888888
# 7777777777
# 6666666666
# 5555555555
# 4444444444
# 3333333333
# 2222222222
# 1111111111
# """
#
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end='')
#     print()

# print("******************Program 101*************")
# """ Write a python program to print below pattern
# 10987654321
# 10987654321
# 10987654321
# 10987654321
# 10987654321
# 10987654321
# 10987654321
# 10987654321
# 10987654321
# 10987654321
# """
#
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-j,end='')
#     print()

# print("******************Program 102*************")
# """ Write a python program to print below pattern
# JJJJJJJJJJ
# IIIIIIIIII
# HHHHHHHHHH
# GGGGGGGGGG
# FFFFFFFFFF
# EEEEEEEEEE
# DDDDDDDDDDD
# CCCCCCCCCCC
# BBBBBBBBBBB
# AAAAAAAAAAA
# """
#
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(65+n-i),end='')
#     print()

# print("******************Program 103*************")
# """ Write a python program to print below pattern
# JIHGFEDCBA
# JIHGFEDCBA
# JIHGFEDCBA
# JIHGFEDCBA
# JIHGFEDCBA
# JIHGFEDCBA
# JIHGFEDCBA
# JIHGFEDCBA
# JIHGFEDCBA
# JIHGFEDCBA
# """
#
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(65+n-j),end='')
#     print()

# print("******************Program 104*************")
# """ Write a python program to print below pattern
# *
# **
# ****
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# """
#
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()

# print("******************Program 105*************")
# #WAP to print given number is even or Odd
# x=101
# if x%2==0:
#     print(x,"is a Even Number")
# else:
#     print(x,"is a Odd Number")

# print("******************Program 106*************")
# #WAP to find given number is positive or Negative
# #Approach 1
# x=10
# if x>=0:
#     print("Given number is Positive")
# else:
#     print("Given number is Negative")
#
# #Approach 2
# x=-10
# if x>0:
#     print("Given number is Positive")
#
# elif x==0:
#     print("Zero")
#
# else:
#     print("Given number is Negative")
#
# #Approach 3 Nested If condition
# num=float(input("Enter the number"))
# if num>=0:
#     if num>0:
#         print("Positive Number")
#     else:
#         print("Zero")
# else:
#     print("Negative Number")

# print("******************Program 107*************")
# #WAP to find given number is prime or not
# """
# A prime number is a special kind of whole number that’s greater than 1 and
# has exactly two distinct positive divisors: 1 and itself. In simpler terms,
# it's a number that can’t be evenly divided by anything other than 1 and itself.
#
# Examples of Prime Numbers
# 2 (the only even prime!)
# 3
# 5
# 7
# 11
# 13
# """
# #Case 1
# num=13
# if num>1:
#     for i in range(2,num):
#         if (num%i)==0:
#             print(num,"Is not a prime number")
#             break
#
#     print(num,"Is a prime Number")
# else:
#     print(num,"Is not a prime Number")
#
# #Case 2
# num=11
# if num>1:
#     for i in range(2, num//2):
#         if (num % i) == 0:
#             print(num, "Is not a prime number")
#             break
#
#     print(num, "Is a prime Number")
# else:
#     print(num, "Is not a prime Number")
#
# #Case 3
# n=17
# flag=False
# if n>1:
#     for i in range(2,n):
#         if (n%i)==0:
#             flag=True
#             break
#
#
# if flag:
#     print(n,"Is not a prime number")
# else:
#     print(n,"Is a Prime Number")

print("******************Program 108*************")
#WAP to find given number is Armstrong or not ?
""""

abcd...=an+bn+cn+dn+.......
153 ==> 1*1*1 + 5*5*5 + 3*3*3 =1+125+27 =>153 (Armstrong Number)
121 ===> 1*1*1 +2*2*2 + 1*1*1 = 1+8+1 =10 (Not Armstrong Number)

0,1,153,371,370,407

"""
num=int(input("Enter the number"))
temp=num
sum=0

while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp//=10 #temp=temp//10

#Display the result
if num==sum:
    print("Given number is armstrong number")
else:
    print("Given number is not a armstrong number")



