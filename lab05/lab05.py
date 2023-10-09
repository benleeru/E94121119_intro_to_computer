dict0={'index':['國文','英文','數學','自然','社會'],
       'StuA':[50,60,70,80,90],
       'StuB':[57,86,73,82,43],
       'StuC':[97,96,86,97,83]}
key1=list(dict0.keys())
value1=list(dict0.values())
n=1
while n<=3:
       print(key1[n],'的平均成績為',sum(value1[n])/len(value1[n]))
       n+=1
sub=0
num=0
Stu=1
sum=0
while sub<=4:
       while Stu <=3:
              sum=sum+value1[Stu][num]
              Stu+=1
       print(value1[0][sub], '科的平均成績為', sum/3)
       Stu=1
       num+=1
       sum=0
       sub+=1