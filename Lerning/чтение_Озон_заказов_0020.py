import pandas as pd

input_file_1 = r"F:\Озон TEMP\Обороты\25.07.23\FBS 25.07.23.csv"

articles_table = r"F:\Озон TEMP\Наши товары\Наши товары 25.06.17.xlsx"

columns_to_extract = [   # были изменены названия столбцов, "Итоговая стоимость товара" на "Ваша цена" | "Стоимость товара для покупателя" на "Оплачено покупателем"
    "Номер заказа",
    "Номер отправления",
    "Принят в обработку",
    "Статус",
    "OZON id",
    "Артикул",
    "Ваша цена",
    "Оплачено покупателем",
    "Кластер доставки"
]

# 1. Чтение основных данных
# df1 = pd.read_csv(input_file_1, sep=';', usecols=columns_to_extract)
# df1['FBS/FBO'] = 'FBS'

# pd.set_option('display.max_rows', 100)  # показывать до 100 строк
# pd.set_option('display.max_columns', 20)  # показывать до 20 столбцов
# print(df1)

articles_df = pd.read_excel(articles_table)
articles_df = articles_df.rename(columns={
    articles_df.columns[0]: 'Артикул',
    articles_df.columns[1]: 'Склад'
})

pd.set_option('display.max_rows', 20)  # показывать до 20 строк
pd.set_option('display.max_columns', 20)  # показывать до 20 столбцов
print(articles_df)