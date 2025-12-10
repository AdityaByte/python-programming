# In this we are working with binary coded files.
# The text files are UTF-8 coded.

# Task: We are copying an image file.

# in the mode rb- read in binary and wb- write in binary.
with open("norway.jpg", "rb") as rf:
    with open("norway_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)

    print("Image copied successfully")