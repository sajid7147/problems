"""Accept a string as input. Your task is to determine if the input string is a valid password or not. For a string to be a valid password, it must satisfy all the conditions given below:
(1) It should have at least 8 and at most 32 characters
(2) It should start with an uppercase or lowercase letter
(3) It should not have any of these characters: / \ = ' "
(4) It should not have spaces
It could have any character that is not mentioned in the list of characters to be avoided (points 3 and 4). Output True if the string forms a valid password and False otherwise.
"""
# Accept a string as input
password = input()

# Check if the string is a valid password
def is_valid_password(password):
    # Condition 1: Check the length
    if 8 <= len(password) <= 32:
        # Condition 2: Check the first character is an uppercase or lowercase letter
        if password[0].isalpha():
            # Condition 3: Check for forbidden characters
            forbidden_chars = {'/', '\\', '=', "'", '"'}
            if not any(char in forbidden_chars for char in password):
                # Condition 4: Check for spaces
                if ' ' not in password:
                    return True

    return False

# Output True if the string forms a valid password, and False otherwise
print(is_valid_password(password), end="")