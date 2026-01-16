nums = [129, 245, 113, 99, 231]

def min_value(nums):
    min_val=nums[0]
    for num in nums:
        if num < min_val:
            min_val=num
    return min_val
print(min_value(nums))