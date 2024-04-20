# Question Link 
# https://leetcode.com/problems/roman-to-integer/description/



def roman_to_integer(chars):

    roman_table = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    
    result = 0
    for i in range(len(chars)):
        if i < len(chars) - 1 and roman_table[chars[i]] < roman_table[chars[i + 1]]:
            result -= roman_table[chars[i]]
        else:
            result += roman_table[chars[i]]

new_result = roman_to_integer("MCMXCIV")
print(new_result)