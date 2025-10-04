import csv

FileName = r"D:\Превосходство\TEMP\users.csv"

users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

with open(FileName, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FileName,"a",newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)