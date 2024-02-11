def zeroed_code(numbers):
    # Check if the input list is empty or contains only one element
    if len(numbers) <= 1:
        return numbers

    # Zero the first and last elements of the list
    numbers[0] = 0
    numbers[-1] = 0

    return numbers

# Example usage:
input_list = [2, 5, 7, 8, 9]
result = zeroed_code(input_list)
print(result)  # Output will be [0, 5, 7, 8, 0]
