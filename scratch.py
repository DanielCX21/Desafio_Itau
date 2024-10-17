import datetime

data = "16/10/2024"

data = datetime.datetime.strptime(data, "%d/%m/%Y")

print(data)
