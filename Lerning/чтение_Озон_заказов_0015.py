import pandas as pd
from datetime import datetime


def process_excel_by_cluster(input_file, output_file):
    # Чтение данных (заголовок в 3-й строке, пропуск 4-й строки)
    df = pd.read_excel(input_file, sheet_name=0, header=2, skiprows=[3])

    # Проверка наличия нужных столбцов
    required_columns = ['Кластер', 'SKU', 'Артикул', 'Название товара', 'Доступно к продаже']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Столбец '{col}' не найден в таблице")

    # Получаем текущую дату в формате ДД.ММ.ГГГГ
    current_date = datetime.now().strftime("%d.%m.%Y")

    # Получаем все уникальные артикулы из исходных данных
    unique_articles = df[['Артикул', 'SKU', 'Название товара']].drop_duplicates()

    # Создание новой таблицы
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for cluster in df['Кластер'].unique():
            # Фильтруем данные по кластеру
            cluster_data = df[df['Кластер'] == cluster]

            # Группируем по артикулу и суммируем 'Доступно к продаже'
            grouped = cluster_data.groupby(['Артикул'])['Доступно к продаже'].sum().reset_index()

            # Объединяем с уникальными артикулами (left join)
            result_df = pd.merge(
                unique_articles,
                grouped,
                on='Артикул',
                how='left'
            ).fillna(0)  # Заменяем NaN на 0 для артикулов, которых нет в кластере

            # Переименовываем столбец в текущую дату
            result_df = result_df.rename(columns={'Доступно к продаже': current_date})

            # Сортировка по убыванию
            result_df = result_df.sort_values(by=current_date, ascending=False)

            # Упорядочиваем столбцы
            result_df = result_df[['SKU', 'Артикул', 'Название товара', current_date]]

            # Запись на отдельный лист
            sheet_name = str(cluster)[:31]
            result_df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Файл успешно создан: {output_file}")

# Пример использования
input_filename = r"F:\Озон TEMP\Эксперименты\stock-report (7).xlsx"  # Замените на ваш файл
output_filename = r"F:\Озон TEMP\Эксперименты\output.xlsx"  # Имя выходного файла

process_excel_by_cluster(input_filename, output_filename)