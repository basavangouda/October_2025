from abc import abstractmethod


# class Student:
#     """This is a student class with required date"""
#     x=10
#     y=20
#
#     def m1(self):
#         print("Hello")
#
# print(Student.__doc__)
# print(Student)
# help(Student)

# class Student:
#     """Developed by QACircle Basava for python demo"""
#     def __init__(self):
#         self.name="Basava"
#         self.age=31
#         self.marks=34
#
#     def talk(self):
#         print("Hello I AM",self.name)
#         print("My age is",self.age)
#         print("My marks are",self.marks)
#
# s=Student()
# s.talk()
# print(s.marks)
# print(s.age)
# print(s.name)

# class Student:
#     """Developed by QACircle Basava for python demo"""
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#
#     def m1(self):
#         print("Hello")
#
#     def talk(self):
#         self.m1()
#         print("Hello I AM",self.name)
#         print("My age is",self.age)
#         print("My marks are",self.marks)
#
# s=Student("Sushma",35,90)
# s.talk()

# class Test:
#
#     def __init__(self):
#         print(" Constructor Execution")
#         self.x=100
#
#     def m1(self):
#         print(self.x)
#         print("Method Execution")
#
# t=Test()
# t.m1()
# t.x=1000
# t.m1()
# t1=Test()
# t1.m1()
#
# t2=Test()
# t2.m1()

# class Student:
#     """Developed by QACircle Basava for python demo"""
#     def __init__(self,x,y,z):
#         self.name=x
#         self.roll_num=y
#         self.marks=z
#
#
#     def display(self):
#         print("Student Name:{} \n Roll_num :{} \n Marks:{}".format(self.name,self.roll_num,self.marks))
#         self.a=100
#
# s1=Student("Suresh",121,55)
# s1.display()
# s1.display()
# s1.display()
# s1.display()
#
# s2=Student("Rohit",420,86)

# class Employee:
#     def __init__(self):
#         self.eno=120
#         self.ename="BG"
#         self.esal=10000
#         #del self.eno
#
#     def m1(self):
#         print(self.eno)
#         print(self.ename)
#         print(self.esal)
#         self.jobrole="QA Engineer"
#         #del self.ename
#
# e=Employee()
# e.hike="Still in Progress"
# e.m1()
# #del e.hike
# print(e.hike)
# print(e.jobrole)
# print(e.ename)
#
# class Test:
#     #Static Variable
#     a=10
#
#     def __init__(self):
#         #Static Variable
#         Test.b=20
#         print(self.a)
#         print(Test.a)
#
#         #Instance Variable
#         self.x=400
#
#     def m1(self):
#         #Static Variable
#         Test.c=30
#         print(self.a)
#         print(Test.a)
#         print(Test.b)
#         print(self.b)
#
#     @classmethod
#     def m2(cls):
#         # Static Variable
#         cls.d=40
#         Test.e=50
#         print(cls.a)
#         print(Test.a)
#
#     @staticmethod
#     def m3():
#         Test.f=60
#         print(Test.a)
#
# t=Test()
# print(Test.a)
# print(t.a)
# t.m1()
# Test.m2()
# Test.m3()

# class Test:
#     a=777
#     @classmethod
#     def m1(cls):
#         print(cls.a)
#         cls.a=888
#
#     @staticmethod
#     def m2():
#         print(Test.a)
#         Test.a=999
#         print(Test.a)
#
#
# print(Test.a)
# Test.m1()
# Test.m2()
# Test.a=1000
# print(Test.a)

# class Test:
#     a=10
#     def m1(self):
#         self.a=999
#         del Test.a
#
# t=Test()
# t.m1()
# #print(Test.a)   #AttributeError: type object 'Test' has no attribute 'a'
# print(t.a)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def display(self):
#         print("Hi",self.name)
#         print("Your Marks are",self.marks)
#
#     def grade(self):
#         if self.marks>=60:
#             print("You have got first class")
#         elif self.marks>=50:
#             print("You have got second class")
#         elif self.marks>=35:
#             print("You got Third class")
#         else:
#             print("You are Failed")
#
# n=int(input("Enter the Number of Students"))
# for i in range(n):
#     name=input("Enter the studenet name")
#     marks=int(input("Enter the marks"))
#     s=Student(name,marks)
#     s.display()
#     s.grade()
#     print()


