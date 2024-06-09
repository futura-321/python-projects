class person:
    def massage(self,name=None):
        if name==None:
            print("hello")
        else:
            print('hello'+name)
p=person()
p.massage()
p.massage("world")

class A:
    def area(self,a,b=None):
        if b==None:
           res=a*a
           print(res)
        else:
            res=a*b
            print(res)
c=A()
c.area(10)
c.area(10,20)



