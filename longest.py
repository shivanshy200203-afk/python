#find the longest string in a list

word = ["PHP" , "Exercise" , "backend" , "python"]

longest = word[0]

for i in word:
    if len(i) > len(longest):
        longest = i
print("longest=",longest)