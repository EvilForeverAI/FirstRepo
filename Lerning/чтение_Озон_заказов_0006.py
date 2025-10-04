# Как записывать данные в Excel

import openpyxl

book = openpyxl.Workbook()

sheet = book.active

sheet['A2'] = 100
sheet['B3'] = "Hello World!!!"

sheet[1][0].value = 'DarkSider'

book.save("F:\Озон TEMP\Наши товары\Таблица всех артикулов 465_2.xlsx")
book.close()

my_list = (1, 2, 3, 4)
print(type(my_list))
