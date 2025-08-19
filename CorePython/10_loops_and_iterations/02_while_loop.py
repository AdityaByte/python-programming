# While loop:
# While loop is used when we don't know the termination condition the loop runs till the condition evaluates to true.

# while True:
#     print("Hello world") # this will run infinite times.

# Some keyword that came across with looping statements
# 1. break 2. continue

i = 0

while i < 10:
    if i == 5:
        i += 1 # This condition  is necessary otherwise we'll stuck into the deadlock.
        continue # Skipping that iterations.
    elif i == 8:
        break # Exiting from the loop.
    print(i)
    i += 1