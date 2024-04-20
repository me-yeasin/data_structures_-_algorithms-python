#remove the target element from list
# [0,1,2,2,3,0,4,2]
# target = 2
# return the correct length of the array
# this case its 5


def remove_element(nums,target):
    
    index = 0
    
    for i in range(len(nums)):
        
        if nums[i] != target:
            nums[index] = nums[i]
            index += 1
    
    return index


remove_element([0,1,2,2,3,0,4,2],2)