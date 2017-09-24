"""Question 1: Using os.walk, write a script that will print the filenames of zero length files. 
It should also print the count of zero length files."""

import os

def empty_files(path):
    for root, dirs, files in os.walk(path, topdown=False):
        # Iterate through all the files in 'path'
        for f in files:
            # Join the root path and the file name to get the full file path
            file_path = os.path.join(root, f)

            if not os.path.getsize(file_path):
                print(file_path)


def main():
    empty_files('.')  # Current path of where this script is run from


if __name__ == '__main__':
    main()
