import csv

input_file = r"F:\Озон TEMP\TEMP\Венера - Заказы - Мои Склады - 27.05.25.csv"
output_file = r"F:\Озон TEMP\Заказы Венера по дням\Венера_26.05.25.csv"
columns_to_extract = ["Номер заказа",
                      "Номер отправления",
                      "Принят в обработку",
                      "Дата отгрузки",
                      "OZON id",
                      "Артикул",
                      "Сумма отправления",
                      "Итоговая стоимость товара",
                      "Кластер доставки"]  # Названия нужных столбцов

with open(input_file, newline='', encoding='utf-8-sig') as infile, \
        open(output_file, 'a', newline='', encoding='utf-8-sig') as outfile:
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile)

    # Считываем заголовок
    header = next(reader)
    # Проверка состава header
    # print(header)

    # Находим индексы нужных столбцов
    indices = [header.index(col) for col in columns_to_extract]
    # Проверка состава indices
    # print(indices)

    # Записываем заголовок в новый файл
    writer.writerow(columns_to_extract)

    # Обрабатываем и записываем строки с выбранными столбцами
    for row in reader:
        new_row = [row[index] for index in indices]
        writer.writerow(new_row)