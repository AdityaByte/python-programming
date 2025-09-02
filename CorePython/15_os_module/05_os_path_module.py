import os.path

# 1. Joining the paths: os.path.join(args)
path = os.path.join("Folder1", "Folder2", "File.pdf")
print(path)

# 2. If we want the filename and we have a path: os.path.basename(path)
# we have a path
filename = os.path.basename(path)
print(filename) # File.pdf

# 3. If we want the dirname of the path then: os.path.dirname(path)
dirname = os.path.dirname(path)
print(dirname) # Folder1\Folder2

# 4. If we want the both of them the dirname and the filename too: os.path.split(path)
dir_file = os.path.split(path)
print(dir_file) # ('Folder1\\Folder2', 'File.pdf')

# 5. If we want to check the existance of a path: os.path.exists(path)
exists = os.path.exists(path) # False not exists.
print(exists)

# 6. Checking the path points to a dir or a file: os.path.isfile() and os.path.isdir()
isDir = os.path.isdir(path)
print(isDir)
isFile = os.path.isfile(path)
print(isFile)

# 7. If we want to split up the file extension then: os.path.splitext(path)
extension = os.path.splitext(path)
print(extension) # ('Folder1\\Folder2\\File', '.pdf')