import sys

def main():
    
	my_files = open("myfiles.txt", 'r')
	max_len = 0
	max_line = 0

	while True: 
		line_text = my_files.readline()
		line_len = len(line_text)

		if line_text != "" and (line_len > max_len):
			max_len = line_len
			max_line = line_text
		else: 
			break
	print(max_line)
	my_files.close()

if __name__ == '__main__':
    main()

