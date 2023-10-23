def per(numlist, i , tmp , n): 
    if len(tmp)==4:
        if tmp[0]!=tmp[1] and tmp[0]!=tmp[2] and tmp[0]!=tmp[3] and tmp[1]!=tmp[2] and tmp[1]!=tmp[3] and tmp[2]!=tmp[3]:
            anslist.append(tmp[0]+tmp[1]+tmp[2]+tmp[3]) 
            if len(anslist)==24:
                i=0
                return anslist
            else:
                i=0
                return per(numlist, i , tmp)
        else:
            tmp=[]
            return per(numlist, i , tmp)
    else: #想要照順序排出1234的組合但是做不出來...這次作業花了超過10小時還是做不出答案
        
        #while i<=4 :
        #if len(tmp)==0
            #tmp.append(numlist[a1])
        #if len(tmp)==0
            #tmp.append(numlist[a2])
            #a2+=1
        #if len(tmp)==0
            #tmp.append(numlist[a3])
            #a3+=1
        #if len(tmp)==0
            #tmp.append(numlist[a4])
            #a4+=1
            
        #tmp.append(numlist[i])
        #i+=1
        
        
        #for i in range(len(numlist)):
            #tmp.append(numlist[i])
            #i+=1
            #return per(numlist, i , tmp)
tmp=[]
i=0
anslist=[]   
stringnumber = str(1234)
numlist = list(stringnumber)
int_numlist = [int(num) for num in numlist]

per(numlist, i , tmp)
print(per(numlist))   


