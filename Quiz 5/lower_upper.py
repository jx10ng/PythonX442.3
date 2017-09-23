"""Question 1: Write a regular expression that will match strings that are either all lower case or all upper case."""

import re

def matching (string):
	if (re.match (r'^[a-z]{2,}$', string)) or (re.match (r'^[A-Z]{2,}$', string)):
		print ('{0} has all lowercase or uppercase'.format(string))
	else:
		print ('{0} is not either all lowercase or uppercase'.format(string))
	return

def main():
	matching('AM')

	matching('pm')

	matching('parrot')

	matching('Next')

if __name__ == '__main__':
	main()