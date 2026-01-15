numbers=[12,34,3,66,11]

def second_largest(nums):
    largest=nums[0]
    second = None

    for num in nums :
        if num > largest :
            second = largest
            largest=num

        elif num != largest and (second is None or num > second):
            second = num
    return second

print(second_largest(numbers))
    

