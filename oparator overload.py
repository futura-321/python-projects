class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
       sum=self.a+other.a
       return sum
obja=A(10)
objb=A(20)
print(obja+objb)

class B:
    def __init__(self,b):
        self.b=b
    def __gt__(self, other):
        result=self.b>other.b
        return result
obj1=B(20)
obj2=B(2)
print(obj1>obj2)

class c:
    def __init__(self,b):
        self.b=b
    def __mul__(self, other):
        result=self.b*other.b
        return result
obj1=c(20)
obj2=c(2)
print(obj1*obj2)
obj3=c("hey")
obj4=c(5)
print(obj3*obj4)

class D:
    def __init__(self,a):
        self.a=a
    def __eq__(self,other):
        result=self.a==other.a
        return result
obj5=D(10)
obj6=D(2)
print(obj5==obj6)







