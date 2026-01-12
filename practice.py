# write a function that takes a list of numbers and returns the second largest

nums=[112,57,124,555,33,20]


def min_max(nums):
    large=nums[0]
    small=nums[0]
    for i in nums:
        if i > large :
            large=i
        if i < small :
            small=i
    return large,small
print(min_max(nums))