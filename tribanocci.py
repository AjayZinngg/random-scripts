def printTribRec(n):

	if n == 0 or n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return printTribRec(n - 1) +  printTribRec(n - 2) + printTribRec(n - 3)


def printTrib(n):

    for i in range(0,n):
       print(printTribRec(i) + " ")

 
def main():

    print("Enter the number of elements")
    n = input()
    printTrib(n)
    return 0

