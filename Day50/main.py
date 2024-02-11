def add_hash(input_string):
    words = input_string.split()  # Split the input string into words
    modified_string = '#'.join(words)  # Add a hash between words
    return modified_string

def add_underscore(input_string):
    modified_string = input_string.replace('#', '_')  # Replace hash with underscore
    return modified_string

def remove_underscore(input_string):
    modified_string = input_string.replace('_', '')  # Remove underscore
    return modified_string

# Example usage
result = remove_underscore(add_underscore(add_hash('Python')))
print(result)  # Output: "Python"
