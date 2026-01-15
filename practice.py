nums = [12, 245, 3, 99, 231]

def max_value(nums):
    max_value=nums[0]
    for num in nums:
        if num > max_value :
            max_value = num

    return max_value

print(max_value(nums))