# class Student:
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def setMarks(self, marks):
#         self.marks = marks
#
#     def getMarks(self):
#         return self.marks
#
#     def display(self):
#         print("Hi",self.name)
#         print("Your Marks are",self.marks)
#
# n=int(input("Enter the Number of Students"))
# for i in range(n):
#     s=Student()
#     name = input("Enter the student name")
#     s.setName(name)
#     marks=int(input("Enter the marks"))
#     s.setMarks(marks)
#
#     print("Hi",s.getName())
#     print("Your Marks is",s.getMarks())
#     print()
# class Animal:
#     legs=4
#     @classmethod
#     def walk(cls,name):
#         print("{} walks with {} legs".format(name,cls.legs))
#
# Animal.walk("Dog")
# Animal.walk("Cat")

# class Test:
#     count=0
#     def __init__(self):
#         Test.count=Test.count+1
#
#     @classmethod
#     def noOfObjects(cls):
#         print("The number of objects got created for this class is",cls.count)
#
# Test.noOfObjects()
# t=Test()
# Test.noOfObjects()
# t1=Test()
# t2=Test()
# t3=Test()
# t4=Test()
# Test.noOfObjects()

# class QACircleMath:
#
#     @staticmethod
#     def add(x,y):
#         print("The sum is",x+y)
#
#     @staticmethod
#     def product(x, y):
#         print("The Product is", x * y)
#
#     @staticmethod
#     def Average(x, y):
#         print("The Average is", (x+y)/2)
#
# QACircleMath.add(100,200)
# QACircleMath.product(100,200)
# QACircleMath.Average(100,200)

# class Employee:
#     def __init__(self,eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#
#     def display(self):
#         print("Employee Number:",self.eno)
#         print("Employee Name",self.ename)
#         print("Employee Salary",self.esal)
#
# class Test:
#     def modify(emp):
#         emp.esal=emp.esal+10000
#         emp.display()
#
#
# e=Employee(100,"Basava",10000)
# e.display()
# print("**************************")
# Test.modify(e)

#Demo Program1
# class Outer:
#
#     def __init__(self):
#         print("Outer class object creation")
#
#     class Inner:
#         def __init__(self):
#             print("Inner class object creation")
#         def m1(self):
#             print("Inner class Method")
#
# #case 1
# o=Outer()
# i=o.Inner()
# i.m1()
# print("**********************************************")
# #Case 2
# i=Outer().Inner()
# i.m1()
# print("**********************************************")
# #case 3
# Outer().Inner().m1()

#Demo 2
# class Person:
#     def __init__(self):
#         self.name="Mahesh"
#         self.db=self.DOB()
#
#     def display(self):
#         print("Name",self.name)
#
#     class DOB:
#         def __init__(self):
#             self.dd=10
#             self.mm=5
#             self.yyyy=1948
#
#         def display(self):
#             print("DOB={}/{}/{}".format(self.dd,self.mm,self.yyyy))
#
#
# p=Person()
# p.display()
# x=p.db
# x.display()

#Demo 3
# import gc
# print(gc.isenabled())
# class Human:
#
#     def __init__(self):
#         self.name="Sunny"
#         self.head=self.Head()
#         self.brain=self.Brain()
#
#
#     def dispay(self):
#         print("Hello my name is",self.name)
#
#     class Head:
#         def talk(self):
#             print("Talking")
#             self.x=100
#             print()
#     class Brain:
#         def think(self):
#             print("Thinking")
#
# gc.disable()
# h=Human()
# h.dispay()
# h.brain.think()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())

#Note: The job of destructor is not to destroy object and just perform clean up activity
# import gc
# gc.disable()
# gc.enable()
# import time
# class Test:
#     def __init__(self):
#         print("Object Creation")
#
#     def __del__(self):
#         print("Fulfilling the last wish and perform clean up activities")
#
#
# t1=Test()
# t1=None
# time.sleep(5)
# print("End the application")

