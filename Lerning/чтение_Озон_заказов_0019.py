import pandas as pd

input_filename = r"F:\Озон TEMP\TEMP\2025-07-11.xls"  # Замените на ваш файл

excel_tab = pd.read_excel(input_filename, engine='xlrd')


print(excel_tab.head())
# excel_tab["RecordNumber"] = [i for i in range(1, len(excel_tab) + 1)]

# excel_tab.head(3)
