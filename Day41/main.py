def sum_list(nested_list):
    total = 0  # Initialize the total sum

    # Define a recursive function to calculate the sum
    def recursive_sum(nested):
        nonlocal total  # Access the total variable defined in the outer function

        for item in nested:
            if isinstance(item, list):
                recursive_sum(item)  # If the item is a list, recursively sum its elements
            elif isinstance(item, int):
                total += item  # If the item is an integer, add it to the total

    # Call the recursive function to calculate the sum
    recursive_sum(nested_list)

    return total

# Example usage:
nested_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
result = sum_list(nested_list)
print(result)  # This will print 33

