nums=[12,34,3,66,11]

def min_value(nums):
    min_value=nums[0]
    for num in nums :
        if num < min_value :
            min_value = num
    return min_value

print(min_value(nums))

    

