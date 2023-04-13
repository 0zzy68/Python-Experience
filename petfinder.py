#Alex Austin - CS110-02 Michael Kremer
import pets_class as pt #import classes

petList = [] #create empty list
FILE_PATH = "/Users/luvz3017/Desktop/USF/CS/pets.csv"

def main():
	object_list = fReadData()
	fShowMenu(object_list)

def fShowMenu(petList):
	#Show the menu on one line
	print("---------Pet finder Menu------------------\n 1. Show Pet Names \n 2. Search for pet \n 3. Show List \n 4. Shows Pets of Certain Type \n 5. Sort all of the pets alphebetically \n 6. Exit the Program \n --------------------------")
	choice = int(input('Please enter one of the above options: '))
	if choice == 1:
		fShowPet(petList)
	elif choice == 2:
		fSearchPet(petList)
	elif choice == 3:
		fShowList(petList)
	elif choice == 4:
		fShowType(petList)
	elif choice == 5:
		fAlphabetize(petList)
	elif choice == 6:
		print("Byeeee")
		exit()
	else:
		print("Invalid Choice")

def fShowPet(object_list):#Selection 1
	for object in object_list:
		print(object.getName())

def fSearchPet(petList):#Selection 2
	print("--Search Pet-------------")
	found = False
	petInput = input('Search for a Pet Name. What is the name of the pet you want to find? ')
	for x in petList:
		if x.getName() == petInput:
			print("Pet found at index: ", petList.index(x))
			print(x)
			found = True
		else:
			continue
	if found == False:	#control flow to get name
		print("Sorry, ", petInput, " is not in the list.")

def fShowList(petList):#Selection 3
	for x in petList:
		print(x) #prints whole list

def fShowType(petList):#Selection 4
	
	petType = input('What kind of pet would you like to find? Please enter selection: Dog, Cat, Fish, Bird, Hamster ')
	petType = petType.lower()
	for x in petList:
		if x.getType().lower() == petType:
			print(x) #prints specific type in list

def fAlphabetize(petList):#Selection 5
	poopLst = []
	for x in petList:
		poopLst.append(x.getName())
	for x in sorted(poopLst):
		print(x)

def fReadData():
	file  = open(FILE_PATH, 'r')
	# holds nested list of every pet
	pet_list = []
	object_list = []
	for line in file:
		comma_count = 0
		str_type = ''
		str_name = ''
		str_birthdate = ''
		str_breed = ''
		str_color = ''
		pet_info = []

		for character in line:
			if character == ",":
				comma_count += 1
			elif comma_count == 0:
				str_type += character
			elif comma_count == 1:
				str_name += character
			elif comma_count == 2:
				str_birthdate += character
			elif comma_count == 3:
				str_breed += character
			elif comma_count == 4:
				str_color += character
		str_type = str_type.replace(' ', '') #replaces the space at the beginning with nothing
		str_name = str_name[1:] # for each must get rid of spaces to read
		str_birthdate = str_birthdate[1:]
		str_breed = str_breed[1:]
		str_color = str_color[1:]
		str_list = [str_type, str_name, str_birthdate, str_breed, str_color]
		for string in str_list:
			pet_info.append(string)
		pet_list.append(pet_info)
	#create object from list
	#loops through list of pets
	for lst in pet_list:
		# creates an object using the elements in the nested list
		obj_pet = pt.Pets(lst[0], lst[1], lst[2], lst[3], lst[4])
		# appends the objects to a list
		object_list.append(obj_pet)
	return object_list
main()