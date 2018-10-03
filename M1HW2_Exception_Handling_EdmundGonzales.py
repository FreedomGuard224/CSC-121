# Gonzales, Edmund
# 5 Sep 2018
# CSC-121 M1HW2 - Exception Handling
# Implement 2 exceptions 

def main():
    
    try:
        
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

    except ValueError:
        print("Error: Data must be a number.")
                
    except IOError:
        print("Error: Can not find the designated file. Check name and path.")
           
main()
