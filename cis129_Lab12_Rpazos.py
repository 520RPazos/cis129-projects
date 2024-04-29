#Rene Pazos
#CIS129
#Lab 12
#Program gathers information from user to display Pet name type and age

#Define the Pet class
class Pet:

#Constructor
    def __init__(self, n="", t="", a=0):

#Initialize fields
        self.name = n
        self.type = t
        self.age = a  

#Mutators
    def setName(self, n):

#Name of the pet
        self.name = n
    
    def setType(self, t):

#Type of the pet
        self.type = t
    
    def setAge(self, a):

#Age of the pet
        self.age = a
    
    def getName(self):

#Return name of the pet
        return self.name
    
    def getType(self):

#Return type of the pet
        return self.type
    
    def getAge(self):

#Return age of the pet
        return self.age

#Main module
def main():

#Input variables
    inputName = input("Enter a pet name: ")
    inputType = input("Enter a pet type: ")
    inputAge = int(input("Enter a pet age: "))
    
#Create a Pet object
    Animal = Pet()
    
#Set values for the pet using mutator methods
    Animal.setName(inputName)
    Animal.setType(inputType)
    Animal.setAge(inputAge)
    
#Display information about the pet using accessor methods
    print("The pet name is", Animal.getName())
    print("The pet type is", Animal.getType())
    print("The pet age is", Animal.getAge())

#Call the main function
if __name__ == "__main__":
    main()
