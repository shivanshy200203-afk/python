# Calculate discount 
#Amount >= 5000 -> 20 %
#Amount >= 3000 -> 10%

#otherwise -> no discount

Amount = int(input('enter the amount'))

if Amount >= 5000 :
    discount = (Amount*20) / 100
elif Amount >= 3000:
    discount = (Amount*10) / 100
else:
    discount  = 0

final_amount = Amount - discount

print('Amount' , Amount)
print('discount', discount)
print('final_amount ', final_amount)


