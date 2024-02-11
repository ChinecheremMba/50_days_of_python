def names_starting_with_s(name_list):
    name_dict = {}  # Create an empty dictionary to store the results

    for name in name_list:
        if name.startswith("S"):
            # If the name starts with "S", add it to the dictionary or increment its count
            if name in name_dict:
                name_dict[name] += 1
            else:
                name_dict[name] = 1

    return name_dict

# Example usage:
names = ["Joseph", "Nathan", "Stephie", "Kelly", "almond", "Abundance", "stephen", "israel", "Stephen"]
result = names_starting_with_s(names)
print(result)  # Output: {"Stephie": 1, "Stephen": 2}
