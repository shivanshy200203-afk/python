
# Write a program to find sum of all odd numbers between 1 to n
n = int(input("Enter the number"))
sum = 0
for i in range(3,n+1,3):
    sum = sum + i
print(sum)