#if the object does not contain any reference variable then only it is eligible for GC.
#If the reference count is zero then only object is eligible for GC

# import time
# class Test:
#     def __init__(self):
#         print("Constructor Execution")
#
#     def __del__(self):
#         print("Destructor Execution")
#
# t1=Test()
# t2=t1
# t3=t2
# print(id(t1),id(t2),id(t3))
# del t1
# print("Object is not yet destroyed after deleting t1")
# del t2
# time.sleep(5)
# print("Object is not yet destroyed after deleting t2")
# print("I am trying to delete last reference variable")
# del t3


# import time
# class Test:
#     def __init__(self):
#         print("Constructor Execution")
#
#     def __del__(self):
#         print("Destructor Execution")
#
# list=[Test(),Test(),Test()]
# print(list)
# del list
# time.sleep(5)
# print("End of the Application")

# import sys
# class Test:
#     pass
# t1=Test()
# t2=t1
# t3=t1
# print(sys.getrefcount(t1))
#
# #Note : For every object, Python internally maintains one default reference variable self

# class Engine:
#     a=10
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         print("Engine specific functionalities")
#
# class Car:
#     def __init__(self):
#         self.engine=Engine()
#
#     def m2(self):
#         print(self.engine.a)
#         print(self.engine.b)
#         self.engine.m1()
#
#
# c=Car()
# c.m2()

# class P:
#     a=10
#     def __init__(self):
#         self.b=10
#         print("Hello")
#
#     def m1(self):
#         print("This is a parent  method")
#
#     @classmethod
#     def m2(cls):
#         print("This is a parent class method")
#
#     @staticmethod
#     def m3():
#         print("This is a parent static method")
#
# class C(P):
#     pass
#
# c=C()
# print(c.a)
# print(c.b)
# c.m1()
# c.m2()
# c.m3()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eatdrink(self):
#         print("Eat Egg Rice and Drink Water")
#
# class Employee(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         self.eno=eno
#         self.esal=esal
#
#     def work(self):
#         print("Coding Python is very easy like drinking chilled water")
#
#     def empifo(self):
#         print("Employee Name is :",self.name)
#         print("Employee Age is :",self.age)
#         print("Employee Salary is",self.esal)
#         print("Employee Number is",self.eno)
#
#
# e=Employee("BG",31,121,10000)
# e.eatdrink()
# e.work()
# e.empifo()

# class A():
#     def m1(self):
#         print("Parent A Method ")
#
# class B(A):
#     def m2(self):
#         print("Child B Method ")
#
# class C(B):
#     def m3(self):
#         print("Child C Method")
#
# class D(C):
#     def m4(self):
#         print("Child D method")
#
# class E(C):
#     def m5(self):
#         print("Child E method")
#
# class F:
#     def m6(self):
#         print("Parent F method")
#
# class G:
#     def m7(self):
#         print("Parent G method")
#
# class H:
#     def m8(self):
#         print("Parent H method")
#
# class I(F,G,H):
#     pass


# class A:pass
#
# class B():pass
#
# class C():pass
#
# class X(A,B):pass
#
# class Y(B,C):pass
#
# class P(X,Y,C):pass
#
# print(A.mro())
# print(B.mro())
# print(C.mro())
# print(X.mro())
# print(Y.mro())
# print(P.mro())

#Demo Program 2 using super() method to call parent class members
# in subclass constructor
# class Person:
#     a=10
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display(self):
#         print("My name is :",self.name)
#         print("My age is :",self.age)
#
#     @classmethod
#     def m2(cls):
#         print("Parent class Method")
#
#     @staticmethod
#     def m3():
#         print("Parent Static Method")
#
# class Student(Person):
#
#     def __init__(self,name,age,rollno,marks):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.marks=marks
#         print(super().a)
#         super().display()
#         super().m2()
#         super().m3()
#
# s=Student("K2",23,44,90)

