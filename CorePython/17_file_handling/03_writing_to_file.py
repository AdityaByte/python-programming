"""
Topic: Writing to a file.
1. "w" mode:
-> This will create the file if not exists or overrides a pre-existed file.

"""

# with open("test1.txt", "w") as f:
#     f.write("test 1 is here")
#     f.seek(0)
#     f.write("T")

with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        # For each line that was in the read file write that line,
        # to the write file.
        for line in rf:
            wf.write(line)