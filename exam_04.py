"""
Questions on PCAP-31-03 Practice Test 4
All code which will cause error is commented out - uncomment them to test if you want
"""
# Question 1
import math
x = math.e

# insert  your code here to output 3
print(math.floor(x))   # 2
print(math.ceil(x))    # 3
print(round(x, 0))     # 3.0 - read up on round function, it rounds down for odds and up for evens
print(math.trunc(x))   # 2


# Question 2
import random

a = random.randrange(2, 10, 2)
b = random.randint(1, 10)

print(len(random.sample([1, 2, 3, 4], 1)) < a)      # True
print(random.random() < b)                          # True
print(random.choice((1, 2, 3)) > b)                 # Can be True or False
print(a < b)                                        # Can be True or False


# Question 3
import platform

print(platform.machine())


# Question 7
class Err(Exception):
    def __init__(self, msg):
        self.message = msg

    # Comment out this str function if you want the message in Err to be printed
    def __str__(self):
        return "From Err block"				# This message has priority when printed


try:
    print("Start")
    raise Err("Error raised")			    # Err Error is raised
except Err as e:							# Err will catch it
    print(e)
else:
    print("From else block")


# Question 8
dict_pets = {'dog': 1, 'cat': 1}

try:
    print(dict_pets['mouse'])
except LookupError:
    print("Error handled by lookup branch")
except KeyError:
    print("Error handled by key branch")
except:
    print("Error handled by except branch")


# Question 9
print(issubclass(NameError, OSError))           # False
print(issubclass(SystemError, SystemExit))      # False
print(issubclass(ValueError, Exception))        # True
print(issubclass(FileNotFoundError, OSError))   # True


# Question 10
def foo(x):
    assert x, 'assertion error'         # assertion error message attached with a comma
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except AssertionError as e:
    print(e)


# Question 11
try:
    print('No need for except block')
finally:
    print('yup')


# Question 12
print(str(1+1) in '0123456789'[-1::-1])     # True
print('be'.title() in 'beta')               # False
print('fed'.find('d') in [1, 2, 3])         # True
# print(True not in 123)                    # TypeError


# Question 14
print('Hello World!'.replace('i', 'e'))            # 'Hello World!'
# 'Hello World!'.join()                            # .join() needs a list argument
# 'Hello World!'.sort()                            # .sort() is a list method
print('Hello World!'.center(20, 'a'))              # centre with 20 chars, 'a' used as filler


# Question 15
x = False
y = '0'

# print(x >= y)             # Type Error - cannot compare with > or < with different types


# Question 16
print("good"[:3] == "dog"[::-1])    # False
# print(len(300) == 3)                  # Type Error - integers have no len property
print(chr(32) == " ")               # True
print(len("two dogs") == 8)         # True


# Question 18
string = str(2**2**3)

temp = ''

for ch in string:
    if ch in '12345':
        temp += ch

print(temp)


# Question 19
num = 1_000 / 1000

s = str(num)[-1]

print(s == str(1.)[-1])


# Question 21
class X:
    pass

class Y(X):
    pass

class Z(X):
    pass

y = Y()
z = Z()

print(isinstance(y, Z), isinstance(z, Y))


# Question 22
class Class:
    var = 1
    _var = 2

    def __init__(self):
        self._prop = 1
        self.__prop = 2


o = Class()
o.var += 1                      # sets a new local variable o.var = 2
print(Class.var + o._prop)


# Question 25
# inside exam_04.py
from test import Classy


print(Classy.__module__)

obj = Classy()              # this does nothing and only to confuse you


# Question 26
class A:
    def __init__(self):
        self.var = 0


class B(A):
    var = 1


class C(A):
    var = 2


class D(B, C):
    pass


d = D()
print(d.var)
print(hasattr(d, 'var'), d.__dict__)        # shows d has inherited a local var


# Question 28
# class Mouse:
#     def __init__(self, name):
#         self.my_name = name
#
#     def __str__():                          # missing sel;f parameter
#         return self.my_name
#
#
# the_mouse = Mouse('mickey')
# print(the_mouse)


# Question 30
class Stack:
    def __init__(self, size):
        self.stack = [i for i in range(1, size)]

    def __str__(self):
        return str(self.stack)

    def pop(self):
        x = self.stack[-1]
        del x
        return x

    def push(self, value):
        # insert the line of code here
        self.stack.append(value)


object = Stack(3)
object.push(3)
print(object)


# Question 31
class ExampleClass:
    counter = 0

    def __init__(self, val_one =1, val_two=2):
        self.first = val_one
        self.second = val_two
        ExampleClass.counter += 1


example_object_1 = ExampleClass(3)

print(example_object_1.__dict__)


# Question 32
def outer(val1):
    var = val1
    _var = 3

    def inner(val2):
        return var ** _var ** val2
    return inner


clos = outer(2)
print(clos(2))


# Question 33
var = 1


def foo():
    global var
    var += 2

    def g():
        return var

    return g


a = foo()
var += 1
b = foo()

print(a() == 6)                 # True
print(b() == 6)                 # True
print(a == b)                   # False
# print(isinstance(b, type(g)))   # NameError


# Question 35
any_list = [0, 1, 2, 3, 4]
new_list = list(filter(lambda n: n & 1, any_list))
print(new_list)


# Question 37
print((lambda x: [])(2))
print((lambda: (1, 1))())
# lambda x: return 1 / x            # Syntax error
# print((lambda y x:2)())            # Syntax Error


# Question 38
from datetime import date

d = date(2021, 1, 12)
print(d.strftime('%y/%m/%d'))


# Question 40
try:
    f = open('file', 'a')
    print(1, end=' ')
except IOError as error:
    print(error.errno, end=' ')
    print(2, end=' ')
else:
    f.close()
    print(3, end=' ')
