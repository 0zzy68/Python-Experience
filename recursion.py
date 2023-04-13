def main(): 
	times = int(input('How many times are you calling the function?: '))
	message(times)
def message(times):
	if times > 0:
		print('This is a recursive function.') 
		message(times - 1)
	
	#Wrong
		#count = 0
		#while count < 10:
		#	message()
		#	count += 1
#just call message(5) = calling 5 times

# Call the main function. 
main()