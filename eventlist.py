#  List Comprehension for Filtering Numbers


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = []
for i in list:
 

 if i % 2 == 0 :
   even_number.append(i)

print(even_number)