"""Question 1: Suppose you want to determine whether an arbitrary text string can be converted to a number. 
Write a function that uses a try/except clause to solve this problem. 
Can you think of another way to solve this problem"""

import re

def num_convert(string): #using try and except to convert a number to an int
	try:
		int_num = int(string)
		print ('{0} is converted to an integer.'.format(string))
	except ValueError as ex:
		print ('Input cannot be converted to an integer: %s' % (ex))
	return

def other_convert(string): #using RegEx to convert a number to an int
	num_match = re.match (r'^[0-9]+$', string)

	if num_match:
		int_num = int(string)
		print ('{0} is converted to an integer.'.format(string))
	else: 
		print ('Input cannot be converted to an integer.')
	return


def main():

	my_string1 = 'one'
	num_convert(my_string1)

	my_string2 = '2'
	num_convert(my_string2)

	my_string3 = '3.14'
	other_convert(my_string3)

	my_string4 = '4'
	other_convert(my_string4)

if __name__ == '__main__':
	main()