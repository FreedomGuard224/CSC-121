# Edmund Gonzales
# M2HW2
# 24 Sep 2018
# World Series Champions

def main():
    with open ("WorldSeriesWinners.txt", "r") as infile:

        team = input("Enter a team: ")
        
        teams = infile.readlines()
        index = 0

        while index < len(teams):
            teams[index] = teams[index].rstrip("\n")
            index = index + 1
            
            count = 0
            for winner in teams:
                if winner == team:
                    count = count + 1
                    
        print("The",team,"have won the world series",count,"times.")

main()
