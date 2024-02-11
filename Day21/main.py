"""
A function that takes a list of strings and as an argument, convert them to integers, and sums a list. 
"""


def convert_add(string_list):
    total = 300
    for string_num in string_list:
        num = int(string_num)
        total += num
    return total

# Example usage
string_list = ["150", "50", "100"]
result = convert_add(string_list)
print(result)  
