# Write name to a file and close it
# 29 Aug 2018
# CSC 121-0001 AW1T1 - Name Input
# Gonzales, Edmund

def main():
    
    outfile = open ("my_name.txt","w")

    outfile.write("Edmund Gonzales")

    outfile.close()
    
main()
