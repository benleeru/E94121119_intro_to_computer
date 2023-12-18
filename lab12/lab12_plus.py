import matplotlib.pyplot as plt
import numpy as np

# 讀完的資料會長這樣
#[301.8267195898913, 206.48068590297993, ...........139.43161572804308, 281.7900813768265, 229.67424006279856]
#[-10, -9, ................. 9, 10]
y_list=[]
x_list=[]
with open('OddExperiment.txt', 'r') as f:
    count=0
    for line in f :
        a=line 
        if count !=0 :
            a_split=a.split()
            y_list.append( float(a_split[0]) )
            x_list.append( float(a_split[1]) )
        count+=1
        #for i in range(1,)
print (y_list)
print (x_list)


#將資料點利用plt.scatter繪製出來
y = y_list
x = x_list
plt.scatter(x,y)
plt.title('oddExperiment Data')
#plt.xlabel('x')
#plt.ylabel('y')


# 擬合一階多項式（線性擬合）
coefficients_linear = np.polyfit(x, y, 1)
first_degree_polynomial = np.poly1d(coefficients_linear)

# 擬合二階多項式
coefficients_quadratic = np.polyfit(x, y, 2)
second_degree_polynomial = np.poly1d(coefficients_quadratic)

# 計算一階多項式和二階多項式的最小平方法誤差
mse_linear = np.mean((first_degree_polynomial(x) - y)**2)
mse_quadratic = np.mean((second_degree_polynomial(x) - y)**2)

# 繪製資料點和擬合多項式
plt.scatter(x, y, label='Data',  color='blue')
plt.plot(x, first_degree_polynomial(x), label=f'Fit of degree 1, LSE = {mse_linear:.5f})',  color='red')
plt.plot(x, second_degree_polynomial(x), label=f'Fit of degree 2, LSE = {mse_quadratic:.5f})',  color='purple')

plt.legend()

plt.savefig('lab12_plus.png')

plt.show()