
#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values


# Create the dict
my_dict = {}
 
# populate it
for i in range(97, 97 + 26):
    # Map character to ascii value
    my_dict[chr(i)] = i
 
# Print the populated dict
print(my_dict)