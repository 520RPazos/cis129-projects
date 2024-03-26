#CIS129
#Rene Pazos
#Lab8
#Palindrome tester check to see if input is the same forwards as it is backwards 

def is_palindrome(s):

#Remove spaces and punctuation and convert to lowercase
    def preprocess_string(s):
        return ''.join(char.lower() for char in s if char.isalnum())

#Function to check if a string is a palindrome
    def check_palindrome(string):

#Initializes an empty stack
        stack = []

#Pushes each character from the string into the stack
        for char in string:
            stack.append(char)

#Creates empty string to store reversed characters
        reversed_string = ''

#Pops each character from the stack and appends it to the reverse
        while stack:
            reversed_string += stack.pop()

#Checks if the original string is the same as the reversed string 
        return string == reversed_string

#Check if is a palindrome
    return check_palindrome(preprocess_string(s))

#Allows for input and test if palindrome 
input_string = input("Please enter the test for a palindrome: ")
print("Is it a palindrome?", is_palindrome(input_string))
