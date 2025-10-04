import openpyxl
import csv

input_file_1 = r"F:\Озон TEMP\Обороты\FBS 25.01.01-31.csv"
input_file_2 = r"F:\Озон TEMP\Обороты\FBO 25.01.01-31.csv"
output_file = r"F:\Озон TEMP\Обороты\Orders 25.01.01-31.csv"

columns_to_extract = ["Номер заказа",
                      "Номер отправления",
                      "Принят в обработку",
                      "Статус",
                      "OZON id",
                      "Артикул",
                      "Итоговая стоимость товара",
                      "Стоимость товара для покупателя",
                      "Кластер доставки"]  # Названия нужных столбцов

# def find_last_column(sheet):
#     last_column = 1  # Минимальный столбец (A)
#     for row in sheet.iter_rows():
#         for cell in reversed(row):
#             if cell.value is not None:
#                 if cell.column > last_column:  # Нашли столбец правее
#                     last_column = cell.column
#                 break  # Переходим к следующей строке
#     return last_column


with open(input_file_1, newline='', encoding='utf-8-sig') as infile1, \
        open(input_file_2, newline='', encoding='utf-8-sig') as infile2, \
        open(output_file, 'w', newline='', encoding='utf-8-sig') as outfile:
    reader1 = csv.reader(infile1, delimiter=';')
    reader2 = csv.reader(infile2, delimiter=';')
    writer = csv.writer(outfile)

    # Считываем заголовок
    header1 = next(reader1)
    # print(header1)
    header2 = next(reader2)

    # Находим индексы нужных столбцов
    indices1 = [header1.index(col) for col in columns_to_extract]
    indices2 = [header2.index(col) for col in columns_to_extract]
    print(indices1)
    print(indices2)

    # Записываем заголовок в новый файл и добавляем столбец тип заказа FBS или FBO
    writer.writerow(columns_to_extract+["FBS/FBO"])

    fbs_count = 0
    fbo_count = 0

    # Обрабатываем и записываем строки с выбранными столбцами
    for row in reader1:
        new_row = [row[index] for index in indices1]
        new_row.append("FBS")
        writer.writerow(new_row)
        fbs_count = fbs_count + 1

    for row in reader2:
        new_row = [row[index] for index in indices2]
        new_row.append("FBO")
        writer.writerow(new_row)
        fbo_count = fbo_count + 1

    print(f"FBS: {fbs_count} строк | FBO: {fbo_count} строк")
