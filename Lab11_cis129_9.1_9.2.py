#Rene Pazos
#CIS129
#Lab 11
#Deitel & Dietel 9.1, 9.2
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

#Displays grades have been written to grades.txt
print("Grades have been written to", file_path)

try:

#Attempt to open grades.txt file
    with open(file_path, "r") as file:

#Initialize an empty list to store valid grades
        grades = []

#Read all lines from the file
        for line in file:
#Gets rid of whitespace from the line and converts into integer if it is unable to it skips it
            try:
                grade = int(line.strip())
                grades.append(grade)
            except ValueError:
                print(f"Skipping invalid grade: '{line.strip()}'")

#Shows individual grades
        print("Individual Grades:")
        for grade in grades:
            print(grade)

#Calculate total, count, and average
        total = sum(grades)
        count = len(grades)
        average = total / count if count > 0 else 0

#Display total, count, and average
        print("\nTotal:", total)
        print("Count:", count)
        print("Average:", average)

#Checks if grades.txt exis in users desktop 
except FileNotFoundError:
    print(f"File '{file_path}' not found. Please make sure the file exists.")

#Catch any other exceptions and display an error message
except Exception as e:
    print("An error occurred:", e)
