#Rene Pazos
#CIS129
#Lab 11
#Deitel & Dietel 9.1, 9.2, 9.3

#Using OS Module to path to current users desktop
import os

#Prompt the user to enter grades
print("Enter grades (enter 'q' to quit):")

#Get the path to the user's desktop
current_desktop = os.path.join(os.path.expanduser('~'), 'Desktop')

#Sets the pathing for the grades.txt to be created on the logged in users desktop.
file_path = os.path.join(current_desktop, 'grades.txt')

#Open the file in append mode
with open(file_path, "a") as file:
    while True:
        grade = input("Enter a grade: ")
        if grade.lower() == 'q':
            break
        file.write(grade + "\n")

print("Grades have been written to", file_path)
