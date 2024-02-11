def user_name():
    # Ask the user to input their email
    email = input("Please enter your email: ")

    # Split the email address at the "@" symbol
    parts = email.split("@")
    
    # Check if the email is valid (contains exactly one "@" symbol)
    if len(parts) != 2:
        return "Invalid email format. Please enter a valid email address."

    # Extract and return the username (part before the "@")
    username = parts[0]
    return username

# Call the function and print the result
username = user_name()
print("Your username is:", username)
