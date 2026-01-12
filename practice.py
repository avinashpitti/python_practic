# write a function that takes a list of numbers and returns the largest

nums=[2,57,124,555,33,20]

    
def largest_nums(nums):
    large=nums[0]
    for i in nums:
        if i > large:
            large=i
    return large

print(largest_nums(nums))
