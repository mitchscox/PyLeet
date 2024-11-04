import pickle

# Load a dictionary from a file
with open('my_dict.pkl', 'rb') as f:
    my_dict = pickle.load(f)

print(my_dict)