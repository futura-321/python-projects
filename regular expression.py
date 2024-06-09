import re
txt="The rain in spain"
x=re.search("^The.*spain$",txt)
if x:
    print("yes we have a match")
else:
    print("no match")

txt="The rain in spain"
x=re.findall("ai",txt)
print(x)

txt="The rain in spain"
#check if the"portugal" is in the string:
x=re.findall("portugal",txt)
print(x)

txt="the rain in spain"
x=re.search("\s",txt)
print(x.start())


txt="the rain in spain"
x=re.split("n",txt)
print(x)


txt="the rain in spain"#replacing elements
x=re.sub("\s","9",txt)
print(x)
