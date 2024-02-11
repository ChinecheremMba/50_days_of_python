def count_dots(input_string):
    # Initialize a variable to count the dots
    dot_count = 0

    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is a dot
        if char == '.':
            dot_count += 1

    return dot_count

# Example usage:
string1 = "a.m.a.z.i.n.g"
string2 = "a.w.e.s.o.m.a"
dots1 = count_dots(string1)
dots2 = count_dots(string2)
print("Dots in string1:", dots1)  # This will print 6
print("Dots in string2:", dots2)  # This will print 6
