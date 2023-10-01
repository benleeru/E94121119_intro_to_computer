nums = [3, 2, 2, 3, 6, 5, 3, 2, 1]
a=int(input('要刪除的數字是:'))
i=0
while i<len(nums):
    if nums[i]==a:
        nums.remove(a)
    else:
        i+=1
print(len(nums))
print(nums)