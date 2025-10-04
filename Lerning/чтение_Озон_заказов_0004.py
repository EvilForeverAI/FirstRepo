import csv

input_file = r"F:\Озон TEMP\TEMP\Венера - Заказы - Мои Склады - 27.05.25.csv"
output_file = r"F:\Озон TEMP\Заказы Венера по дням\Венера_26.05.25.csv"
art_search = ""

with open(input_file, newline="", encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=';' )

