def is_power_of_two(number):
    if number == 0:  # Check if the number is 0
        return False

    while number % 2 == 0 and number != 0:  # Add condition number != 0
        number = number // 2  # Use integer division to avoid ZeroDivisionError

    if number == 1:
        return True
    return False

# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False