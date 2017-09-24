"""Questions 2: Write a script that will list and count all of the images in a given HTML web page/file. You can assume that: 
- Each image file is enclosed with the tag <img and ends with >
- The HTML page/file is syntactically correct"""

import re

def list_images(filepath):
    f = open(filepath, 'r')

    # Read the entire file into memory since we can't guarantee that the <img>
    # tags are never split into multiple lines.
    source = f.read()

    # Pattern to match <img> tags and only grab the image path.
    pattern = r'<img\s+[^>]*src=\"([^\"]*)\"[^>]*>'
    # re.findall() returns a list of matched strings.
    matches = re.findall(pattern, source)

    # Print number of matched strings.
    print('Matched {} images:'.format(len(matches)))
    
    # Print matches.
    for m in matches:
        print(m)


def main():
    list_images('test.html')


if __name__ == '__main__':
    main()