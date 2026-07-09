#check  whether a number is divisible by 2 but not by 3

num = int(input('enter the number'))

if num % 2 == 0 and num % 3 != 0 :
 print('the number is divisible by 2 but not by 3')
else :
 print('false')