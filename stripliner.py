#This script removes a given keyword/pattern/etc. from a file

# File definitions
f_in = "in.txt"
f_out = "out.txt"

# String to be filtered out
filter_str = ", "

def removeComments(inputFileName, outputFileName, tag):

    input = open(inputFileName, "r")
    output = open(outputFileName, "w")

    output.write(input.readline())

    for line in input:
        if not line.lstrip().startswith(tag):
            output.write(line)

    input.close()
    output.close()

removeComments(f_in, f_out, filter_str)
