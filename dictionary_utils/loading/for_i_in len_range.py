# Creating a dictionary using a for loop with a single key set and value pair set
my_dict = {}

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York","Bob",20,"Chicago","Dave",25,"Los Angeles"]

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)



#when values
chunked_values = [values[i:i+len(keys)] for i in range(0, len(values), len(keys))]

my_dict.

# Create a list of dictionaries for each chunk of values
result = [dict(zip(keys, chunk)) for chunk in chunked_values]

print(result)

