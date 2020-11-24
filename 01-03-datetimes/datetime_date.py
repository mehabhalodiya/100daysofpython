#!python3

from datetime import datetime
from datetime import date

#datetime.now() takes tzinfo as keyword argument but datetime.today() does not take any keyword arguments
datetime.today()

today = datetime.today()

#type() method returns class type of the argument(object) passed as parameter and is mostly used for debugging purposes
type(today)

#we used the date.today() method to get the current local date.
todaydate = date.today()

todaydate
print("Today's date(yyyy-mm-dd): " + str(todaydate))

type(todaydate)

todaydate.month

todaydate.year

todaydate.day

christmas = date(2020, 12, 25)
christmas

if christmas is not todaydate:
    print("There are still " + str((christmas - todaydate).days)+ " days until Christmas!")
else:
    print("Yay it's Christmas!")