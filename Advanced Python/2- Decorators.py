def myDecorators1(function):

    def wrapper():
        # if u will are change functions positions (like a move to 7 row) its will change starting func/def
        function()
        print("myDecorators1: That's my Decorator func")

    return wrapper

def printHello1():
    print("myDecorators1: HELLO HELLO")
myDecorators1(printHello1)()

#------------#

def myDecorators2(function):

    def wrapper():
        function()
        print("myDecorators2: That's my Decorator func")

    return wrapper
# You can use like that 
@myDecorators2
def printHello2():
    print("myDecorators2: HELLO HELLO")

printHello2()

#------------#

def myDecarators3(function):

    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("myDecorators3: That's my Decorator func")
        return return_value

    return wrapper
@myDecarators3
def printHello3(person):
    return f"myDecorators3: HELLO HELLO {person}!"

print(printHello3("Mert"))

#------------#

#Practical Example #1 - Logging
def logged(function):
    def wrapper (*args, **kwargs) :
        value = function(*args, **kwargs)
        with open('logfilee.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10,20))

import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value

    return  wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result *= i
    return  result

myfunction(100000)