def gcd(a,b):
    if(a==b):
        return a
    elif(a==1 or b==1):
        return 1
    else:
        if(a>b):
            return gcd(a-b,b)
        else:
            return gcd(a,b-a)


def fact(num):
    if(num==0 or num == 1):
        return 1
    else:
        return num * fact(num-1)

def sum(a,b):
    return a+b

def multiply(a,b):
    return a*b

print(fact(5))
print(gcd(3,1))
print(sum(3,4))
print(multiply(5,6))