"""Question 2: The input function will read a single line of text from the terminal. 
If you wanted to read several lines of text, you could embed this function inside a 
while loop and terminate the loop when the user of the program presses the interrupt 
key (Ctrl-C under UNIX, Linux and Windows.) Write such a program, and note its behavior 
when it receives the interrupt signal. Use a try/except clause to make the program behave more grace"""


def main():
	entered_inputs = []

	try:
		while 1:
			my_input = input('Type an input ')
			entered_inputs.append(my_input) #saves the entered inputs into a list

	except KeyboardInterrupt:
		print('Input request terminated with KeyboardInterrupt')
		print("Your current inputs: {0}".format(entered_inputs))

	return	

if __name__ == '__main__':
	main()