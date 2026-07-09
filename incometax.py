# calculate income tax 
# up to 250000 -> 0 %
# 250000 - 500000 -> 5 %
# 500001 - 1000000 ->  20 %

income = int( input(' enter the number '))

if income < 250000 :

    tax = 0 
elif income <= 5000000:
    tax = (income * 5) / 100 
elif income <= 1000000:
    tax = ( income* 20) / 100
else:
    tax =(income*30)/ 100

total_amount = income + tax

print('total_amount' , total_amount)
print('tax', tax)
