# Gonzales, Edmund
# 29 Aug 2018
# CSC121 M1HW1 - Average Numbers
# calculate the average of all numbers sorted in a file

def main():

    with open ("numbers.txt","r") as infile:
    
        line = infile.readline()

        count = 0

        total = 0
    
        while line != "":

            count = count + 1 

            amount = int(line)

            print(format(amount,".0f"))

            total = total + amount

            line = infile.readline()        

        average = total / count

        print("The average of ",count," numbers is ",format(average,".0f"),".",sep="")
              
main()


