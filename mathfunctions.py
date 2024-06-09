import math

a=10.5
print(math.ceil(a))
print(math.floor(a))
print(math.factorial(5))
b=-5
print(math.fabs(b))
print(math.gcd(36,2))
print(math.copysign(5,-3))
print(math.sqrt(20))

def fun(a):#area of circle
    a=(math.pi)*(a**2)
    return a
print(fun(2))

import random
print(random.randint(1,9))
print(random.randrange(1,10,2))
print(random.choice([1,2,3,4,5]))
x=list(range(1,10,2))
(random.shuffle(x))
print(x)

import random as r
for x in range(1,6):
    a=int(input("enter a number:"))
    b=r.randint(1,5)
    if a==b:
        print("win the game")
    else:
        print("loose the game:")
    print(b)
    