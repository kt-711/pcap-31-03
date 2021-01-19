"""
Questions on PCAP-31-03 Practice Test 1
All code which will cause error is commented out - uncomment them to test if you want
"""
# Question 1
import math
pi = 3.141592653589793

# insert  your code here to output 3
# print(math.round(pi))
print(math.ceil(pi))    # 4
print(round(pi, 0))     # 3.0
print(math.trunc(pi))   # 3 correct


# Question 2
# from math import sqrt
# cannot use from math - NOTE code WILL work because whole of math is imported from Q1! (line 6)
# print(dir(math))


# Question 3
from platform import system
print(system())     # Windows (or whatever current OS is)


# Question 4 - commented out incorrect answers
from module import var as pyvar       # correct
pyvar = 1

# import module
# var = 1

from module import *                  # correct
var = 1

# from var import module
# var = 1


# Question 7
# try:
# 	print(int('0'))                     # No error so except branch skipped and straight to else
# except NameError:
# 	print('0')
# else:
# 	print(int(''))                      # will cause a NameError

try:
    print(0/0)                          # ZeroDivisionError
except:
    print(0/1)                          # Error caught here and 0/1 is 0, it's not an error
else:
    print(2/0)

try:
    print(math.sqrt(-1))                # ValueError
except:
    print(math.sqrt(0))                 # Error caught and sqrt(0) is not an error
else:
    print(math.sqrt(1))

# try:
# 	print(float("1e1"))                 # handled fine so except branch skipped
# except (NameError, SystemError):
# 	print(float("1.1"))
# else:
# 	print(float('1c1'))                 # will cause a ValueError because no base c


# Question 8
try:
    print(1 // 0)
except ArithmeticError:
    print("Error handled by arithmetic branch")             # correct
except ZeroDivisionError:                                   # most IDE will flag this line as unreachable code
    print("Error handled by zero division branch")
except:
    print("Error handled by except branch")


# Question 9
print(issubclass(KeyError, Exception))                  # True
print(issubclass(LookupError, Exception))               # True
print(issubclass(SystemExit, Exception))                # False
print(issubclass(KeyboardInterrupt, Exception))         # False


# Question 10
def foo(x):
    assert x
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except AssertionError as e:
    print(e)                    # this is executed which is a blank line
except:
    print("some")


# Question 11
# x = 1E250 ** 2                                      # will cause OverflowError
# print(x, "is a really big number", sep=" : ")


# Question 12 - added print so you can see the output
print(str(1+1) in '0123456789'[3::])    # False
print('bea' in 'beta')                  # False
print('fed' in 'abcdefgh'[::-1])        # True
print('True' not in 'False')            # True


# Question 14
string = """\\
\\"""
print(len(string))              # outputs 3


# Question 15
alphabet = "abcdefghijklmnopqrstuvwxyz"

# alphabet.insert(0, "A")           # AttributeError
# del alphabet[0]                   # TypeError
alphabet[-30:30:-1]                 # blank line because of the -1
alphabet.lstrip()                   # would remove whitespace to left of string but as none to remove does nothing


# Question 16
x = "True"
y = 3
print(x == y)       # Outputs False - string comparison is always False


# Question 17
for ch in "aBc123":
    if ch.isupper():
        print(ch.lower(), end='\n')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')
# Ab
# C123


# Question 18
print()                 # added new line or code will be joined to Question 17
s1 = 'dog cat rat'
s2 = s1.split()
print(s2[-4:1])         # outputs ['dog']


# Question 19
# my_list = ['Hello', 'World', '!']
# s = '\'.join(my_list)                     # error this line because of \
# print(s)


# Question 20
class X:
    pass


class Y(X):
    pass


class Z(Y):
    pass


x = Z()
z = Z()

print(isinstance(x, Z), isinstance(Z, X))       # output: True False


# Question 21
class Class:
    _Var = 5
    __Var = 10

    def __init__(self):
        self._prop = 1
        self.__prop = 2


o = Class()
print(o._Class__Var + o._prop)          # output: 11


# Question 25
class Sample:
    gamma = 0
    def __init__(self):
        self.alpha = 1
        self.__delta = 3


obj = Sample()

# insert  your code here
print(hasattr(obj, "__delta"))        # False
print(hasattr(obj, "gamma"))          # True
# print(hasattr(Sample, gamma))       # NameError - second parameter must be a string - if you add "" it will work
# print(hasattr(Sample, alpha))       # NameError as above


# Question 27
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


# class E(A,C):         # TypeError i.e. MRO error
#     pass


class E(D, A):
    pass


class E(C, D):
    pass


# class E(B,D):         # TypeError i.e. MRO Error
# 	pass


# Question 28
class Mouse:
    def __init__(self, name):
        self.my_name = name


the_mouse = Mouse('mickey')
print(the_mouse)                # output: <__main__.Mouse object at 0x7f260df4d460>


# Question 29
class Mouse:
    pass


mickey = Mouse()
minnie = Mouse()
jerry = mickey
print(mickey is minnie, mickey is jerry)    # output: False True


# Question 31 - desired output [1, 2, 3]
class MyClass:
    def __init__(self, size):
        self.queue = [i for i in range(1, size)]

    def get(self):
        return self.queue

    def get_last(self):
        return self.queue[-1]

    def add_new(self):
        # insert the line of code here
        # self.queue.append(get_last() + 1)         # NameError
        # queue.append(self.get_last() + 1)         # NameError
        # self.queue.append(self.queue[+1])         # outputs [1, 2, 2]
        self.queue.append(self.get_last() + 1)      # outputs [1, 2, 3]


object = MyClass(3)
object.add_new()
print(object.get())


# Question 32
def fun(n):
    for i in range(n):
        yield i


for v in fun(4):
    print(v, sep=",")
# outputs
# 0
# 1
# 2
# 3


# Question 34
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner


b_tag = tag('<div>')
print(b_tag('Hello World!'))            # outputs <div>Hello World!</div>


# Question 36
import errno
try:
    f = open('text.txt')        # opened in read mod, remember default opening is 'r'
    f.write('hello world')      # IOError raised as cannot write to file opened in read mode
    f.close()

except IOError as error:
    print(error.errno)          # Outputs None, should be 13!!! Need to check why, was working before
    print(error)                # added this line to show you the error is "not writable" error

# Question 37
from datetime import datetime

dt1 = datetime(2020, 12, 29, 11, 33, 0)
dt2 = datetime(2020, 12, 28, 11, 33, 0)

print(dt1 - dt2)                        # outputs 1 day, 0:00:00


# Question 39
import calendar
print(calendar.weekheader(10))          # outputs Monday Tuesday Wednesday Thursday Friday Saturday Sunday

