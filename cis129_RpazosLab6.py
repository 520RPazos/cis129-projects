#Get numbers of Dogs for cookout
def getTotalHotDogs():

#Prompts person for number of people attending and ask how many dogs they will want.
    attendees = int(input("Enter the number of people attending the cookout: "))
    hotDogs = int(input("Enter the number of hot dogs each person will be given: "))

#Calculate total number of dogs needed.
    total = attendees * hotDogs

#Returns total of dogs
    return total

#Displays result of cookout Calculations
def showResults(total):

#Sets amounts of Dogs and Buns in packaging    
    DOGS = 10
    BUNS = 8

#Calculates number of dogs and buns left over 
    dogsLeft = (DOGS - total % DOGS) % DOGS
    bunsLeft = (BUNS - total % BUNS) % BUNS

#Calculates min packages needed for both dogs and buns    
    minDogs = (total // DOGS) + (0 ** (0 ** dogsLeft))   
    minBuns = (total // BUNS) + (0 ** (0 ** bunsLeft))
    
#Print statements to show results shows results    
    print("Minimum packages of hot dogs needed:", minDogs)
    print("Minimum packages of hot dog buns needed:", minBuns)
    print("Hot dogs remaining:", dogsLeft)
    print("Hot dog buns remaining:", bunsLeft)

#Sets the program to run by calling the other functions. 
def main():
    totalHotDogs = getTotalHotDogs()
    showResults(totalHotDogs)

#Sets the main function which runs program
if __name__ == "__main__":
    main()
