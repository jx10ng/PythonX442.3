"""Question 2: As an alternative to the range function, some programmers like to increment a 
counter inside a while loop and stop the while loop when the counter is no longer 
less than the length of the array."""

import sys

def main():
    
	a = [7, 12, 9, 14, 15, 18, 12] 
	b = [9, 14, 8, 3, 15, 17, 15] 
	count = 0

	big = [] 
	while count < len(a):
	    big.append(max(a[count], b[count])) 
	    count += 1
	print(big)

if __name__ == '__main__':
    main()