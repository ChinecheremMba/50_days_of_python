def multiply_words(input_string):
    words = input_string.split()  # Split the input string into words
    result = 1  # Initialize the result to 1

    for word in words:
        # Check if the word contains any uppercase letters
        if not any(char.isupper() for char in word):
            result *= len(word)  # Multiply the result by the length of the lowercase word

    return result

# Example usage:
s1 = "love live and laugh"
s2 = "Hate war love Peace"

result1 = multiply_words(s1)  # This will return 240
result2 = multiply_words(s2)  # This will return 12

print(result1)
print(result2)
