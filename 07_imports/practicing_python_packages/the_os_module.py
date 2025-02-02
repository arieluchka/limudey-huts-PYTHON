import os


# Example: Getting the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Example: Changing the current working directory
os.chdir('.\\07_imports\\practicing_python_packages')
print("Changed Directory:", os.getcwd())

# Example: Listing files and directories in the current directory
files_and_directories = os.listdir('.')
print("Files and Directories:", files_and_directories)

# Example: Creating a new directory
# os.mkdir('new_directory')
# print("New Directory Created")

# Example: Removing a directory
# os.rmdir('new_directory')
# print("Directory Removed")

# Example: Renaming a file or directory
# os.rename('old_name', 'new_name')
# print("Renamed")

# Example: Removing a file
# os.remove('file_name')
# print("File Removed")

# The `os` module also provides methods to interact with the environment variables.

# Example: Getting the value of an environment variable
path = os.getenv('PATH')
print("PATH:", path)

# Example: Setting the value of an environment variable
# os.environ['MY_VARIABLE'] = 'my_value'
# print("Environment Variable Set")

# The `os` module provides methods to work with file paths.

# Example: Joining paths
path = os.path.join('folder', 'subfolder', 'file.txt')
print("Joined Path:", path)

# Example: Splitting a path
folder, file = os.path.split('/path/to/file.txt')
print("Folder:", folder)
print("File:", file)

# Example: Checking if a path exists
exists = os.path.exists('/path/to/file.txt')
print("Path Exists:", exists)

# Example: Checking if a path is a file
is_file = os.path.isfile('/path/to/file.txt')
print("Is File:", is_file)



# Example: Getting the name of the operating system
os_name = os.name
print("OS Name:", os_name)
