def hide_password():
    # Get the password input from the user
    password = input("Enter your password: ")

    # Calculate the length of the password
    password_length = len(password)

    # Create a hidden password with asterisks
    hidden_password = '*' * password_length

    # Return the hidden password and the password length
    return hidden_password, password_length

# Example usage:
hidden_pw, pw_length = hide_password()
print("Hidden Password:", hidden_pw)
print("Password Length:", pw_length)
