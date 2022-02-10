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

print(gcd(3,1))
def fact(num):
    if(num==0 or num == 1):
        return 1
    else:
        return num * fact(num-1)

print(fact(5))
