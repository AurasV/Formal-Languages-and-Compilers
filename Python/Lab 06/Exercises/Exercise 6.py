from datetime import datetime, timedelta

print("Current date", datetime.now().strftime("%Y %B %d, %H:%M:%S"))
print("Date 10 days ago", (datetime.now() - timedelta(days=10)).strftime("%Y %B %d, %H:%M:%S"))