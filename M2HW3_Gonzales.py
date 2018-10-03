# Edmund Gonzales
# M2HW3
# 24 Sep 2018
# Lottery Number Generator

import random

def main():
    
    ran_list = []
    
    for x in range (7):
 
        number = (random.randint(0,9))
        ran_list.append(number)
        ran_list.sort()
        
    for number in ran_list:
        print(number)
        
            
   
    




main()
