#A function that checks for duplicates in a list.

def check_duplicate(input_list):
    seen = set()
    duplicates = []

    for item in input_list:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)

    if duplicates:
        return duplicates
    else:
        return None

# Example usage:
my_list = ["Emeka", "obinna", "chukwudi", "ikenna", "ikechukwu", "chukwudi"]
result = check_duplicate(my_list)
if result:
    print("Duplicates found:", result)
else:
    print("No duplicates found.")
