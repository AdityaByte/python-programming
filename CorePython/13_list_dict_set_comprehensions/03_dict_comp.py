# Set Comprehensions:

names = ["Tony", "Bruce", "Steve", "Natasha", "Peter"]
heros = ["Ironman", "Hulk", "CaptainAmerica", "BlackWidow", "Spiderman"]

# We can simply do this.
print(dict(zip(names, heros)))

# Iterative method.
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero

print(my_dict)

# Dictionary comprehensions
my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

# There is more flexibility with compresion although the first one do the same task.
# We don't want peter to the dictionary so.
my_dict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(my_dict)
