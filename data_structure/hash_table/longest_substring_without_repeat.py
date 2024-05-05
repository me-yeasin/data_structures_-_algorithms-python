def lengthOfLongestSubstring(s : str) -> int:
    n = len(s)
    max_length = 0
    char_dict = {}
    l = 0

    for r in range(n):
        if s[r] not in char_dict or char_dict[s[r]] < l:
            char_dict[s[r]] = r
            max_length =max(max_length, r - l + 1)
        else:
            l = char_dict[s[r]] + 1
            char_dict[s[r]] = r
    
    return max_length

result = lengthOfLongestSubstring("tmmzuxt")
print(result)