# Define a dictionary
dict_1 = {'a': 1, 'b': 2, 'c': 3}


# Create an empty dictionary
dict_as_fstrings = {}

# Iterate over the dictionaries
for key, value in dict_1.items():
    dict_as_fstrings[key] = f'the value is {value}'


print(dict_as_fstrings)