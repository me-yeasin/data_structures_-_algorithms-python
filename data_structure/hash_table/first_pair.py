# Google Question 
# Given an array = [2,5,1,2,3,5,1,2,4]
# it should return 2 because it occurs 1 time

# Given an array = [2,1,1,2,3,5,1,2,4]
# it should return 1

# Given an array = [2,3,4,5]
# it should return None

# using array
def first_pair(arr):
   checking_arr = []
   for item in arr:
       if item in checking_arr:
           return item
       else:
           checking_arr.append(item)
    
   return None

first_pair([2,5,1,2,3,5,1,2,4])


# using Hash Table
def first_pair2(arr):
    checking_hash = {}
    
    for i in range(len(arr)):
        if arr[i] in checking_hash:
            return arr[i]
        else:
            checking_hash[arr[i]] = i


result = first_pair2([2,1,1,2,3,5,1,2,4])
print(result)