import pandas as pd

input_file_1 = r"F:\Озон TEMP\Обороты\FBS 25.01.01-31.csv"
input_file_2 = r"F:\Озон TEMP\Обороты\FBO 25.01.01-31.csv"
output_file = r"F:\Озон TEMP\Обороты\Orders4 25.01.01-31.xlsx"

columns_to_extract = ["Номер заказа",
                      "Номер отправления",
                      "Принят в обработку",
                      "Статус",
                      "OZON id",
                      "Артикул",
                      "Итоговая стоимость товара",
                      "Стоимость товара для покупателя",
                      "Кластер доставки"]  # Названия нужных столбцов

df1 = pd.read_csv(input_file_1, sep=';', usecols=columns_to_extract)
df1['FBS/FBO'] = 'FBS'
df2 = pd.read_csv(input_file_2, sep=';', usecols=columns_to_extract)
df2['FBS/FBO'] = 'FBO'

pd.concat([df1, df2]).to_excel(output_file, index=False)
print(f"FBS: {len(df1)} строк | FBO: {len(df2)} строк")