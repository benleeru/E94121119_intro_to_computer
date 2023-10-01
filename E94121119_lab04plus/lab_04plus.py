nums = [3, 2, 2, 3, 6, 5, 4, 3, 2, 1]
print('要刪除的數字是3')
i=0
while i<len(nums):
    if nums[i]==3:
        nums.remove(3)
    else:
        i+=1
print(len(nums))
print(nums)