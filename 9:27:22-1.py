def main():
	firstName, lastName = fGetName()
	print(lastName, ",", firstName, sep='')

def fGetName():
	# Get the user's first and last names
	first = input('Enter your first name: ')
	last = input('Enter your last name: ')
	# return both names
	return first, last
	
main()