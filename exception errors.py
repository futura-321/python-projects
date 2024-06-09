a=[1,2,3]
try:
   print('print 1st element',a[0])
   print("print 5th element",a[5])

except:
    print("the index out of range")#handle the exeption



def func(a):
    if a<4:
        b=a/(a-3)
        print("value of b is:",b)
try:
    func(2)
    func(1)
    func(3)

except ZeroDivisionError:
    print("zero divisional error occured")
except NameError:
    print("name error occurede")
except IndexError:
    print("index error occured")


def fun(x,y):
    result=x/y
    print(result)
try:
    fun(20,20)

except ZeroDivisionError:
    print("zero divisional error occured")
except NameError:
    print("name error occurede")
except IndexError:
    print("index error occured")
except ValueError:
    print('value error occured')






try:
   a=int(input("enter a number:"))
   b=int(input("enter second number:"))
   print(a/b)
except ZeroDivisionError:
     print("zero divisional error occured")
except NameError:
     print("name error occurede")
except IndexError:
     print("index error occured")
except ValueError:
    print('value error occured')






try:
    a=int(input("enter first number:")) #user defined
    b=int(input("enter second number:"))
    x=(a/b)
    print(x)
except ZeroDivisionError:
    print("zero division error")
    res=a/4
    print(res)
print("finished")



def arithmetics(a,b):
    try:
      c=(a+b)/(a-b)
    except Exception as arg:
        print(arg)
    else:
      print(c)
arithmetics(9,2)
arithmetics(0,0)




string="hello"#
try:
    b=string/100
except Exception as arg:
    print(arg)




try:
   a='hey'+10 #
   print(a)
except Exception as arg:
    print(arg)










