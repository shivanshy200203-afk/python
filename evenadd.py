#Write a program to find sum of all even numbers between 1 to n
n = int(input('enter the number'))
sum =0
for i in range (2,n+1,2):
 
    sum = sum +i
print(sum)