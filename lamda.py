double=lambda x:x*2
print(double(5))


a=lambda x:'even' if x%2==0 else 'odd'
print(a(10))

sum=lambda num1,num2:num1+num2
print(sum(10,20))

b= lambda y:'true' if y%5==0 else "false"
print(b(15))

multi=lambda n1,n2:n1*n2
print(multi(5,8))

list1=[1,2,3,4,5,6,7,8]#filter
list2=list(filter(lambda y:(y%2==0),list1))
print(list2)

list3=[1,2,3,4,5]#mapping
list4=list(map(lambda x:(x*5),list3))
print(list4)



from functools import reduce
sum=reduce((lambda x,y:x+y),list3)
print(sum)


