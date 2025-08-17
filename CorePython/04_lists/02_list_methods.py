# List methods:

nums = [1,2,3,4,5,6]

# 1. append() - Add item at last.
nums.append(7)
print(nums)

# 2. insert(index, value) - inserting an element to a specific location.
nums.insert(-1, 0) # Tricky -> insert at last index and the index index element is shifted one right.
print(nums)

# 3. extend() - If we wants to insert multiple value to a list from a list.
nums1 = [10,20,30]
nums.extend(nums1)
print(nums)

# 4. pop() - It removes the last value and return that from list.
print(nums.pop()) # last value.
print(nums) # last value is removed.

# 5. remove() - It remove the first occurance of the value that we passed.
nums.remove(3)
print(nums)

# 6. reverse() - As the name say reverse the actual list.
nums.reverse()
print(nums)

# 7. sort() - sorting list.
# This method is altering the list implace without returning a new list.
nums.sort()
print(nums)
# Reverse sorting.
nums.sort(reverse=True)
print(nums)

# 8. index() method - returns the index of the element.
print("index", nums.index(20))

# Built in functions in builtins module:

# sorted() function is used for sorting but not implace.
print(sorted(nums))

# min() - Returns minimum element.
print(min(nums))

# max() - Returns maximum element.
print(max(nums))

# sum() - Sum of all elements.
print(sum(nums))

# If we want to check a particular element in our list or not and returns a boolean value.
print(20 in nums)
print(90 in nums) # false