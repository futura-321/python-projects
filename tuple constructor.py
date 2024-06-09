x=('apple','orange','grape')
print(x)
y=list(x)
print(y)
y[0]='banana'
x=tuple(y)
print(x)


#TUPLE unpacking
tuple2=("apple","orange","mango")
x,y,z=tuple2
print(x,y,z)
print(tuple2.count("apple"))


