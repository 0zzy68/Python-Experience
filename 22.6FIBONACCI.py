def main():
	n = int(input("Insert how many fibonacci iterations you want: "))
	lstFib = []
	for num in range(n + 1):
		lstFib.append(fFib(num))

	print("The first", n , "Numbers in the ")
	print("Fibonacci series:")
	print(* lstFib, sep = ", ")

def fFib(pNum):
	if pNum == 0:
		result = 0
	elif pNum == 1:
		result = 1
	else:
		result = fFib(pNum - 1) + fFib(pNum - 2)
	return result

main()