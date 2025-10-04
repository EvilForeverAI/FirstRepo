import pandas as pd

input_file_1 = r"F:\Озон TEMP\Обороты\25.07.23\FBS 25.07.23.csv"
input_file_2 = r"F:\Озон TEMP\Обороты\25.07.23\FBO 25.07.23.csv"
output_file = r"F:\Озон TEMP\Обороты\25.07.02\Orders 25.07.23.xlsx"
articles_table = r"F:\Озон TEMP\Наши товары\Наши товары 25.06.17.xlsx"

columns_to_extract = [                  # были изменены названия столбцов, "Итоговая стоимость товара" на "Ваша цена" | "Стоимость товара для покупателя" на "Оплачено покупателем"
    "Номер заказа", "Номер отправления", "Принят в обработку",
    "Статус", "OZON id", "Артикул",
    "Ваша цена", "Оплачено покупателем",
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

# Приведение артикулов к строковому типу
articles_df['Артикул'] = articles_df['Артикул'].astype(str).str.strip()
combined_df = pd.concat([df1, df2])
combined_df['Артикул'] = combined_df['Артикул'].astype(str).str.strip()

# 3. Объединение данных
combined_df = pd.merge(
    combined_df,
    articles_df[['Артикул', 'Склад']],
    on='Артикул',
    how='left'
)
combined_df['Склад'] = combined_df['Склад'].fillna('Не определен')

# 4. Основная статистика
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

# 5. Статистика по складам
warehouse_stats = combined_df.groupby(['Склад', 'FBS/FBO'], as_index=False)\
                            .size()\
                            .pivot(index='Склад', columns='FBS/FBO', values='size')\
                            .fillna(0)

warehouse_stats['Всего'] = warehouse_stats.sum(axis=1)
warehouse_stats['Доля FBS'] = (warehouse_stats['FBS'] / warehouse_stats['Всего'] * 100).round(2)
warehouse_stats['Доля FBO'] = (warehouse_stats['FBO'] / warehouse_stats['Всего'] * 100).round(2)

# 6. Сохранение в Excel
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    combined_df.to_excel(writer, sheet_name='Данные', index=False)
    stats_df.to_excel(writer, sheet_name='Общая статистика', index=False)
    warehouse_stats.to_excel(writer, sheet_name='Статистика по складам')

print(f"Готово! Файл сохранен: {output_file}")
print(f"FBS: {fbs_count} строк ({fbs_percent}%) | FBO: {fbo_count} строк ({fbo_percent}%) | Всего: {total}")
print("\nСтатистика по складам:")
print(warehouse_stats)