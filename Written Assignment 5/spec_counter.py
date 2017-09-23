"""Question 4: Modify the program written in question 3 so that it doesn't count 
characters on any line that begins with a pound sign (#)."""

import sys

def main():
    
	my_files = open("newfile", 'r') #open file
	char_count = 0

	while True: 
		line_text = my_files.readline() #read each line
		line_char = len(line_text)

		if line_text != "" and (char_count < 1000): #checks if not at end of file and character count < 1000
			if not line_text.startswith('#'): #checks if line starts with #
				char_count += line_char #add character count of line to global character counter
			else: 
				continue
		else:
			break

	print(char_count)
	my_files.close()

if __name__ == '__main__':
    main()

