# remove all occurrence of a specific item

list = [5 , 20 , 15 , 20 , 25 , 50 ,20]

target = 20

while target in list:
  list.remove(target)

print(list)