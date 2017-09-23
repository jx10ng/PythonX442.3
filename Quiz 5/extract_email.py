"""Question 3: Construct a regular expression that will extract the 
names of URLs embedded in a string"""

import re

def email_extract(string):
	print (re.findall(r'\w+@\w+\.\w+', string))	

def main():
	email_extract('this is my email: myname@yahoo.com! Do you like it?')


if __name__ == '__main__':
	main()