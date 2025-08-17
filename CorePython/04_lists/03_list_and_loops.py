# Looping through list elements.

courses = ["Art", "Science", "Maths", "Commerce"]

# Here we go through each and every element and prints that.
for course in courses:
    print(course)

# If we want index too.
# enumerate(iterable) function.
for index, course in enumerate(courses, start=1):
    print(index, course)

# str.join() method: if we want to join the list item through a string.
course_str = ", ".join(courses)
print(course_str)

# str.split(delimetter): split value based on the delimetter and returns a list.
new_list = course_str.split(", ")
print(new_list)