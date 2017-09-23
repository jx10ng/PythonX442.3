"""Question 3: Write a loop that reads each line of a file. It should count the number of 
characters in each line and keep track of the total number of characters read. 
Once you have a total of 1,000 or more characters, break from the loop. 
(You can use a break statement to do this.)"""

import sys

def main():
    
	my_files = open("newfile", 'r') #open file
	char_count = 0

	while True: 
		line_text = my_files.readline() #read each line
		line_char = len(line_text)

		if line_text != "" and char_count < 1000: #only proceed if not at end of lines and less than 1000 characters
			char_count += line_char #add character count of line to global character counter
		else: 
			break

	print(char_count)
	my_files.close()

if __name__ == '__main__':
    main()

