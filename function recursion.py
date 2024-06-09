def fact(num):
    if num<=1:
        return 1
    else:
        return num*(fact(num-1))
print(fact(5))

def list(num1):
    if len(num1)==1:
        return num1[0]
    else:
        num1[0]+fact(num1(0))