# class Animal:
#     def speak(self):
#         return "Some sound"
#
# class Dog(Animal):
#     def speak(self):
#         return "Bow Bow!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# def animal_speak(animal):
#      print(animal.speak())
#
#
# # Using polymorphism
# dog = Dog()
# dog.speak()
# cat = Cat()
# cat.speak()
#
# animal_speak(dog)  # Output: Bow Bow
# animal_speak(cat)  # Output: Meow!

#Demo 1
# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#
#     def __add__(self, other):
#         return self.pages+other.page
#
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)
#
# #Demo 2
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"Point({self.x}, {self.y})"
#
# p1 = Point(2, 3)
# p2 = Point(4, 5)
# print(p1 + p2)  # Output: Point(6, 8)

#Operator Overloading
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def __mul__(self, other):
#         return self.salary*other.days
#
# class Timesheet:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days
#
# e=Employee("BG",100)
# t=Timesheet("BG",30)
# print("This Month salary is",e*t)

# class Test:
#     def m1(self):
#         print("No argument method")
#     def m1(self,a):
#         print("One argument method")
#     def m1(self,a,b):
#         print("Two argument method")
#
# t=Test()
# #t.m1()
# #t.m1(10)
# t.m1(10,20)

# class Test:
#     def __init__(self):
#         print("No argument Constructor")
#
#     def __init__(self,a):
#         print("One argument Constructor")
#
#     def __init__(self,a,b):
#         print("Two argument Constructor")
#
# t=Test(100,200)

# class P:
#     def property(self):
#         print("Gold + Cash + Power")
#
#     def business(self):
#         print("Hotel + Resort + Travels")
#
# class C(P):
#     def business(self):
#         super().business()
#         print("Startup on consulting + Car show room")
#
# c=C()
# c.property()
# c.business()

# class P:
#   def __init__(self):
#       print("Parent class Constructor")
#
# class C(P):
#     def __init__(self):
#         super().__init__()
#         print("Child class Constructor")
#
# c=C()

# #Case 1 ==>#Concrete Class
# class Test:
#     pass
#
# t=Test()
#
# #Case 2 ==>#Concrete Class
# class Test1:
#     def m1(self):
#         print("Hello")
#
# t2=Test1()
#
# #Case 3 : Its a abstaact class we are able to create object since its not having abstract method
# from abc import *
# class Test(ABC):
#     pass
#
# t2=Test()
#
# #Case 4 : Abstract class with Abstract method we can't Create Object
# #Abstract class with Abstract method we can't instantiate,
# #To create object we have to implement abstract method in future classes
#
# from abc import *
# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#
# class Hello(Test):
#     def m1(self):
#         print("Good Morning")
#
# h=Hello()

# from abc import *
# class Vehicle(ABC):
#     @abstractmethod
#     def noofwheels(self):
#         pass
#
#
#
# class Bus(Vehicle):
#     def noofwheels(self):
#         return 6
#
# b=Bus()
# print(b.noofwheels())
#
# class Bike(Vehicle):
#     def noofwheels(self):
#         return 2
#
# b1=Bike()
# print(b1.noofwheels())

# from abc import *
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#
#     @abstractmethod
#     def stop_engine(self):
#         pass
#
# class Car(Vehicle):
#     def start_engine(self):
#        print("Car Engine Started")
#
#     def stop_engine(self):
#         print("Car Engine Stopped")
#
# c=Car()
# c.start_engine()
# c.stop_engine()

# from abc import *
# class DBinterface(ABC):
#     @abstractmethod
#     def connect(self):pass
#
#     @abstractmethod
#     def disconnect(self):pass
#
# class Oracle(DBinterface):
#     def connect(self):
#         print("Connecting to Oracle Database")
#
#     def disconnect(self):
#         print("Disconnecting to Oracle Database")
#
# o=Oracle()
# o.connect()
# o.disconnect()
#
# class MySQL(DBinterface):
#     def connect(self):
#         print("Connecting to MySQL Database")
#
#     def disconnect(self):
#         print("Disconnecting to MySQL Database")
#
#
# m=MySQL()
# m.connect()
# m.disconnect()

