list = [1, 2, 3, 4, 5]
print(list)
li = ['apple', 'orange', [1, 2, 3, 4, 5]]
print(li[2][2])
print(li[1][4])
li1=[1,2,3,4,5,6,7,8,9]
print(li1[0:8])
print(li1[:9])
li2=['apple','orange',[1,2,3,4,5]]
(li2[0])='grape'
print(li2)
li4=[1,2,3,4,5,6,7,8,9]
li4[0:5]=10,11,13,14
print(li4)


#to add single value in list use append

li5=[1,2,3,4,5,6,7,8,9]
li5.append(10)
print(li5)

#to add multiple values
li5.extend([11,12,13,14])
print(li5)



#concatination
li6=[1,2,3,4,5]
li7=[6,7,8,9]
print(li6+li7)

li8=[1,2,3,4,5,6,7]# insert and skewsing-for adding values at a specific index position
li8.insert(3,10)
print(li8)
li8.insert(3,[1,2])
print(li8)



#repeatation
print(['apple']*3)



#deletion and remove
li9=[1,2,3,4,5,6]
del li9[0:2]
print(li9)
li9.remove(6)
print(li9)

# negative index-for accessing elements from the last
li10=[1,2,3,4,5]
print(li10[-1],li10[-2],li10[-3])



