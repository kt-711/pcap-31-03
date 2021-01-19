"""
Questions on PCAP-31-03 Practice Test 3
All code which will cause error is commented out - uncomment them to test if you want
"""
# Question 1
x = 5 % 3
y = x if x >= 1 else print(y)         # NameError - y is not defined is NOT called because x>=1 is true
print(x, y)


# Question 2
import random

a = random.random()
b = random.randint(1, 10)

print(len(random.sample([1, 2, 3, 4], 1)) > a)      # True
print(a == b)                                       # False
print(random.choice((1, 2, 3)) > b)                 # False - usually but not always
print(a < b)                                        # True


# Question 3
import platform
print(platform.python_version())        # outputs python version


# Question 4
import package.mod_a                    # Correct import of mod_a - when you run this file, you'll see
#                                        package.mod_a in your console
# from package.dir_a import mod_a
# from package import mod_a.py          # Syntax Errors
# import mod_a from package


# Question 5
from math import e, exp, log

print(log(e, e) == exp(0))              # 1 == 1 so Outputs True


# Question 7
# y = 0
#
#
# def function(x, y):
#     global y                    # Syntax Error - y used for parameter and global
#     y = 1
#     assert y != 0
#     try:
#         return x / y
#     except ZeroDivisionError:
#         raise ValueError
#
# try:
#     function(0, 0)
# except ArithmeticError:
#     y += 1
# except:
#     y += 3
#
# print(y)


# Question 8
lst = [0, 1, 2, 3]

try:
    x = lst[4]
# except IndexError:
except LookupError:                     # LookupError is a parent of IndexError so both will handle this error
    print("Oh noes we have an error!")


# Question 10
# lambda x, y: return x//y - x%y            # SyntaxError cannot return in lambda
lambda x, y: x//y - x%y
# lambda (x,y) = x//y - x%y                 # Syntax Error cannot unpack tuple
lambda x, y: (x, y)


# Question 12
print('Hello','World','!', sep='***', end='')
print('Hello World !', sep='***', end='')           # 6 stars output
print()


# Question 15
string = "Twinkle twinkle little star"

string = string.split(',')

print(string, len(string))                  # length 1


# Question 17
print(ord("z") - ord("Y") == 1)             # False
print(len("""""") == 0)                     # True
print(len('\n') == 1)                       # True
print(chr(ord('A') + 1) == 'b')             # False


# Question 18
names = ['Alice', 'Bob', 'Charlie']
names.sort(key=lambda x: (x[-1], x[-2]), reverse=True)
print(names)                                # ['Charlie', 'Alice', 'Bob']


# Question 19
# print(99 > '99')          # TypeError
print('ABc' > 'CAB')        # False
print(len("""""") <= 1)     # True
print('True' != True)       # True


# Question 21
x = 16 ** (1/2)
y = 2. if x < 6 else 4.

print(y)


# Question 22
class A:
    top = 1

    def __init__(self):
        self.val = 1


class B(A):
    mid = 2

    def __init__(self):
        self.val = 1
        self.__val = 3


class C(B, A):
    bot = 3

    def __init__(self):
        pass
        # super().__init__()  # Replace pass with this line and code will run
        # B.__init__(self)  # Replace pass with this line and code will run


obj_a = A()
obj_b = B()
obj_c = C()
# print(obj_c.val)          # Attribute Error


# Question 25
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())                   # Outputs 1
# Below is extra code for the explanation
print(stack_object)                         # prints Stack object memory reference as no def __str__
print(stack_object._Stack__stack_list)      # Get around name mangling to access the actual list
print(stack_object.push(4))                 # adds 4 to list but as you can see prints None


# Question 26
class A:
    def __init__(self):
        print('Calling Class A')


class B(A):
    def __init__(self):
        # insert code here
        super().__init__()
        A.__init__(self)

b = C()


# Question 27
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(C, A), issubclass(C, B), issubclass(C, C))


# Question 29
def foo(x, y, z):
    return x(y) - x(z)


print(foo(lambda x: x ^ 1, 2, 1))


# Question 30
def foo(x, y):
    return y(x) + y(x+1)


print(foo(1, lambda x: x * x))


# Question 32
def fun(n):
    for i in range(n):
        yield i


x = fun(4)
print(x)


# Question 33
var = 1


def foo():
    global var
    var += 2

    def g():
        return var
    return g


a = foo()
b = foo()

print(a is b)                           # False
print(a() is b())                       # True
print(var == 5)                         # True
# print(isinstance(a, foo))             # Correct way to call print(isinstance(a, type(foo)))


# Question 36
import time

timestamp = time.time()
print("Timestamp:", timestamp)


# Question 37
import calendar

calendar.setfirstweekday(6)
print(calendar.weekheader(2))


# Question 38
print((lambda x: [])(2))
print((lambda: 2 * 2)())                # function in parenthesis so can output number rather than address
# lambda x: def foo(x): return 1 / x    # Syntax Error
# lambda: lambda                        # Syntax Error for incomplete inner lambda function
print((lambda: (lambda: 5)())())        # possible way to complete above lambda


# Question 39
any_list = [0, 1, 2, 3, 4]
new_list = list(map(lambda n: n << 1, any_list))
print(new_list)
