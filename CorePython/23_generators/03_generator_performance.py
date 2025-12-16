"""
This file demonstrates how generators reduce memory usage
using the tracemalloc module.
"""

import tracemalloc
import time
import random

names = ['aditya', 'abhi', 'yeshank', 'sourabh', 'arjun', 'soham']
majors = ['Math', 'Engineering', 'CompSci', 'AstroPhysics', 'Arts']


def people_list(num_people):
    result = []
    for i in range(num_people):
        result.append({
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        })
    return result

# Now seeing how the generator function optimized the performance.
def people_generator(num_people):
    for i in range(num_people):
        yield {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

# Start tracing memory
tracemalloc.start()

t1 = time.perf_counter()
before = tracemalloc.get_traced_memory()[0]

# people = people_list(1000000) # For one million records.
people = people_generator(10000)
for data in people:
    print(data)

after, peak = tracemalloc.get_traced_memory()
t2 = time.perf_counter()

print(f"Memory before: {before / 1024:.2f} KB")
print(f"Memory after : {after / 1024:.2f} KB")
print(f"Peak memory : {peak / 1024:.2f} KB")
print(f"Total time  : {t2 - t1:.6f} seconds")

tracemalloc.stop()


"""
Conclusion:
When you run both the cases without generator and with genrator:
Generator optimized the memory before it generator value on the fly didn't store all the data
to the memory.
"""