a=input('please input a number')
if a%2==0 :
    print('this is even number')
else :
    print('this is an odd number')
b=input('please input your student ID first character')
c=input('please input your student ID last 8 numbers')
if int(c)%2==0 :
    print('your studdent ID is even')
else :
    print('your studdent ID is odd')
print('your student Id is '+b+c)