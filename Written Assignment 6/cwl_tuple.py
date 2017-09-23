"""Quesiton 1: Write a function that accepts the name of a file and returns a tuple containing 
the number of lines, words, and characters that are in the file. 
(Hint: Use the split function of the string module to help you count the words in the file.) """

def count(filename):
	myfile = open(filename, 'r')
	lines = myfile.read().split("\n") #split lines
	line_count = len(lines) #line count
	word_count = 0
	char_count = 0

	for line in lines:
		words = line.split() #split words
		word_count += len(words) #word count
		char_count += len(line) #character count

	print (line_count, word_count, char_count)
	return (line_count, word_count, char_count)

def main():
    count('newfile')

if __name__ == '__main__':
    main()
