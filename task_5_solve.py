import os
import pandas as pd
import json

# Читаем и преобразуем csv файл
df = pd.read_csv('/home/whytech/lab_2/tasks/air_pollution_in_seoul.csv')
df_new = df.drop(columns='Address')

# Сохраняем преобразованный файл
df_new.to_csv('/home/whytech/lab_2/results/air_pollution_in_seoul_new.csv')                     # csv
df_new.to_json('/home/whytech/lab_2/results/air_pollution_in_seoul_new.json')                   # json
df_new.to_pickle('/home/whytech/lab_2/results/air_pollution_in_seoul_new.pkl')                  # pickle
df_new.to_pickle('/home/whytech/lab_2/results/air_pollution_in_seoul_new.msgpack', protocol=5)  # msgpack

# Считаем размеры полученных файлов
csv_size = os.path.getsize('/home/whytech/lab_2/results/air_pollution_in_seoul_new.csv')          # csv
json_size = os.path.getsize('/home/whytech/lab_2/results/air_pollution_in_seoul_new.json')        # json
pickle_size = os.path.getsize('/home/whytech/lab_2/results/air_pollution_in_seoul_new.pkl')       # pickle
msgpack_size = os.path.getsize('/home/whytech/lab_2/results/air_pollution_in_seoul_new.msgpack')  # msgpack

sizes_list = [csv_size, json_size, pickle_size, msgpack_size]

sizes_dict = {'Размер csv': csv_size,
              'Размер json': json_size,
              'Размер pickle': pickle_size,
              'Размер msgpack': msgpack_size,
              'Максимальный размер файла': max(sizes_list),
              'Минимальный размер файла': min(sizes_list)
}

# Статистика для колонок с числовыми данными
columns_stats_num = ['SO2', 'NO2', 'O3', 'CO', 'PM10', 'PM2.5']

stat_num = {}

for column in columns_stats_num:

    stats = df_new[column].describe()
    stat_num[column] = pd.concat([stats[['min', 'max', 'mean', 'std']], pd.Series({'sum': df_new[column].sum()})]).to_dict()

# Статистика для текстовых данных
columns_stats_text = ['Measurement date', 'Station code', 'Latitude', 'Longitude']

stat_text = {}

for column in columns_stats_text:
    stat_text[column] = df_new[column].value_counts().to_dict()

# Сохраняем в json
all_stats = {
    'num_stats': stat_num,
    'text_stats': stat_text
}

with open('/home/whytech/lab_2/results/task_5_solve.json', 'w') as file:
    json.dump([all_stats, sizes_dict], file, ensure_ascii=False, indent=1)

sum_so2 = df_new['SO2'].sum()
print(sum_so2)