# write a python program to display calender

import calendar
year = int(input('Enter the year'))
month= int(input('enter the month'))

calen = calendar.month(year,month)
print(calen)
