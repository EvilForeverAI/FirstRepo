import pandas as pd

input_file_1 = r"F:\Озон TEMP\Обороты\FBS 25.06.csv"
input_file_2 = r"F:\Озон TEMP\Обороты\FBO 25.06.csv"
output_file = r"F:\Озон TEMP\Обороты\Orders 25.06.xlsx"
articles_table = r"F:\Озон TEMP\Наши товары\Наши товары 25.06.17.xlsx"

columns_to_extract = [
    "Номер заказа", "Номер отправления", "Принят в обработку",
    "Статус", "OZON id", "Артикул",
    "Итоговая стоимость товара", "Стоимость товара для покупателя",
    "Кластер доставки"
]

# 1. Чтение основных данных
df1 = pd.read_csv(input_file_1, sep=';', usecols=columns_to_extract)
df1['FBS/FBO'] = 'FBS'
df2 = pd.read_csv(input_file_2, sep=';', usecols=columns_to_extract)
df2['FBS/FBO'] = 'FBO'

# 2. Чтение таблицы с артикулами и складами
articles_df = pd.read_excel(articles_table)
articles_df = articles_df.rename(columns={
    articles_df.columns[0]: 'Артикул',
    articles_df.columns[1]: 'Склад'
})

# Приведение артикулов к строковому типу в ОБЕИХ таблицах
articles_df['Артикул'] = articles_df['Артикул'].astype(str).str.strip()  # Число → текст
combined_df = pd.concat([df1, df2])
combined_df['Артикул'] = combined_df['Артикул'].astype(str).str.strip()  # На случай пробелов

# 3. Объединение с основной таблицей
combined_df = pd.concat([df1, df2])
combined_df = pd.merge(
    combined_df,
    articles_df[['Артикул', 'Склад']],
    on='Артикул',
    how='left'  # Если артикул не найден, будет NaN
)

# 4. Статистика
total = len(combined_df)
fbs_count = len(df1)
fbo_count = len(df2)
fbs_percent = round((fbs_count / total) * 100, 2)
fbo_percent = round((fbo_count / total) * 100, 2)

stats_df = pd.DataFrame({
    'Тип': ['FBS', 'FBO', 'Всего'],
    'Количество': [fbs_count, fbo_count, total],
    'Процент': [fbs_percent, fbo_percent, 100]
})

# 5. Сохранение в Excel
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    combined_df.to_excel(writer, sheet_name='Данные', index=False)
    stats_df.to_excel(writer, sheet_name='Статистика', index=False)

print(f"Готово! Файл сохранен: {output_file}")
print(f"FBS: {fbs_count} строк ({fbs_percent}%) | FBO: {fbo_count} строк ({fbo_percent}%) | Всего: {total}")