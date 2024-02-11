def same_in_reverse(input_string):
    # Use string slicing to reverse the input string
    reversed_string = input_string[::-1]

    # Compare the original string with its reverse
    return input_string == reversed_string

# Example usage:
input_str1 = "My_Mommy"
input_str2 = "Daddy"

result1 = same_in_reverse(input_str1)  # This will return True
result2 = same_in_reverse(input_str2)  # This will return False

print(result1)
print(result2)
