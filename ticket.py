# movie ticket booking
#child < 12-> 100
# adult ( 12 - 59) ->  200
# serior ( 60 %) -> 150

# Apply 10 % discount if booking more than 5 ticked

age = int(input(' enter the age '))
ticket= int(input())

if age < 12 :
    price = 100

elif age < 59 :
    price = 200

else:
    price =  150

total = price * ticket

if ticket > 5:
 discount = total * 0.10
 total = total - discount 

print(total)
