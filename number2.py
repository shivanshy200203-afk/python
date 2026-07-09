# nummber = [100,50,400,500]
#updated (change) : [100, 200, 400, 500 ]
# updated (Append) : [100 , 200, 400, 500,600]
#updated (insert) : [100, 200, 300, 400, 500,600]
# updated ( remove 600) : [100, 200 ,300, 400 , 500]
#updated (remove index 0) : [200,300,400, 500]

number = [100,50, 400,500]

number[1] = 200
print(number)

number.append(600)
print(number)

number.insert(2,300)
print(number)

number.remove(600)
print(number)

number.pop(0)
print(number)