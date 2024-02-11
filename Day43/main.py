# Function to add a hash (#) between words
def add_hash(input_string):
    words = input_string.split()
    return '#'.join(words)

# Function to replace hash (#) with an underscore (_)
def add_underscore(input_string):
    return input_string.replace('#', '_')

# Function to remove underscores
def remove_underscore(input_string):
    return input_string.replace('_', '')

# Example usage:
input_str = 'Python'
result = remove_underscore(add_underscore(add_hash(input_str)))
print(result)  # This will print "Python"
