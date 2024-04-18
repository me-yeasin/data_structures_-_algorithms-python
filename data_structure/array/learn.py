def two_sum(nums, target):
    index_one = 0
    for n1 in nums: # 2
        index_two = index_one + 1
        for n2 in nums[index_two : ]: # 7
            if n1 + n2 == target:
                return [index_one, index_two]
            index_two += 1
        index_one += 1
    
result = two_sum([2,7,11,15],18)
print(result)