def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    arr1Index = 0
    arr2Index = 0

    if not arr1 and not arr2:
        return "Invalid Input"
    
    if not arr1:
        return arr2
    
    if not arr2:
        return arr1
    

    while arr1Index < len(arr1) and arr2Index < len(arr2):
        if arr1[arr1Index] < arr2[arr2Index]:
            merged_array.append(arr1[arr1Index])
            arr1Index += 1
        else:
            merged_array.append(arr2[arr2Index])
            arr2Index += 1
    
    while arr1Index < len(arr1):
        merged_array.append(arr1[arr1Index])
        arr1Index += 1

    while arr2Index < len(arr2):
        merged_array.append(arr2[arr2Index])
        arr2Index += 1


    return merged_array

merge_sorted_arrays([1, 3, 5],[2, 4, 6])