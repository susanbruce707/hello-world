##<-Datetime and Timedelta use and simple demonstation
import datetime
from datetime import date
from datetime import timedelta
affirmations = ("You are:",
                "Acceptable",
                "Forgiveable",
                "Lovable",
                "Capable",
                "Competent",
                "In Christ Jesus",
                "*******")
for item in affirmations:
    print(item)
year_1 = 2018 ##<- pass interger to variable
month_1 = 1
day_1 = 10
start_date = datetime.date(year_1, month_1, day_1) ##<- create datetime object
##<- from integers and pass to variable
print("start date date is", start_date) ##<- print datetime object
d1 = start_date.year ##<- turn datetime object into  3 integers
##<- and pass to 3 variables
d2 = start_date.month
d3 = start_date.day
print("Day", d3,type(d3), "Month", d2, type(d2), "Year", d1, type(d1))
week = start_date + timedelta(7)
fortnight = start_date + timedelta(14)
threeweek = start_date + timedelta(21)
fourweek = start_date + timedelta(28)
fiveweek = start_date + timedelta(35)
sixweek = start_date + timedelta(42)
seven_weeks_ago = start_date - timedelta(49)
print("\nstart date plus 1 week is", week,
      "\nplus 5 weeks is", fiveweek,
      "\nseven weeks ago", seven_weeks_ago)
print()
date_format = '%d-%m-%Y'
date1 = '10-1-2018'
date2 = '17-4-2018'
#
diff = datetime.datetime.strptime(date2, date_format)\
       - datetime.datetime.strptime(date1, date_format)
days_diff = diff.days
weeks_diff = days_diff // 7
weeks_and_days_diff = (weeks_diff, (days_diff - (weeks_diff * 7)))
print("between", date1, "and", date2, "is", diff.days, "days")
print()
print("this is ",
      str(weeks_diff),
      " Weeks and ",
      str(weeks_and_days_diff[1]),
      " Days")
print()

period = 14
periods = days_diff // period
print("number of two week periods is", periods)
print()
print("the date from ", date1, "every 2 weeks is")
for delta in range(period, (periods*period+1), period):
    
    print(start_date + timedelta(delta))

