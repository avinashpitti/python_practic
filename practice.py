# write a function that takes a list of numbers and returns the smallest

nums=[9,57,124,555,3,20]

def smallest_num(nums):
    small=nums[0]

    for i in nums:
        if i < small:
            small=i

    return small
print(smallest_num(nums))

    
