a={1,2,3,4,5,8,7}
b={1,2,3,6,9,10}
#set operations

print(a|b)# a union b
print(a.union(b))

print(a.intersection(b)) # a intersection b
print(a&b)

print(a-b)#diffrence
print(b-a)
print(a.symmetric_difference(b))#symetric diffrence betwwen a and b
print(a^b)