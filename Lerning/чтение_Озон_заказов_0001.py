import csv

n = 10
columns_to_extract = ['Номер заказа',
                      'Номер отправления']

FILENAME = r"F:\Озон TEMP\TEMP\Венера - Заказы - Мои Склады - 27.05.25.csv"

with open(FILENAME, newline="", encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    print(header)
    #print(header.index[1])

    #indices = [header.index(col) for col in columns_to_extract]

    # for i, row in enumerate(reader):
    #     if i >= n:
    #         break
    #     print(f"Строка {i+1}: {row}")
