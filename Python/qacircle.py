
x=898

def add(a,b):
    print("The sum is:",a+b)

def product(a,b):
    print("The Product is:",a*b)

class Hello:
    y=100

    def f1(self):
        print("I am a class function")

h=Hello()

#Finding the members of Module using dir() function
print(dir()) #To print all the members of current Module

def info():
    if __name__ == '__main__':
        print("The Code is executed as a Program directly")
    else:
        print("The code is executed from some other Program")

info()