# from abc import *
# #Interface
# class Automation(ABC):
#     @abstractmethod
#     def m1(self):pass
#
#     @abstractmethod
#     def m2(self):pass
#
#     @abstractmethod
#     def m3(self): pass
#
# #Abstract clas
# class Manual(Automation):
#     def m1(self):
#         print("M1 Method implementation")
#
#     def m2(self):
#         print("M2 Method implementation")
#
# #Concrete Class
# class Fullstactqa(Manual):
#     def m3(self):
#         print("M3 Method implementation")
#
# f=Fullstactqa()
# f.m1()
# f.m2()
# f.m3()

# y=200
# name='Basava'
#
# class QACircle:
#     x=100
#     s="QACircle"
#     _a=2000
#
# class B(QACircle):
#     pass

# class Test:
#     x=10
#     _y=20
#     __z=30
#
#     def m1(self):
#         print(Test.x)
#         print(Test._y)
#         print(Test.__z)
#
# t=Test()
# t.m1()
# print(t)
# print("*******")
# print(Test.x)
# print(Test._y)
# #print(Test.__z) #here you will get attribute error you can't access
#
# #How to access Private variable from outside of class:
# #We can access indirectly objectreference._classname__variablename
# class Test:
#     x=10
#     _y=20
#     __z=30
#
#
# t=Test()
# print(t._Test__z)

# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#
#     def __str__(self):
#         return "This is Student with name : {} and ROllno : {}".format(self.name,self.rollno)
#
# s1=Student("BG",230)
# s2=Student("QACircle",23)
# print(s1)
# print(s2)

# class Account:
#     def __init__(self,name,balance,min_balance):
#         self.name=name
#         self.balance=balance
#         self.min_balance=min_balance
#
#     def deposit(self,amount):
#         #self.balance=self.balance+amount
#         self.balance += amount
#
#     def withdraw(self,amount):
#         if self.balance-amount >= self.min_balance:
#             self.balance -=amount
#         else:
#             print("Sorry, Insufficient Fund")
#
#     def printStatement(self):
#         print("AccountBalance :",self.balance)
#
# class Current(Account):
#     def __init__(self,name,balance):
#         super().__init__(name,balance,min_balance=-1000)
#
#     def __str__(self):
#         return "{} Current Account with balance : {}".format(self.name,self.balance)
#
# class Saving(Account):
#     def __init__(self,name,balance):
#         super().__init__(name,balance,min_balance=0)
#
#     def __str__(self):
#         return "{} saving Account with balance : {}".format(self.name, self.balance)
#
#
# c1=Current("BG",20000)
# c1.deposit(7000)
# print(c1)
# c1.withdraw(29000)
# print(c1)
#
# s1=Saving("Nanda",200000)
# s1.deposit(7000)
# print(s1)
# s1.withdraw(207000)
# print(s1)
#
# class BankAccount:
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # Private attribute
#
#     # Public method to deposit money
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
#         else:
#             print("Deposit amount must be positive.")
#
#     # Public method to withdraw money
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}")
#             print(100/0)
#         else:
#             print("Insufficient funds or invalid amount.")
#
#     # Public method to check balance
#     def get_balance(self):
#         return self.__balance
#
# # Usage
# account = BankAccount("Priya", 10000)
# account.deposit(1000)
# account.withdraw(2000)
# print(f"Final balance: ₹{account.get_balance()}")


# # Without try-Except
# print("Hello")
# print(10/0)
# print("Hi")
#
# #With try-Except block
# print("Hello")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print("Hi")


# try:
#     print("Try block executed")
# except :
#     print(" except block")
# else:
#     print("else")
# finally:
#     print(" finally block")

class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg

age=int(input("Enter your age"))
if age<18:
    raise TooYoungException("Please wait still you have time for marriage, your not eligible now")

elif age>60:
    raise TooOldException("You will not able to get married unless you have money")

else:
    print("You are eligible for marriage")