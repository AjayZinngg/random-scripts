from sys import argv

script, fromFile, toFile = argv


def copy(fromFile, toFile):
    # Open file 'fromFile' for reading as binary
    sourceFile = open(fromFile, "rb") 
    data = sourceFile.read()
    sourceFile.close()

    # Open (or create if does not exists) file 'toFile' for writing as binary
    destFile = open(toFile, "wb") 
    destFile.write(data)
    destFile.close()

    print("Done!")

# Ask for file names
#src = input("Type the source file name:\n")
#dst = input("Type the destination file name:\n")

# Call copy function
copy(fromFile, toFile)