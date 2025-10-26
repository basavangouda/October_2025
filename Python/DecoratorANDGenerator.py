# def outer(x):
#     def inner(y):
#         return x+y
#     return inner
#
# Add_five=outer(5)
# result=Add_five(100)
# print(result)
#
# # Decorator
# def make_pretty(func):
#     def inner():
#         print("I got decorated with makeup")
#         func()
#     return inner
#
#
# def ordinary():
#     print("I am Ordinary and not having makeup")
# """
# ordinary() ====> this will print "I am Ordinary and not having makeup"
# make_pretty()  ====>this takes function as an argument and it has nested function called inner
# ----- and returns inner function
#
# """
# decorated_func=make_pretty(ordinary)
# decorated_func()
#
#
# #Using @ symbol as decorator
#
# def make_pretty(func):
#     def inner():
#         print("I got decorated with makeup")
#         func()
#     return inner
#
# @make_pretty
# def ordinary():
#     print("I am Ordinary and not having makeup")
#
# ordinary()

# def smart_divide(func):
#     def inner(x,y):
#         print("I am going to divide",x," and ",y)
#         if y==0:
#             print("Whoops!! cannot divide")
#             return
#         return func(x,y)
#     return inner
#
#
# @smart_divide
# def divide(x,y):
#     print(x/y)
#
# divide(100,5)
# divide(00,5)
# divide(100,00)

# def simple_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper
#
# @simple_decorator
# def greet():
#     print("Hello, world!")
#
# greet()


import time

from numpy.ma.core import negative

# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took {end - start:.4f} seconds")
#         print(end-start)
#         return result
#     return wrapper
#
# @timer_decorator
# def slow_function():
#     time.sleep(2)
#     print("Finished slow task")
#
# slow_function()

# def star(func):
#     def inner(*args,**kwargs):
#         print("*"*15)
#         func(*args,**kwargs)
#         print("*"*15)
#     return inner
#
#
# def percentage(func):
#     def inner(*args,**kwargs):
#         print("%"*15)
#         func(*args,**kwargs)
#         print("%" * 15)
#     return inner
#
# @star
# @percentage
# def printer(msg):
#     print(msg)
#
#
# printer("Hello")

""""
***************
%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%
**************
"""
#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#star(percentage(printer("Hello")))

# @percentage
# @star
# def printer(msg):
#     print(msg)

#percentage(star(printer("Hello")))
#printer("Good Morning")

# def simplegeneratorFunc():
#     yield 1
#     yield 2
#     yield 3
#
# #Case 1 ==> using for loop
# for value in simplegeneratorFunc():
#     print(value)
#
# #case 2  Creating generator object
# x=simplegeneratorFunc()
#
# #iterating the generator values
# print(next(x))
# print(next(x))
# print(next(x))
#
# print("**********************************")
# #write fibonacci series using generator
# def fib(n):
#     #intialize first2 values
#     a,b=0,1
#     #One by one i want to yield next fibonacci number
#     while a<n:
#         yield a
#         a,b=b,a+b
#
# for i in fib(3):
#     print(i)

# def first(num):
#     n=1
#     while n<=num:
#         yield n
#         n=n+1
#
# value=first(10)
# for i in value:
#     print(i)

# import random
# import time
#
# names=["Basava","Apoorva","Suman","Arun"]
# subjects=["Python","SQL","Selenium","Java"]
#
# def people_list(num_people):
#     result=[]
#     for i in range(num_people):
#         person={
#             "id":i,
#             'name':random.choice(names),
#             'subject':random.choice(subjects)
#         }
#         result.append(person)
#     return result
#
# def people_generator(num_people):
#     for i in range(num_people):
#         person={
#             "id":i,
#             'name':random.choice(names),
#             'subject':random.choice(subjects)
#         }
#
#         yield person
#
# t1=time.time()
# people=people_list(1000000)
# t2=time.time()
#
# print('Took {}'.format(t2-t1))
# #Took 0.00011658668518066406
#
# t1=time.time()
# people1=people_generator(1000000)
# t2=time.time()
# print('Took {}'.format(t2-t1))

#Example 1 ==> multiply 5 for each number should be divisible by 2
# generator_exp=(i*5 for i in range(5) if i%2==0)
#
# for x in generator_exp:
#     print(x)
#
# #Example 2 ==> Get he squares of the numbers
# generator_square=(i*i for i in range(10))
#
# for x in generator_square:
#     print(x)

# #We can check normal collection vs Generator wrt to Memory Utilization
# #Normal Collection
# l=[x*x for x in range(1000000000000000000000000)]
# print(l[0])
#
# #Generators
# g=(x*x for x in range(1000000000000000000000))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# l=[10,20,30]
# iterator=iter(l)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


#Customized iterator
class EvenNumbers:
    def __iter__(self):
        self.num=2
        return self

    def __next__(self):
        result=self.num
        self.num=self.num+2
        return result

#Using the custom iterator
evens=EvenNumbers()
it=iter(evens)
print(it)

for i in range(21):
    print(next(it))