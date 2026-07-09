# Find the grade
#90 - 100 -> A 
#80 - 89 -> B
#70 - 79-> c
#60 - 69 -> D
#below - F """

grade = int(input( 'enter the number'))

if grade < 59 :
 print(' F')
elif grade < 69:
 print('D')
elif grade < 79 :
 print('C')
elif grade < 89:
 print('B')
else:
 print('A')