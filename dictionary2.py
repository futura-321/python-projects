student={'name':'jhon','age':20,'grade':'A','courses':['maths','history']}
print(student['name'],student['age'])
student['courses'].append('english')
#print(student['phone'])
for i in student['courses']:
     print(i)
student['age']=21
print(student)

adress={'street':'123 main st','city':'any town','state':'CA','zip':'12345'}
student['adress']=adress
print(student)
student['adress']='Calicut'
print(student)