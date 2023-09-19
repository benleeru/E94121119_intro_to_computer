a = int(input('請輸入第一邊的長度：'))
b = int(input('請輸入第二邊的長度：'))
c = int(input('請輸入第三邊的長度：'))

if (a == b == c):
    print('是等邊三角形')
elif (a + b <= c or a + c <= b or b + c <= a):
    print('無法構成合法的三角形')
elif (a == b or a == c or b == c):
    print('是等腰三角形')
else:
    print('是一般的三角形')