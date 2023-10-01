student=['A','B' ,'C']
subject=['國文', '數學', '英文']

for i in range(3):
    print('輸入學生', student[i],'的成績')
    list=[student [i]]
    total=0
    for j in range(3):
        score=float(input('輸入學生'+student[i]+'的成績'+subject[j]+'的成績'))
        list.append(score)
        total=total+score
    list.append(total/3)
    print(list)