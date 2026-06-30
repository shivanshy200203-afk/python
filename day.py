
from datetime import datetime

year= int(input('enter the year'))
month = int (input('enter the month'))
day= int (input('enter date'))
cale = datetime(year,month,day)
print(cale.strftime("%A"))