#Rene Pazos
#CIS129
#Lab 10
#Check Protection Lab 
#Program to  prevent fradulent checks, enters in astericks to prevent fraud 

def main():
    while True:
        try:
#Input initial dollar amount            
            dollar_amount = float(input("Enter dollar amount: "))

#Checks if the amount provided is negative 
            if dollar_amount < 0:
                raise ValueError("Negative dollar amount is not allowed.")
            
#Break the loop if input is valid
            break  
        except ValueError:
            
#Prints error if something other than a positive number is given
            print("Invalid input. Please enter a valid positive number.")

#Convert dollar amount to string with 2 decimal place and comma at thousandth place
    dollar_str = "{:,.2f}".format(dollar_amount)

#Check if need for leading characters
    if len(dollar_str) < 10:

#Calculate number of characters needed
        num_spaces = 10 - len(dollar_str)

#Print amount with leading asterisk
        print("*" * num_spaces + dollar_str)
    else:
#Print amount without leading space
        print(dollar_str)

if __name__ == "__main__":
    main()
