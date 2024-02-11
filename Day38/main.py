def flat_list(nested_list):
    # Initialize an empty list to store the flattened elements
    flat_result = []

    # Define a recursive function to flatten the list
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                flatten(item)  # If the item is a list, recursively flatten it
            else:
                flat_result.append(item)  # If the item is not a list, add it to the result

    # Call the recursive function to flatten the nested list
    flatten(nested_list)

    return flat_result

# Example usage:
nested_list = [[2, 4, 5, 6]]
flat_result = flat_list(nested_list)
print(flat_result)  # This will print [2, 4, 5, 6]
