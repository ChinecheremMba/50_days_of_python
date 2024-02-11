def get_unique_numbers(nested_list):
    unique_numbers = set()  # Initialize an empty set to store unique numbers
    for sublist in nested_list:
        for num in sublist:
            if isinstance(num, int):
                unique_numbers.add(num)  # Add the number to the set to ensure uniqueness

    unique_numbers_list = list(unique_numbers)  # Convert the set to a list

    return unique_numbers_list

# Example usage:
nested_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
unique_numbers_list = get_unique_numbers(nested_list)
print(unique_numbers_list)  # This will print [2, 3, 4, 5, 6]