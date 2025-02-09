from datetime import datetime


date1 = datetime(2025, 2, 7, 14, 30, 0)  
date2 = datetime(2025, 2, 7, 15, 30, 0) 


difference = (date2 - date1).total_seconds()   #difference between date1,date2

print(f"Difference in seconds: {difference}")