dict0={}
key1=input('Enter keys: ') #輸入: index
value1_temp=input('Enter values: ') #輸入:　國文, 英文, 數學, 自然, 社會
value1=value1_temp.split(', ')
dict0[key1]=value1
#print(dict0) :　{'index': ['國文', '英文', '數學', '自然', '社會']}
keyA=input('Enter keys: ') #輸入: StuA
valueA_temp=input('Enter values: ') #輸入:　50, 60, 70, 80, 90
valueA=valueA_temp.split(', ')
dict0[keyA]=valueA

keyB=input('Enter keys: ') #輸入: StuB
valueB_temp=input('Enter values: ') #輸入:　57, 86, 73, 82, 43
valueB=valueB_temp.split(', ')
dict0[keyB]=valueB

keyC=input('Enter keys: ') #輸入: StuC
valueC_temp=input('Enter values: ') #輸入:　97, 96, 86, 97, 83
valueC=valueC_temp.split(', ')
dict0[keyC]=valueC

print(dict0)
