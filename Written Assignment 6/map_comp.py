"""Question 3: Use the map function to add a constant to each element of a list. 
Perform the same operation using a list comprehension. """

def main():

	list1 = [1, 2, 3, 4] 
	num1 = 1
	num2 = 2

	map_list=map(lambda x: x + num1, list1) #use map 
	print(map_list)

	comprehension_list = [item + num2 for item in list1] #use compression
	print(comprehension_list)

if __name__ == '__main__':
	main()