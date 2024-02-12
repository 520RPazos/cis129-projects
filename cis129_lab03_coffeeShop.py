#Name of Shop and add Description
print("Pazos Coffee and Baked Goods")
print("When you are here you are with family!")

#Creates the question that ask users quantity of items Coffee,Muffin
Numbs_coffee = int(input("How much coffee would you like?"))
Numbs_muffin = int(input("How many muffins would you like?"))

#Add new items to the shop list Croissant and Banana Bread
Numbs_croiss = int(input("How many Croissants would you like?"))
Numbs_bbread = int(input("How much Banana bread would you like?"))

#Calculates of cost of items
price_muffin = 4.00
price_coffee = 5.00

#Add pricing of the Croissant and the Banana bread
price_croiss = 8.00
price_bbread = 9.00

#Calculates Subtotal
subtotal = (Numbs_coffee * price_coffee) + (Numbs_muffin * price_muffin) + (Numbs_croiss * price_croiss) + (Numbs_bbread * price_bbread)

#Calculates Tax with tax rate of 6%
tax_rate = 0.06
tax = (subtotal * tax_rate)

#Total Cost with tax included
total = subtotal + tax

#Print statements rounded to the second decimal point to act as a receipt, list the items of purchase with price
print("Pazos Coffee and Baked Goods Receipt")
print(Numbs_coffee, "Coffee at $5 each: $",'{:.2f}'.format(Numbs_coffee * price_coffee,))
print(Numbs_muffin, "Muffins at $4 each: $",'{:.2f}'.format(Numbs_muffin * price_muffin) )
print(Numbs_croiss, "Croissant at $8 each: $",'{:.2f}'.format(Numbs_croiss * price_croiss))
print(Numbs_bbread, "Banana Bread at $9 each: $",'{:.2f}'.format(Numbs_bbread * price_bbread))
#Prints tax, total, and thank you message
print("6% tax: $",'{:.2f}'.format(tax))
print("Total: $",'{:.2f}'.format(total))
print("Thank you for coming in to Pazos C&B! Show this receipt the next time you come in an receive 5% off your next purchase!")
