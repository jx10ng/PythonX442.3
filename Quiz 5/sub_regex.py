"""Question 2: Write a substitution command that will change names like file1, file2, etc. 
to file01, file02, etc. but will not add a zero to names like file10 or file20."""

import re

def convert(x):
	return (x.group('filename')+'0'+ x.group('num'))


def subs(string):
	
	reg_pat = r'^(?P<filename>[a-zA-Z]+)(?P<num>[1-9]{1})$'
	regex = re.compile(reg_pat)
	need_upd = regex.match(string)

	if need_upd:
		new_string = regex.sub(convert, string)
		print (new_string)

	else:
		print('{0} is already in proper format'.format(string))

	return


def main():

	subs('file1')
	subs('file2')
	subs('file10')

if __name__ == '__main__':
	main()

