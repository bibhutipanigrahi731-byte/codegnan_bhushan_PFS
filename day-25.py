#day-25
'''
data and time
-------------
-->python provides the built-in datatime module to work with datas and time...


import datetime
now = datetime.datetime.now()
print(f"year is: {now.year}")
print(f"month is: {now.month}")
print(f"day is: {now.day}")
print(f"hour is: {now.hour}")
print(f"year is: {now.minute}")
print(f"second is: {now.second}")



formatting date and time
-------------------------
-->strftime() is used to formate date and tome...
%d-day
%m-month


import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H-%M-%S"))


import datetime
date_1 = datetime.date(2026, 6, 1)
date_2 = datetime.date(2026, 6, 16)
differ_ = date_2 - date_1
print(differ)


timedelta
---------

import datetime
today = datetime.data.today()
future = today + datetime.timedelta(days = 7)
print(future)


import datetime
day_ = datetime.date.today()
print(day_.ctime())


import calendar
import datetime
today = datetime.date.today()
year = today.year
month = today.month
print(calendar.month(year,month))



import calendar
year = 2026
print(calendar.calendar(year))

'''
import smtplib
from email.message import EmailMessage
import time
from datetime import datetime
sender_mail = "bibhutipanigrahi731@gmail.com"
password_ = 'zcwfzneucuvtotvu'
recevier_mail = 'panigrahibibhutibhushan@gmail.com'
targer_time = '10:35'






















