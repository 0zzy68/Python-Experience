#Alex Austin - CS110 Section 2 Michael Kremer
#Steps for file processing
	#First Step: = open
	#Second Step = read or process
	#Third step = close

#CONSTANTS
FILE_PATH = "contacts.txt"

def main():
	fMenu()

# used for selction of what function to be used
def fMenu():
	choice = int(input('Print Address Book (1)\nSearch Contact (2)\nAdd new contact (3)\nDelete Contact (4)\nQuit (5)\nEnter your choice: '))
	if choice == 1:
		fPrintAddressBook()
	elif choice == 2:
		fSearchContact()
	elif choice == 3:
		fAddContact()
	elif choice == 4:
		fDeleteContact()
	elif choice == 5:
		check = input('Do you want to continue? Yes (y) and No (n) ')
		if check == 'y':
			fMenu()
		if check == 'n':
			exit()
		else:
			print("Invalid Choice")
			check2 = input('Do you want to continue? Yes (y) and No (n) ')
			if check2 == 'y':
				fMenu()
			elif check2 == 'n':
				exit()
			else:
				print("Invalid Choice")
	else:
		print("Invalid Choice")

#First Selection
def fPrintAddressBook():
	file = open(FILE_PATH, "r")
	count = 0
	for line in file:
		#cycle through to make sure that all parts of a contact are printed before hyphens
		if count == 0:
			print('--------------------------')
		elif count % 3 == 0:
			print('--------------------------')
		print(line.rstrip())
		count += 1
	print('--------------------------')
	file.close()

#Second Selection
def fSearchContact():
	searchContact = input('Enter contact to be searched: ')
	file = open(FILE_PATH, "r")
	boolFound = False
	for line in file:
		if line.rstrip() == searchContact:
			print("contact Found")
			file.close()
			return
	print("Contact " + searchContact + " not found")
	file.close()

#Third Selection
def fAddContact():
	file = open(FILE_PATH, "a")
	name = input("Enter new contact name ")
	address = input("Enter new contact address ")
	zipcode = input("Enter new contact zipcode ")
	file.write(name + "\n" + address + "\n" + zipcode + "\n")
	file.close()
	print("Contact added")

#Fourth Selection
def fDeleteContact():
	strFile = ''
	file = open(FILE_PATH, "r")
	searchContact = input('Enter contact to be searched: ')
	modifiedContact = input('Enter modified contatct: ')
	for line in file:
		if line.rstrip() == searchContact:
			strFile += modifiedContact
		else:
			strFile += line
	file.close()
	file = open(FILE_PATH, "w")
	file.write(strFile)
	file.close()
	print("Contact Updated")

#PART 3 - fileOpen
#WHAT IS THE MODE?
def fFileOpen(FILE_PATH, mode):
	file = fFileOpen(FILE_PATH, "r")
	mode = input('What file mode are you wanting')
	try:
		file
		#Pass an exception to file check
	except FileNotFoundError:
		print("File not found")	
	return file, mode

main()