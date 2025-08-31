# Sorting Dictionaries:

# Note: Understand 'key' as the function by which the each value would pass and after that they being sorted on the basis
# of that key.

my_dict_list = [{"name": "aditya"}, {"name": "yeshank"}, {"name": "adi"}]
# Now the task is we have to sort them in descending order based on the length of the actual name ok.

def sorting_logic(data):
    return len(data["name"])

# The key function would pass each value one by one and sort them on the basis of the key.
sorted_data = sorted(my_dict_list, key=sorting_logic, reverse=True)
print(f"Sorted Data:\t{sorted_data}")