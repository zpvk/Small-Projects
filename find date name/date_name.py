from datetime import date
from datetime import datetime
date_string = str(input("Enter the Date (ex: dd mm yyyy) : "))
date_name = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day = datetime.strptime(date_string, '%d %m %Y').weekday()
print("You finding date is : " + date_name[day])