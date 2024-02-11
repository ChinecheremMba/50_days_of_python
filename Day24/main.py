# A function with two parameters, a and b. 


def only_float(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0

# Example usage:
result = only_float(12.1, 23)
print(result)  # Output: 1
