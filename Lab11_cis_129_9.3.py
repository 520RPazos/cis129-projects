#Imports both CSV/OS modules for csv and OS manipulation/pathing 
import csv
import os

#Get the path to the current user's desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

#Make the file path for the CSV file on the desktop
file_path = os.path.join(desktop_path, "grades.csv")

try:

#Ask for the number of students
    num_students = int(input("Enter the number of students: "))

#Open the CSV file in write mode
    with open(file_path, "w", newline='') as csvfile:

#Create a CSV writer object
        csv_writer = csv.writer(csvfile)
        
#Write headers to the CSV file
        csv_writer.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])
        
#Loop through each student
        for i in range(num_students):
#Prompt the instructor to enter student information
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
#Loop until a valid numeric grade is entered for each exam
            while True:
                try:
                    exam1_grade = int(input("Enter student's exam 1 grade: "))
                    exam2_grade = int(input("Enter student's exam 2 grade: "))
                    exam3_grade = int(input("Enter student's exam 3 grade: "))

#Exit the loop if all grades are valid                    
                    break  

#Displays error if a non numberic value is given for grades                
                except ValueError:
                    print("Please only input numberic values for grades")
            
#Write student information to the CSV file
            csv_writer.writerow([first_name, last_name, exam1_grade, exam2_grade, exam3_grade])

    print("Student information has been written to", file_path)


except PermissionError:
    print("Permission denied: Unable to create file on desktop. Please run script as an Administrator")

except Exception as e:
    print("An error occurred:", e)
