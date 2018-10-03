# open file and read name, close file and print name
# 29 Aug 2018
# CSC 121-0001 AW1T2 - Name output
# Gonzales, Edmund

def main():
    infile = open("my_name.txt","r")

    file_contents = infile.read()

    infile.close()
    
    print(file_contents)

main()
