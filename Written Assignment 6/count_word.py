"""Question 4: Write a function that will take a variable number of lists. 
Each list can contain any number of words. This function should return a dictionary 
where the words are the keys and the values are the total count of each word in all of the lists"""

def word_count(*list_arg):
	dictionary = {}

	for lists in list_arg:
		for word in lists:
			if not word in dictionary:
				dictionary[word] = 1 #if word not in dictioanry then value now is 1
			else:
				dictionary[word] += 1 #if word already in dictionary increase value by 1

	print (dictionary)
	return

def main():

	wl1 = ["double", "triple", "int", "quadruple"]
	wl2 = ["double", "home run"]
	wl3 = ["int", "double", "float"]

	word_count(wl1, wl2, wl3)

if __name__ == '__main__':
	main()