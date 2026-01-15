nums = [1, 2, 3, 4, 6]

def count_even(nums):
    count=0
    for num in nums:
        if num % 2 ==0:
            count+=1
    return count

print(count_even(nums))
    
