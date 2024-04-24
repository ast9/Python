from datetime import datetime

now = datetime.now()
print(now)

today = now.strftime("%d %m %Y")
print(today)

str = "17/04/2024"
obj_datetime = datetime.strptime(str,"%d/%m/%Y")

print(obj_datetime.strftime("%Y-%m-%d"))