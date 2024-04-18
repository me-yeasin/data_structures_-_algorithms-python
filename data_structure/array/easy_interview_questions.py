# Find the index
def find_index(x):
    array_of_integers = [1, 3, 5, 7, 9]

    if x not in array_of_integers:
        return -1
    
    return array_of_integers.index(x)
    
find_index(7)


# Get the Maximum Product

def maximum_product(arr):
    
    if type(arr) is not list:
        return "Please Enter a List of numbers"
    if not arr:
        return "Please Enter a valid Array"
    

    negative_num_one = 0
    negative_num_two = 0
    positive_num = 0


    for num in arr:
        if num < negative_num_one:
            negative_num_two  = negative_num_one
            negative_num_one = num
        elif num < negative_num_two:
            negative_num_two = num

        if num > positive_num:
            positive_num = num
    
    return (negative_num_one * negative_num_two * positive_num)


result = maximum_product([-10, -3, 5, 6, -2])

print(result)