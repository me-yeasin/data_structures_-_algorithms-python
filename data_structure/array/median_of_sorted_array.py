import heapq

def findMedianSortedArrays(nums1, nums2):
    # sorted marge
    sorted_arr = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2): # O(n)
        if nums1[i] < nums2[j]:
            sorted_arr.append(nums1[i])
            i += 1
        else:
            sorted_arr.append(nums2[j])
            j += 1

    # if remain elements in num1 and num2
    # note : only one loop will be executed
    while i < len(nums1): # O(n)
        sorted_arr.append(nums1[i])
        i += 1
    while j < len(nums2): # O(n)
        sorted_arr.append(nums2[j])
        j += 1

    # sorted_marged_list = list(heapq.merge(num1, num2))
    total_length = len(sorted_arr)
    if total_length % 2 == 1:
        return float(sorted_arr[total_length // 2])
    else:
        mid1 = sorted_arr[total_length // 2 - 1]
        mid2 = sorted_arr[total_length // 2]
        return float(mid1 + mid2) / 2.0


median = findMedianSortedArrays([1,2],[3,4])