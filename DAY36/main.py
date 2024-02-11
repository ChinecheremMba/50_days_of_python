def equal_strings(str1, str2):
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False

    # Sort and compare the characters in both strings
    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))

    # Return True if the sorted strings are equal (i.e., they contain the same characters)
    return sorted_str1 == sorted_str2

# Example usage:
string1 = "Great"
string2 = "Glory"
result = equal_strings(string1, string2)
print(result)  # This will print True since "Great" and "Glory" are anagrams of each other
