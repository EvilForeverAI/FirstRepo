import pandas as pd

from чтение_Озон_заказов_0007 import articles_table2

input_file_1 = r"F:\Озон TEMP\Обороты\FBS 25.05.01-31.csv"
input_file_2 = r"F:\Озон TEMP\Обороты\FBO 25.05.01-31.csv"

output_file = r"F:\Озон TEMP\Обороты\Orders5 25.05.01-31.xlsx"

articles_table = r"F:\Озон TEMP\Наши товары\Наши товары 25.06.17.xlsx"

columns_to_extract = [
    "Номер заказа", "Номер отправления", "Принят в обработку",
    "Статус", "OZON id", "Артикул",
    "Итоговая стоимость товара", "Стоимость товара для покупателя",
    "Кластер доставки"
]

# Чтение данных
df1 = pd.read_csv(input_file_1, sep=';', usecols=columns_to_extract)
df1['FBS/FBO'] = 'FBS'
df2 = pd.read_csv(input_file_2, sep=';', usecols=columns_to_extract)
df2['FBS/FBO'] = 'FBO'

# Объединение данных
combined_df = pd.concat([df1, df2])

# Статистика
total = len(combined_df)
fbs_count = len(df1)
fbo_count = len(df2)
fbs_percent = round((fbs_count / total) * 100, 2)
fbo_percent = round((fbo_count / total) * 100, 2)

# Создаем DataFrame для статистики
stats_df = pd.DataFrame({
    'Тип': ['FBS', 'FBO', 'Всего'],
    'Количество': [fbs_count, fbo_count, total],
    'Процент': [fbs_percent, fbo_percent, 100]
})
print(type(stats_df))
# Сохранение в Excel с двумя листами
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    combined_df.to_excel(writer, sheet_name='Данные', index=False)
    stats_df.to_excel(writer, sheet_name='Статистика', index=False)

print(f"Готово! Файл сохранен: {output_file}")
print(f"FBS: {fbs_count} строк ({fbs_percent}%) | FBO: {fbo_count} строк ({fbo_percent}%) | Всего: {total}")