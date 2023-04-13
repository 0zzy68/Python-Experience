##Alex Austin 20651943 - CS110 # CS 110: Introduction to Computer Science I Michael Kremer - Section 2
public static main(string)args{
	print("hi")
}
def main():
	palindrome = input('Enter a string: ')
	print(fPalindrome(palindrome))

def fPalindrome(pString):
	isPalindrome = true
	pString = pString.lower().replace(' ', '') #Part 2- ignores cases and spaces to check for reversing
	count = 0
	for x in len(pString)-1:
		while x in pString:
			print(x)
			count += 1
		else: 
			isPalindrome == false
	return isPalindrome
	for i in range(len(array)):
	#Java = for(int i =0;i<some.array.length;i++){}
	##++i= incremente before
	##i++=increment after
	#returns true or false depending on if string is palindrome or not

#Pseudocode
#declare the input string to be passed into the function: fPalindrome as an agrument

main()