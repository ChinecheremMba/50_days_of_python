import os

def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)  # Create the new directory if it doesn't exist

    # Create the new file inside of the new directory
    os.chdir(directory)  # Change the working directory to the new directory
    with open(filename, 'w') as file:
        pass

    # Return the list of files in the new directory
    return os.listdir()  # List the files in the current directory

print(new_directory("PythonPrograms", "script.py"))
