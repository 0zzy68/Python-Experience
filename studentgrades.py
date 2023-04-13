#import pickle library
import pickle
FILE_PATH = 'students.dat'

#Functions for retrieval
def main():
	student = fLoadStudent()
	choice = 1
	while choice != 0:
		print()
		try:
			choice = int(input("1- Add Student, 2 - Display Students, 0 - Exit "))
			if choice == 1:
				fAddStudent(student)
			elif choice == 2:
				fDisplayStudents(student)
			elif choice == 0:
				print("Exiting")
			else: # User entered invalid number
				print("Invalid Input, enter 0, 1, 2") # Print number error, only 0,1,2
		except:  # Exception, If user entered a character rather than a number
			print("Enter a number and not a character") # Print to enter a number and not a character
	fSaveStudents(student) # Save student dictionary into file

def fDisplayGrades(pDictStudent):
	for key in pDictStudent.keys():# Loop over dictionary
		print("Student", student, grade, end='')# Print out student and major
	print("-" * 50) # Print line of 50 hyphens

def fLoadStudent():
	dctStudent = {}
	try:# try statement to test for non-existent file
		file = open(FILE_PATH, 'r')    # Open file for binary read
		pb = pickle.load(file)# Unpickle dictionary
		file.close()# Close file
	except IOError:# Exception: File does not exist
		dctStudent.clear()# Could not open file --> create empty dictionary 
	return dctStudent# Return dictionary

def fAddStudent(pDictStudent):
	student = input('Enter student name: ') # Get student
	grade = input('Enter grade: ') # Get grade
	if student not in pDictStudent:# If student does not exist in  dictionary,
		pDictStudent[grade]# add it as key with grade as associated value
		pDictStudent[student]# Add student object to dictionary
		print('Student', student,'has been added') # Print student has been added
	else: # Else student already exists
		print("Student ", student, " already exists")# Print student already exists  

# fSaveStudent funtion pickles specified
# object and saves it to student file
def fSaveStudents(pDictDeposits):
	file = open(FILE_PATH, 'w')# Open file for writing
	pickle.dump(student, file)# Pickle dictionary and save it
	file.close() # Close file

# Call main function to start program
main()