import csv

def print_first_10_lines_as_dict(csv_file):
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')  # Читаем строки как словари
            for i, row in enumerate(reader):
                if i < 10:
                    print(dict(row))  # Выводим словарь
                else:
                    break
    except FileNotFoundError:
        print(f"Ошибка: файл '{csv_file}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
csv_file = r"F:\Озон TEMP\Наши товары\2025.05.30\analytics_report_2025-05-30_17_57 - Sheet1.csv"  # Укажите путь к файлу
print_first_10_lines_as_dict(csv_file)