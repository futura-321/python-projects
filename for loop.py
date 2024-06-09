for  x  in range(25,51):
    print(x)

numbers=[1,2,3,4,5,6]
for x in numbers:
    print(x,end=" ")

sum=0
a=int(input("enter your numbers:"))
for x in range(1,a+1):
    sum=sum+x
print(sum)

n=int(input("eneter multiplication number:"))
for i in range(1,n+1):
    print(i,"x",n,'=',i*n)


list1=[10,20,30,50]
print(list1)
reversedlist = []
for value in list1:
  reversedlist = [value] + reversedlist
print(reversedlist)



