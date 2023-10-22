def gcd(a,b):
    if a==0 or b==0:
        return 'NO gcd exist'
    else:
        smallnum=min(a,b)
        bignum=max(a,b)
        if bignum%smallnum==0 and smallnum==1:
            print(x , '與' ,y ,'互質' )
            return 0
        elif bignum % smallnum == 0 and smallnum != 1:
            return smallnum
        else:
            return gcd(bignum%smallnum,smallnum)
    
a=int(input('give an integer'))
x=a
b=int(input('give an integer'))
y=b
result=gcd(a,b)
print(result)
#ans1 = gcd(80, 20)
#ans2 = gcd(10, 0)
#ans3 = gcd(19, 20)