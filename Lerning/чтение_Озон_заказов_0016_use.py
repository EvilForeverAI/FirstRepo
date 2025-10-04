import pandas as pd
from datetime import datetime


def process_excel_by_cluster(input_file, output_file):
    # Предопределенный порядок листов
    CLUSTER_ORDER = [
        "Москва, МО и Дальние регионы",
        "Санкт-Петербург и СЗО",
        "Юг",
        "Казань",
        "Воронеж",
        "Ярославль",
        "Урал",
        "Уфа",
        "Кавказ",
        "Сибирь",
        "Саратов",
        "Самара",
        "Тюмень",
        "Красноярск",
        "Дальний Восток",
        "Калининград",
        "Беларусь",
        "Казахстан",
        "Армения"
    ]

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

    # Создание новой таблицы с упорядоченными листами
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Обрабатываем только кластеры из списка CLUSTER_ORDER, присутствующие в данных
        existing_clusters = [c for c in CLUSTER_ORDER if c in df['Кластер'].unique()]

        for cluster in existing_clusters:
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
            ).fillna(0)

            # Переименовываем столбец
            result_df = result_df.rename(columns={'Доступно к продаже': current_date})

            # Сортировка по убыванию
            result_df = result_df.sort_values(by=current_date, ascending=False)

            # Упорядочиваем столбцы
            result_df = result_df[['SKU', 'Артикул', 'Название товара', current_date]]

            # Запись на отдельный лист
            sheet_name = str(cluster)[:31]  # Ограничение Excel на длину имени листа
            result_df.to_excel(writer, sheet_name=sheet_name, index=False)

        # Добавляем недостающие кластеры (если нужно)
        missing_clusters = set(CLUSTER_ORDER) - set(existing_clusters)
        if missing_clusters:
            print(f"Внимание: следующие кластеры отсутствуют в данных: {', '.join(missing_clusters)}")

    print(f"Файл успешно создан: {output_file}")


# Пример использования
input_filename = r"F:\Озон TEMP\Эксперименты\stock-report (7).xlsx"  # Замените на ваш файл
output_filename = r"F:\Озон TEMP\Эксперименты\output.xlsx"  # Имя выходного файла

process_excel_by_cluster(input_filename, output_filename)