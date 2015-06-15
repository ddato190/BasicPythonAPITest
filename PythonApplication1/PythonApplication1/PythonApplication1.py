import Test
print(Test.testList)
name = 'Jim'
print(name)
list = [1,2,3]
print(list)
print(list[0])
list.append(5)
print(list)
for intValue in list:
    print(intValue)

def TestFunc():
    return 222
print(TestFunc())

from Test import testList
print(testList)

#tempName = input('Your Name:')
#print(tempName)

floatDivide = 10/3
print(floatDivide)
intDivide = 10 // 3
print(intDivide)

twoFiveSquare = 2 ** 5
print(twoFiveSquare)

import decimal
doubleA = decimal.Decimal('1.0')
doubleB = decimal.Decimal('0.8')
doubleDiff = doubleA - doubleB
print(doubleDiff)

strPlusInt = 'Jim = ' + str(190)
print(strPlusInt)

print('%s is %d height, %.2f weight' % ('Jim',190,85.2222))
print('{0} is {1} Height'.format('Jim',190))

import math
print(format(math.pi,'.5f'))

list = []
list.append(1)
list.append('Jim')
list.append(True)
print(list)
print(len(list))

list = [[1,2,3],[4,5,6],[7,8,9]]
for row in list:
    for ele in row:
        print(ele)

list2 = list[:]
print(list2)

list = [1,8,5,6,9,4,3,7,2]
list.sort()
print(list)
list.sort(reverse = True)
print(list)

#Union
family = set()
family.add('Dad')
family.add('Mom')
family.add('Child')
print(family)

family = {'Jim'}
print(family)
for person in {'Maggie','Ping'}:
    family.add(person)
print(family)

#Dictionary
passwords = {'Jim':12345, 'Pai':67890}
print(passwords)
print(passwords['Jim'])
passwords = dict(justin = 123456, momor = 670723, hamimi = 970221)
print(passwords)
if 'Jin' in passwords:
    print(passwords['Jin'])
else:
    print(None)


class Demo:
    i = 9527
    def hello(self):
        print(self.i)
d = Demo()
d.hello()

#GC
import gc
gc.collect()

#Operators
password = ''
if not password:
    print('Need Password !!')

#if
#score = int(input('Score = '))
#if score >=90:
#    print('A')
#elif 80<= score and score < 90:
#    print('B')
#else:
#    print('C')
inputt = 3
print('{0} is {1}'.format(inputt, 'Even' if inputt % 2 else 'Odd'))

#for
for num in range(10):
    print(num)

matrix = [1,2,3,4,5,6,7,8,9]
for element in matrix[0:4]:
    print(element)

#for comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrixdouble = [element ** 2 for row in matrix for element in row]
print(matrixdouble)

#try except
try:
    score = int(input('Score = '))
    print(score)
except:
    print('Error')

#def
def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

sumTotal = sum(1,2,3,4,5)
print(sumTotal)

def selection(number):
    def min(m, j):
        if j == len(number):
            return m
        elif number[j] < number[m]:
            return min(j, j + 1)
        else:
            return min(m, j + 1)
    
    for i in range(0, len(number)):
        m = min(i, i + 1)
        if i != m:
            number[i], number[m] = number[m], number[i]

number = [1, 5, 2, 3, 9, 7]
selection(number)
print(number)

#lambda
max = lambda m,n: m if m>=n else n
print(max(5,2))

score = int(input('Score= '))
level = score // 10
{
    10 : lambda: print('Perfect'),
    9  : lambda: print('A'),
    8  : lambda: print('B'),
    7  : lambda: print('C'),
    6  : lambda: print('D')
}.get(level, lambda: print('E'))()

def add(m):
    def func(n):
        return m + n
    return func

tempAdd = add(5)(2)
print(tempAdd)

#class
class Some:
    x = 0
    def __init__(self, x):
        self.x = x
    def service(self, y):
        print('do service...', self.x + y)

    @staticmethod
    def service2(x, y):
        print('do service2...', x + y)

s1 = Some(10)
s1.service(5)
s2 = Some(50)
s2.service(5)

service1 = Some.service
service1(s1,20)
service1(s2,20)

s1.service2(10,30)
print(s1.x)

#Class constructor
class Some2:
    def __new__(clz):
        print('__new__')
        return object.__new__(clz)
    def __init__(self):
        print('__init__')

s3 = Some2()

class SingletonClass:
    _single = None
    def __new__(clz):
        if not SingletonClass._single:
            SingletonClass._single = object.__new__(clz)
        return SingletonClass._single
    def __del__(self):
        print('__del__')
    def doSomething(self):
        print("do something...XD")

single1 = SingletonClass()
single2 = SingletonClass()
print(single1 is single2)
single1 = None
single2 = None

#Inheritance
class BaseClass:
    #id = 100
    #name = 'Jim'
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return ('id = ' + str(self.id) + ', name = ' + str(self.name))
    def BaseMethod(self):
        print('BaseMethod !!')
    def ShowMessage(self):
        print('BaseClass ShowMessage !!')

class DerivedClass(BaseClass):
    def __init__(self, id, name):
        super(DerivedClass, self).__init__(id, name)
    def __str__(self):
        return ('id = ' + str(self.id) + ', name = ' + str(self.name))
    def ShowMessage(self):
        print('DerivedClass ShowMessage !!')

derivedObject = DerivedClass(123,'Jim')
derivedObject.BaseMethod()
derivedObject.ShowMessage()
print(derivedObject)

#Abstract
import random
from abc import ABCMeta, abstractmethod
class AbstractBase(metaclass=ABCMeta):
    @abstractmethod
    def ShowMessage(self):
        pass
    @abstractmethod
    def Guess(self):
        pass

class InheritAbstractClass(AbstractBase):
    def ShowMessage(self):
        pass
    def Guess(self):
        pass

abstractInherit = InheritAbstractClass()

#Module
import sys
print(sys.path)

import Test as Other
print(Other.testList)

import sys
print(sys.modules['Test'].testList)

#assert
tempValue = 1
assert tempValue > 0, 'tempValue must be greater than 0'

#Property()
class Ball:
    def __init__(self, radius):
        self._radius = radius
    def getRadius(self):
        return self._radius
    def setRadius(self, radius):
        self._radius = radius
    def delRadius(self):
        pass
    radius = property(getRadius,setRadius,delRadius,'Radius Property')

tempBall = Ball(3.14)
print(tempBall.radius)
tempBall.radius = 5
print(tempBall.radius)

#Function Intepret
def sidedish(number):
    def dish1(meal):
        return lambda: meal() + 30
        
    def dish2(meal):
        return lambda: meal() + 40
        
    def dish3(meal):
        return lambda: meal() + 50
        
    def dish4(meal):
        return lambda: meal() + 60
        
    def nodish(meal):
        return lambda: meal()
        
    return {
        1 : dish1,
        2 : dish2,
        3 : dish3,
        4 : dish4
    }.get(number, nodish)

@sidedish(2)
@sidedish(3)
def friedchicken():
    return 49.0

print(friedchicken())

#Method Intepret
def log(mth):
    def wrapper(self, a, b):
        return mth(self, a, b)
    return wrapper

class Some:
    @log
    def doIt(self, a, b):
        return a + b

s = Some()
print(s.doIt(1, 2))




