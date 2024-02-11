"""Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. You can assume that the string will only contain letters.
"""

input_string = input()

# Convert the string to lowercase
lowercase_string = input_string.lower()

# Sort the string in alphabetical order
sorted_string = ''.join(sorted(lowercase_string))

# Print the sorted string to the console
print(sorted_string,end="")