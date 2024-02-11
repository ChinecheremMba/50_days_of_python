def string_range(num):
    if num < 0:
        return ""
    
    return ".".join(map(str, range(num)))

# Example usage:
result = string_range(6)
print(result)  # Output: "0.1.2.3.4.5"
