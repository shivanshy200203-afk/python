# calculate dicount 
# Amount >= 5000  -> 20 %
# amount >= 3000 -> 10 %
# Amount = no discount 
Amount = int(input(' enter the amount'))
discount = int (input ('Enter the discount'))

discount_amount = ((Amount* discount)/100)
final_price = Amount - discount_amount

print('discount_amount', discount_amount)
print('final_price', final_price)


