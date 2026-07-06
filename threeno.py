# find the largest of three number
a = int(input())
b = int (input())
c = int(input())

if a >= b and a >= c:
    print("larger number", a)
elif b >= a and b >= c:
    print("larger number", b)
else:
    print("larger number", c)