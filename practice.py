nums=[12,34,3,66,11]

def max_value(nums):
    max_value=nums[0]
    for num in nums:
        if num > max_value:
           max_value=num
    return max_value

print( "maximum value of nums :", max_value(nums))
        
    

