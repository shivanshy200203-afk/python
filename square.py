# write a program that will take three digit from the user and add the square of each
n = int(input('enter the number '))

digit1 = n // 100
digit2 = (n //10) % 10 
digit3 = n % 10

sum = digit1**2 + digit2**2 + digit3**2

print(sum)