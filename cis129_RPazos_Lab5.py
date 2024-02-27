#CIS129
#Rene Pazos
#Takes input to calculate number of bottles in a week and payout 
#Lab 5 The Botle Return Program

# Step 1: Declare variables
total_bottles = 0
count = 1
today_bottles = 0
total_payout = 0.0
keep_going = 'y'

# Step 2: Loop to run program again
while keep_going.lower() == 'y':

# Step 3: Code to set value of variables
# Reset for week
    total_bottles = 0
    total_payout = 0.0
    
    # getBottles code
    num_days = 7

    # Declare and set counter for totalBottles, todayBottles to 0 
    total_bottles = 0
    today_bottles = 0
    count = 1
    
    while count <= 7:
        print("Enter number of bottles returned for day #", count, ":")
        today_bottles = int(input())
        total_bottles = total_bottles + today_bottles
        count = count + 1
    
#Calc for payout
    mon_perBottle = 0.10
    total_payout = total_bottles * mon_perBottle
    
#Print total and payout
    print('Your total number of bottles is', total_bottles)
    print(f'Your payout is ${total_payout:.2f}')
#Start again for next iteration
    print("Do you want to enter another week's worth of data? (Enter y or n)")
    keep_going = input("Enter y or n:")
