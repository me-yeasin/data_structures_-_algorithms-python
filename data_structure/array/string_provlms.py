from functools import reduce

def reverse_string(text_input):
    if not text_input or type(text_input) != str or len(text_input) <= 1:
        return "invalid input"
    
    reverse_arr = []
    
    for i in range(len(text_input) - 1,-1,-1):
        reverse_arr.append(text_input[i])   

    return "".join(reverse_arr)

# Convert list to string dfrnt way
# way 1 :  

    # output_text = ""
    # for char in reverse_arr:
    #     output_text += char

# way 2 :

    # output_text = reduce(lambda x,y : x+y,reverse_arr)



new_one = reverse_string("Yeasin")
