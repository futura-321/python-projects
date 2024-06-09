# file=open(r"C:\Users\allama thabsheer\OneDrive\Desktop\macbeth (2).txt",'r')
# print(file.read())
# print(file.read(100))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# file=open(r"C:\Users\allama thabsheer\OneDrive\Desktop\macbeth (2).txt",'a')
# print(file.write("hello world"))
# file=open(r"C:\Users\allama thabsheer\OneDrive\Desktop\macbeth (2).txt",'r')
# print(file.read())
# file.close()



import os

#os.mkdir("new directory")# creating new directory
print('string format:',os.getcwd())
print('byte format:',os.getcwdb())
# print("rename format:",os.rename("new directory","hello"))


print("The files in cwd are:",os.listdir(os.getcwd()))
cwd='k:/'
print(os.path.isdir(cwd))
other='k:/'

import datetime as dt

print(os.path.isdir(other))

print("last access time:",os.path.getatime(os.getcwd()))# last acces time
print("last modification time:",os.path.getmtime(os.getcwd()))#last modification time

acess_time=dt.datetime.formatstamp(os.path.getatime(os.getcwd())).strftime('%Y-%m-%d-%I-%M-%p')
modification_time=dt.datetime.formatstamp(os.path.getatime(os.getcwd())).strftime('%Y-%m-%d-%I-%M-%p')
print("last acess time:",acess_time)
print("last modification time:",acess_time)


