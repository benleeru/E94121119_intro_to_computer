import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15,8))
fig.add_subplot(2, 2, 1)
plt.subplot(2, 2, 1)
with open('Temperature.txt', 'r') as f:
    temp_list = []
    for line in f: #for迴圈跑9次，每一年畫一條線共9年
        #例如2013, 17.5, 20.4, 22.5, 23.9, 27.3, 29.5, 29.4, 28.9, 28.6, 25.7, 22.8, 18.0
        #和同學討論後發現應該要用二維串列(串列套串列)比較方便，我的方法比較麻煩
        a=line
        a_stripped = a.strip()
        a_remove_year=a_stripped.split(',')
        #把第一個"Tainan"移除
        a_remove_year.remove( a_remove_year[0] ) #把每一行資料前面的年分移除
        if a_remove_year!=[]:#把第一個"台南"移除
            for i in range(12) :
                int_a_remove_year = float( a_remove_year[i] ) #float(不是integer!)
                temp_list.append ( int_a_remove_year  )
        #已把年份移除，從第一個數開始找即可，不需要從第二個數取到最後一個組成陣列

#繪製plot 折線圖
                
list_year = [] #每一條線都代表不同年份
for i in range(9):
    list_year.append( i+2013 )

plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')

for i in range(9) :
    x = np.linspace(1, 12, 12)
    
    y=[]
    for n in range(12):
        y.append( temp_list[12*i+n] )
        #如同將資料儲存在一個行列式的模型，n代表每年的一到十二月(n=0~11)；i代表不同的西元年分(i=0~8)
    plt.plot(x, y, label=list_year[i] )

    plt.legend()

#print(temp_list)

#分別計算每個月份每年的氣溫平均值

plt.subplot(2, 2, 2)
avg_y=[]
for i in range(12):
    avg_y.append(0) #avg_y=[0,0,0,0,0,0,0,0,0,0,0,0]

for n in range(12):
    for i in range(9) :
        avg_y[n]=avg_y[n]+(temp_list[12*i+n]/9)
#print(f'每個月溫度的平均的串列{avg_y}')
#'avg_y'是每個月份每年的氣溫平均值(共12項的串列)
x = np.linspace(1, 12, 12)
plt.plot(x, avg_y)

plt.scatter(x, avg_y, color='red', s=50)#每個點紅色加深

for j in range(len(avg_y)):
    plt.text(j, avg_y[j],str(round(avg_y[j],2)))

plt.ylabel('Temperature in Degree C')
plt.legend()

print(avg_y)
mean_value=0
for k in range(len(avg_y)):
    mean_value=mean_value+avg_y[k]/12
    
plt.axhline(y=mean_value, color='red', linestyle='--', label="Mean Of 9 Years" )

plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
# 在圖上標示文字
plt.text(max(x), mean_value, f'{mean_value:.2f}', color='red', verticalalignment='bottom', horizontalalignment='left')
plt.legend()

plt.show() 

fig.savefig('lab12_03.png')

