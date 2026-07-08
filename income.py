# calculate income tax: income < 2.5L -> 5L -> 5%
# 5L -> 10L -> 20%
# 10 L -> 20 % 
#Above 10L -> 30 %

income = int(input('enter the income'))
if income < 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <=1000000:
    tax = income * 0.20

else : 
    tax = income * 0.30

print( "income tax = ", tax)