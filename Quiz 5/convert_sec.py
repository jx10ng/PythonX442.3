"""Question 4: Write a function that takes times of the form 03:12:19 
(in other words, three hours, twelve minutes, and nineteen seconds) 
and converts them to the corresponding number of seconds."""

import re

def sec_convert(mytime):
	
	regex = r'^([0-1]\d|2[0-3])(?::([0-5]?\d)?(?::[0-5]?\d))?$'

	#regex = r'^(\d{2})(?::\d{2})(?::\d{2})$'
	#([0-1]\d|2[0-3])   - hours from 0 to 23: [0-1]+digit or 2+[0-3] 
	#(?::([0-5]?\d))?  - optional mins, 0 - 59
	#(?::[0-5]?\d))?  - optional secs, 0 - 59

	newtime = re.search(regex, mytime)
	if newtime:
		hours , mins, secs = re.split(':', mytime)

		hours_sec = int(hours) * 3600 #converts hours string to a number in seconds
		mins_sec = int(mins) * 60 #converts mins string to a number in seconds
		secs_sec = int(secs) #converts secs string to a number in seconds

		my_secs = hours_sec + mins_sec + secs_sec #adding all the seconds
		print('{0} calculates to {1} seconds'.format(mytime, my_secs))

	else:
		print('{0} is not a proper time format'.format(mytime))

	return

def main():
	sec_convert("03:12:19")
	sec_convert("Testing") #for testing purposes

if __name__ == '__main__':
	main()