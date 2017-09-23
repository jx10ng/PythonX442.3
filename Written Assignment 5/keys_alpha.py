"""Question 1: Using the keys method for dictionaries and the sort method for 
lists, write a for loop that prints the keys and corresponding values of 
a dictionary in the alphabetical order of the keys."""

import sys

def main():
    
	dictionary = {'s':'star fruit', 'b':'banana', 'o':'orange', 'd': 'dragon fruit'}

	key_list = list(dictionary.keys())
	key_list.sort()
	
	for i in range(len(key_list)):
		print ("key is " + key_list[i] + " and value is " + dictionary[key_list[i]])

if __name__ == '__main__':
    main()