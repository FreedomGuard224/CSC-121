# Edmund Gonzales
# M2HW1
# 24 Sep 2018
# Number Analysis

# List from user
def main():

    num_list = []
    
    # List from user
    for x in range (20):
        
        num = float(input("What are the numbers? "))
        num_list.append(num)

    # Print Lowest Number
    print("The lowest value is", min(num_list))
    
    # Print Highest Number
    print("The highest value is", max(num_list))
    
    # Print Total Numbers In List
    length = len(num_list)
    print("There are",length,"numbers in this list.")
    
    # Print Average
    total = 0
    for num in num_list:
        total += num
    average = total / len(num_list)
    print("The average of the list is ",format(average,".0f"),".",sep="")
    
main()
