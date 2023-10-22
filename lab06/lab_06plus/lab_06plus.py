import random

def function1(n, permutation):
    if n == 24:
        permutation.sort()
        return permutation  # 找到所有值了，可以結束程式
    else:
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        c = random.randint(1, 4)
        d = random.randint(1, 4)
        if a != b and a != c and a != d and b != c and b != d and c != d:
            ans = 1000 * a + 100 * b + 10 * c + d
            if ans not in permutation:
                permutation.append(ans)
                n += 1
            return function1(n, permutation)
        else:
            return function1(n, permutation)

n = 0
permutation = []
result = function1(n, permutation)
print(result)