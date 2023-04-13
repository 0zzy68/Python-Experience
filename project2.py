#Project 2
#Steps:
#	Read the files, extract data for San Francisco County only
#	Calculate the daily cases from the cumulative cases (cumulative: 3, 8, 20  daily cases: 3, 5, 12)
#	Calculate the 7-day moving average
#	Save the data for San Francisco County into a new file
#	Plot the data in a scatter plot

import CovidSFPlot

#Part 1a: Obtain the files and add your name
#Alex Austin - CS110-02 Michael Kremer
#Part 1b: Familiarize yourself with the files
#Constants
FILE_PATH_INPUT = [open("/Users/luvz3017/Desktop/USF/CS//covid-19-data-master/us-counties-2020.csv"), open("/Users/luvz3017/Desktop/USF/CS//covid-19-data-master/us-counties-2020.csv"), open("/Users/luvz3017/Desktop/USF/CS//covid-19-data-master/us-counties-2020.csv")] #A list object containing the 3 files downloaded as a string 
FILE_PATH_OUTPUT = "/Users/luvz3017/Desktop/USF/CS/covid-SF.csv" #The path and name of the new file, name the file covid-SF.csv
WINDOW = 7 #the number of previous days for the moving average

#Part 2a: Create the program structure
#In function main, replace the print statement used in part 2a with the function fWriteOutputFile. Basically, the argument of function fWriteOutputFile is the return value of function fReadInputFile,
#In function main, call the function fReadOutputFile passing the file stored in constant FILE_PATH_OUTPUT as the argument. Wrap a print statement around this function call for testing purposes.
#In function main, call function fCalcMovAvg and pass the return value of function fReadOutputFile and wrap a print statement around it for testing purposes. Scroll up to see the first values and verify that the first 6 values are 0, and the 7th value should be unequal to 0.
def main(): #Orchestrating main program (as usual)
	print(fReadInputFile(FILE_PATH_INPUT)) #In function main, loop over the 3 input files, within the loop call the function fReadInputFile. For testing purposes, wrap the print function around to output the lists into the console.
	
	#In project2, import the CovidSFPlot file as plot. In function main, at the end, call the function fPlotSFCovid passing the file stored in constant FILE_PATH_OUTPUT.
	fPlotSFCovid(FILE_PATH_OUTPUT)
#Part 2a: Read the input files
#In function fReadInputFile read one file at a time in read mode. Loop over the file line by line. For each line, test whether it contains the string ‘San Francisco’. If it does, calculate the daily cases by subtracting the current cumulative case number from the previous (iteration) cumulative case number.
#To test this program, put a print statement in all other functions (otherwise you will receive an error message) or comment out the not yet used functions.
#To fix some the data irregularities, test the daily case number. If it is greater than 2000, then set it to 2000 and convert it into string (since all information in the file are string values). Then append the date value (first column) and daily case value into a list object. When you are done with the loop, close the file and return the list.
def fReadInputFile(pFileName): #Define one parameter pFileName, this function reads the input files and returns a list of data
	file = open(str(FILE_PATH_INPUT, "r")) #r+ reads and writes
	for line in file:
		if line.contains("San Francisco"):
			file.readlines()
	file.close()
	return pFileName

#Part 2b: Save the input file into the output file		
#In function fWriteOutputFile, open the file stored in constant FILE_PATH_OUTPUT in append mode. Loop over the list stored in the parameter pList and write each item into the file. After the loop, close the file.
def fWriteOutputFile(pList): #Define one parameter pList, write the list data to the new file stored in constant FILE_PATH_OUTPUT
	file = open(FILE_PATH_OUTPUT, "a")
	for line in pList:
		pList.write(file)
	file.close()
	return pList

#Part 2c: Read the output file
#In function fReadOutputFile open the file stored in constant FILE_PATH_OUTPUT in read mode. Loop over each line and append the second column (cumulative case numbers) into a list and return the list
def fReadOutputFile(pFile): #Define one parameter pFile, reads data from the new file stored in constant FILE_PATH_OUTPUT and returns a list of cases in San Francisco County
	file = open(FILE_PATH_OUTPUT, "r") #r+ reads and writes
	file = open(FILE_PATH_OUTPUT, "r")
	for line in file:
		file.readlines()
	file.close()
	return pFile
#Part 3a: Calculate moving average
#In function fCalcMovAvg initialize variable movAvg to an empty list. Loop over the passed list pList. For the first 6 elements in this list, set the elements to 0 and append them into a list named movAvg. For the 7th and higher values, calculate the 7-day moving average by summing up the previous 6 values plus the current value and divide it by the value stored in constant WINDOW and append them to list movAvg. Return the list movAvg.
#Part 3b: Add moving average to output file
#In function fCalcMovAvg open the output file in first read mode. Loop over each line, concatenate a comma and the moving average that was passed as an argument to this function to the current line. Make sure to remove the line break from the current line, add the moving average, and then add a line break at the end. Store the modified line in a variable and accumulate this variable for each loop. After the loop, the variable will hold the entire modified file content.
#Now close the file and open it up in write mode. Write the value of the variable holding the modified file content to the file. Then close the file.
#Open the output file and verify that the moving average has been written as the 3rd column.
def fCalcMovAvg(pList): #Define one parameter pList, this function calculates and returns a list of 7-day moving averages
	list_mov_avg = [0] * 6 #can be a string with ["0"]
	movAvg = []
	for i in (WINDOW,len(pList)): #nested loop to go through all data values
		num = 0
		for j in range(WINDOW):
			num += pList[i-j]
	list_mov_avg.append(num/WINDOW)
	return movAvg

#IMPORTANT: If you run this program multiple times, keep in mind that you are appending data to the new file. That means, for every run you are adding more and more data to it. Make sure to manually delete the file before running the program again.
def fWriteCovidSFFile(pFile, pListMovAvg): #Define two parameters pFile and pListMovAvg, this function adds the calculated moving average to the new file stored in constant FILE_PATH_OUTPUT in the 3rd column
	file = open(pFile, "r")
	lst = []

main()
#Especially, look at the 2022 file for January 1. The cumulative case number is extremely large compared to previous and following numbers. So, there are data irregularities that we have to address (in a simple way here).

#Required files to be uploaded to Canvas:
	#README.txt file - A description of your project with your name and your student ID. Please include any problems you faced, any resources you used, names of friends/tutors you received help from
	#	Screenshot of the executed code in command line/terminal window and the plot graphics window (either pasted into a Word document or as an image)
	#	The main python file named project2.py
	#	The plot file named CovidSFPlot.py