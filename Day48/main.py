def make_tuples(list_a, list_b):
    # Check if the input lists are of equal length
    if len(list_a) != len(list_b):
        raise ValueError("Input lists must be of equal length")
    
    # Combine the lists into a list of tuples
    tuples_list = [(list_a[i], list_b[i]) for i in range(len(list_a))]
    return tuples_list

# Example usage
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

try:
    tuples_list = make_tuples(list_a, list_b)
    print(tuples_list)  # Output: [(1, 5), (2, 6), (3, 7), (4, 8)]
except ValueError as e:
    print(e)  # Output: "Input lists must be of equal length"
