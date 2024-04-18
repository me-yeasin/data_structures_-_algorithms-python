def twoSum(nums, target):

    num_range = range(len(nums))

    for i in num_range:
        for j in num_range[i + 1 : ]:
            if nums[i] + nums[j] == target:
                return [i,j]
            

    
result = twoSum([2,7,11,15],18)
print(result)
