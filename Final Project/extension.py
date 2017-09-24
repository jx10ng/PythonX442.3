
"""Question 1: A file with a name like picture.jpg is said to have an extension of "jpg"; i.e. 
the extension of a file is the part of the file after the final period in its name. 
Write a program that takes as an argument the name of a directory (folder) and then finds the extension of each file. 
Then, for each extension found, it prints the number of files with that extension and the minimum, average, and 
maximum size for files with that extension in the selected directory."""

import os

class ExtInfo:
    def __init__(self, extension):
        # Check extension existence
        if extension != '':
            self.extension = extension
        else:
            self.extension = '[empty]'

        # Create initial counters
        self.count = 0
        self.file_sizes = []
        self.min_file_size = None
        self.max_file_size = None

    def append_file_size(self, size):

        if self.count == 0:
            # If initial count, current size is new size
            self.min_file_size = size
            self.max_file_size = size
        elif size < self.min_file_size:
            # Set new min
            self.min_file_size = size
        elif size > self.max_file_size:
            # Set new max
            self.max_file_size = size

        self.count += 1
        self.file_sizes.append(size)
        # Add size to list of file_sizes

    def get_average_file_size(self):
        # Return average file sizes in list
        return sum(self.file_sizes) / self.count

    def __repr__(self):
        return ('<ExtInfo> {} - count: {}, min: {}, max: {}, avg: {}'.format(self.extension, self.count, self.min_file_size, self.max_file_size, self.get_average_file_size()))
        # For printing object 

def analyze_dir(dir_path):
    extension_map = {}
    # Create dictionary

    for root, dirs, files in os.walk(dir_path, topdown=False):
       
        # Iterate through all files in path
        for f in files:
            file_path = os.path.join(root, f)
            # Join the root path and the file name to get the full file path

            file_size = os.path.getsize(file_path)
            # Get file size

            file_name, file_ext = os.path.splitext(f)
            # os.path.splitext() split path into a base and file extension

            ext_info = extension_map.setdefault(file_ext, ExtInfo(file_ext))
            # Set keys and values to dictionary

            ext_info.append_file_size(file_size)
            # Update count, min, max,

    for ext in extension_map.values():
        print(ext)


def main():
    analyze_dir('.')
    # Current path of where script is run from

if __name__ == '__main__':
    main()

