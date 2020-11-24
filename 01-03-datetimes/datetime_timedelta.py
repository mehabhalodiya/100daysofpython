#!python3

#timedelta object represents the difference between two dates or times
from datetime import datetime, timedelta

#using current time
ini_time_for_now = datetime.now()

#printing initial date
print("Initial Date(yyyy/mm/dd): ", str(ini_time_for_now))

#calculating future dates
#for after two years/days
future_date_after_2yrs = ini_time_for_now + timedelta(days=730)
future_date_after_2days = ini_time_for_now + timedelta(days=2)

#printing calculated future dates 
print("Future date after 2 years: ", str(future_date_after_2yrs))
print("Future date after 2 days: ", str(future_date_after_2days))

#calculating future dates
#for before two years/hours
past_date_before_2yrs = ini_time_for_now - timedelta(days=730)
past_date_before_2hours = ini_time_for_now - timedelta(hours=2)

#printing calculated past dates
print("Past date before 2 years: ", str(past_date_before_2yrs))
print("Past date before 2 hours: ", str(past_date_before_2hours))
