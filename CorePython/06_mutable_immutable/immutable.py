# Immutability:
# Tuples are immutable in java
tup1 = ("aditya", "pawar")
tup2 = tup1

tup2[0] = "hello" # It will raise the error.
print(tup1)
print(tup2)