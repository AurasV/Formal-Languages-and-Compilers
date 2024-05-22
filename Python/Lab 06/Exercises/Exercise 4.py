import datetime

date = input("Enter date (YYYY-MM-DD): ")
date = datetime.datetime.strptime(date, "%Y-%m-%d")
print(datetime.date(date.year, date.month, date.day).isocalendar()[1])