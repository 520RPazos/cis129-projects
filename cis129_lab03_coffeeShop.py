#Name of Shop
print("My Coffee and Muffin Shop")

#Creates the question that ask users quantity of Coffee/Muffins
Numbs_coffee = int(input("Number of coffees bought? "))
Numbs_muffin = int(input("Number of muffins bought? "))

#Calculates of cost of items
price_muffin = 4.00
price_coffee = 5.00
subtotal = (Numbs_coffee * price_coffee) + (Numbs_muffin * price_muffin)

#Calculates Tax with tax rate of 6%
tax_rate = 0.06
tax = (subtotal * tax_rate)

#Total Cost with tax included
total = subtotal + tax

#Print statements rounded to the second decimal point to act as a receipt
print("My Coffee and Muffin Shop Receipt")
print("1 Coffee at $5 each: $",'{:.2f}'.format(Numbs_coffee * price_coffee,))
print("2 Muffins at $4 each: $",'{:.2f}'.format(Numbs_muffin * price_muffin) )
print("6% tax: $",'{:.2f}'.format(tax))
print("Total: $",'{:.2f}'.format(total))
