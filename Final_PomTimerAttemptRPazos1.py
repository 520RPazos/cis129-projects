#Rene Pazos
#CIS129
#Final timer attempt
#Pomodoro Timer - Timer for people to use and prevent burn out sounds will play when timer goes off. 
#To fully make use of this please ensure you are using a windows Operating System and audio is not muted.

#Time module to handle time functions
#Winsound module allows  basic sounds to play on a Windows PC
import time
import winsound

def pomodoro_timer():
#Set durations for work and relaxation times
    durations = [25 * 60, 5 * 60] 

#Motivational messages to user
    work_messages = [
        "Work for 25 minutes! Stay focused and productive!",
        "Keep pushing, you're doing great!",
        "Stay on task and keep your goals in mind!"
    ]

    relax_messages = [
        "Take a break for 5 minutes! You've earned it!",
        "Relax and recharge for a bit!",
        "Good job! Now, take a short break!"
    ]

#Main loop for timer 
    while True:

#Work cycle
#Show the first message
        print(work_messages[0])

#Play sound for work
        winsound.Beep(440, 1000)

#Wait duration
        time.sleep(durations[0])
        
#Relax Cycle and frist relax message
        print(relax_messages[0])

#Play sound for time to relax          
        winsound.Beep(880, 1000)

#Wait for relaxation time to end
        time.sleep(durations[1])  

#Cycle through the messages
        work_messages.append(work_messages.pop(0))  
        relax_messages.append(relax_messages.pop(0)) 

#Ask if user wants to repeat cycle 
        user_input = input("Would you like to continue? (yes/no): ")
        
#Checks user response
        if user_input.lower() == "no":
            print("You've done great work! Remember to take breaks when needed.")
            break
        elif user_input.lower() != "yes":
            
#Does not allow anything other than yes/no
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    pomodoro_timer()
