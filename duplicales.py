# Remove Duplicates from List
List = [10, 20, 10, 30, 40, 40, 20, 50]

new = []

for i in List:
    if i not in new:
        new.append(i)

print(new)