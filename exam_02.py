"""
Questions on PCAP-31-03 Practice Test 2
All code which will cause error is commented out - uncomment them to test if you want
"""
# Question 2
import random
a = random.randrange(2, 20, 3)
b = random.sample([1, 5, 10], 1)
c = random.randint(10, 20)

print(f"a is {a}, b is {b}, c is {c}")


# Question 3
import platform
print(platform.python_implementation())


# Question 4
from package.dir_a.dir_b import mod_c


# Question 7
class Err(Exception):
	def __init__(self, msg):
		self.message = msg

	def __str__(self):
		return "From Err block"				# This message has priority when printed


# try:
# 	print("Start")
# 	raise Exception("Error raised")			# Exception Error is raised
# except Err as e:							# Err will not catch it
# 	print(e)
# else:
# 	print("From else block")


# Question 8
# number = '5'
#
# try:
# 	x = int(dog)			# this would be a NameError as dof is not defined - but suntax error thrown first
# except:						# Except block must always be last - syntax error thrown before code can run
# 	x = 0
# except ValueError:
# 	x = 1
# except ArithmeticError:
# 	x = 2
# finally:
# 	print(number)


# Question 10
try:
	assert 'zero'				# assert branch raises error if value is False - non empty strings are Truthy
except:
	print("one", end=' ')		# no exception raised as 'zero' was True
else:
	print("two", end=' ')		# no error raised in try branch => else branch will execute
finally:
	print("three")				# as long as code runs and reaches this try block,  final branch is always executed


# Question 12
s = 'It is either easy or impossible'
s = s.replace('hard', 'easy').replace('easy', 'hard') 	# first replace() does nothing as no 'hard'
print(s)


# Question 15
string = str(16**1/2)
temp = ''
for character in string:
	temp += character
print(temp[-1])


# Question 16
# 'car'.lfind('c')					# lfind() does not exist. Finding from left of string is just find()
print('dog'.endswith('i'))
print('mouse'.index('ou'))
# title('cow')						# should be 'cow'.title()


# Question 17
# at in math							# NameError
# print('c'.isupper() in 'Cat')			# TypeError - Bool can't be compared with string
print('The'[-2] in 'Python')			# True
print('dog'[::-1] not in 'good')		# True


# Question 18
for ch in "abc":
	print(chr(ord(ch) + 1), end='')
print()

# Question 19
print(10+1 == '1'+1*'1')				# False
print('AbC' > 'AB')						# True
print('0'+'0'+'0' > '0' * 0)				# True
# print('2'-'1' == '1')					# TypeError
print('cat','dog','mouse')				# Extra: Note no explicit space between commas but default sep is a space


# Question 21
class Class:
	var = 0

	def __init__(self):
		self.value = 0


obj_a = Class()
obj_a.var = 5
obj_b = Class()
print(obj_a.var, obj_b.var)


# Question 22
class A:
	top = 1
	def __init__(self):
		self.val = 1

class B(A):
	mid = 2
	def __init__(self):
		self.val = 2
		self.__val = 2

class C(B):
	bot = 3
	def __init__(self):
		super().__init__()

obj_a = A()
obj_b = B()
obj_c = C()

print(obj_b.top == 1)					# True
print(obj_c.val is not None)			# True
print(hasattr(obj_b, '__val'))			# False, to access __val need '_B__val'
# print(isinstance(obj_c, obj_a))		# TypeError obj_a should be A for true


# Question 25
class ExampleClass:
	counter = 0

	def __init__(self, val_one =1, val_two=2):
		self._first = val_one
		self.__second = val_two
		ExampleClass.counter += 1


example_object_1 = ExampleClass()

print(example_object_1.__dict__)
print(ExampleClass.__dict__)


# Question 26
class Classy:
	pass


obj = Classy()
print(Classy.__name__)
# print(obj.__name__)				# AttributeError - __name__ is a class method, obj is an object
# print(Classy().__name__)			# AttributeError - same as above, Classy() creates an object
print(type(obj).__name__)


# Question 27
# inside test.py
class Classy:
	pass


print(Classy.__module__)

obj = Classy()


# Question 29
class Mouse:
	def __init__(self, name):
		self.name = name

	# insert your code here
	# def __str__(self):					# Both repr and str work - comment one out
	def __repr__(self):
		return "My name is " + self.name


mouse = Mouse("Danger")
print(mouse)


# Question 30
class A:
	pass


class B(A):
	var = 1


class C(A):
	var = 2


class D(B, C):
	pass


d = D()
print(d.var)


# Question 32.
try:
	f = open('sample.txt', 'rt')
	d = f.readline()
	print(len(d))
	f.close()
except IOError:
	print(-1)


# Question 33
try:
	f = open('file', 'w')
	print(1, end=' ')
except IOError as error:
	print(error.errno, end=' ')
	print(2, end=' ')
else:
	f.close()
	print(3, end=' ')
print()


# Question 35
import os
print(os.name)


# Question 36
from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%b/%d'))


# Question 38 - uncomment odd lists to test them
any_list = [1, 2, 3, 4]
# odd_list = list(map(lambda x: x % 2, any_list))
odd_list = [x for x in any_list if x % 2]
# odd_list = list(filter(lambda x: x is 1 or x is 3, any_list))
# odd_list = [filter(lambda x: x == 1 or x == 3, any_list)]

print(odd_list)


# Question 39
any_list = [0, 1, 2, 3, 4]
new_list = list(map(lambda n: n | 1, any_list))
print(new_list)
