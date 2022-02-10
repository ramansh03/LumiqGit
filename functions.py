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