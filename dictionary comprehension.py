# list1=[1,2,3,4,5,6,7]
# dict1={i:i**3 for i in list1 if i%2!=0}
# print(dict1)


#dictionary len name

# name=['adarsh','anas','thabsheer']
# newdict={i:len(i) for i in name}
# print(newdict)

# li2=[1,2,3,4,5,6,7,8,9,10]#set comprehension
# set2={i for i in li2 if i%2==0}
# print(set2)

# list1=[1,2,3,4,5,6]
# set=set()
# for i in list1:
#     if i%2==0:
#         set.add(i)
# print(set)

set3=("apple",'orange','hey')
set4={len(i) for i in  set3}
print(set4)

li3=[1,2,3,4,5,6,7,8,9,10]
set5={i**2 for i in li3}
print(set5)
