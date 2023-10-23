def per(numlist):
    for i in range(len(numlist)):
        a=numlist[i]
        for i in range(len(numlist)):
            b=numlist[i]
            
            for i in range(len(numlist)): 
                c=numlist[i]
                 
                for i in range(len(numlist)):
                    d=numlist[i]
                    
                    if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                        anslist.append(a+b+c+d)   

    return anslist
    
anslist=[]   
stringnumber = str(1234)
numlist = list(stringnumber)
int_numlist = [int(num) for num in numlist]


per(numlist)
print(per(numlist))   