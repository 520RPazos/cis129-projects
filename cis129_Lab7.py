#CIS129
#Rene Pazos
#Lab7
#Program to calculate income from theater ticket sales

#Sections Names, prices for tickets in each section, number of available seats in each section
SECTION_NAMES = ['A', 'B', 'C'] 
SECTION_PRICES = {'A': 20, 'B': 15, 'C': 10}  
SECTION_SEATS = {'A': 300, 'B': 500, 'C': 200}  

#Display welcome message
def display_welcome():
    print("Welcome to the theater ticket sales program!")
    print("Please enter the number of tickets sold for each section.")

#Number of tickets sold per section
def get_ticket_sales():

#Stores ticket sales for each section     
    ticket_sales = {}  
    for section in SECTION_NAMES:
        while True:
            try:
                tickets = int(input(f"Enter number of tickets sold for Section {section}: "))
                if tickets < 0:

#Checks for negative tickets                  
                    raise ValueError("Number of tickets cannot be negative")
                elif tickets > SECTION_SEATS[section]:

#Makes sure seats are available
                    raise ValueError("Not enough seats available")
                else:
                    ticket_sales[section] = tickets
                    break
            except ValueError as e:
                print("Error:", e)
    return ticket_sales

#Calculate subtotal for each section
def calculate_subtotal(ticket_sales):
    subtotal = {}  # Dictionary to store subtotal for each section
    for section in ticket_sales:
        subtotal[section] = ticket_sales[section] * SECTION_PRICES[section]
    return subtotal

#Calculate overall total
def calculate_total(subtotal):
    total = sum(subtotal.values())  # Summing up all subtotals to get total income
    return total

#Main function
def main():
    display_welcome()
    
#Ticket sales for each section, Calc subtotal for each section, and finally calculate overall total income.
    ticket_sales = get_ticket_sales() 
    subtotal = calculate_subtotal(ticket_sales) 
    overall_total = calculate_total(subtotal) 

    print("\nSubtotal for each section:")
    for section in subtotal:

#Shows subtotal for each section
        print(f"Section {section}: ${subtotal[section]}")

#Displays overall total income
    print("\nOverall Total:", overall_total)

    print("\nNumber of seats remaining in each section:")
    for section in SECTION_NAMES:
        remaining_seats = SECTION_SEATS[section] - ticket_sales.get(section, 0)
        
# Display remaining seats for sections
        print(f"Section {section}: {remaining_seats} seats")  

#Run main function
main()
