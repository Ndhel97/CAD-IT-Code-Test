import json
import pandas as pd

f = open('sensor_data.json', 'r')
data_sensor = json.load(f)

df = pd.DataFrame(data_sensor['array'])
df['timestamp'] = df['timestamp'] / 1000
df['date'] = pd.to_datetime(df['timestamp'], unit='s').dt.date  # convert timestamp to date

df_min = df.groupby(['roomArea', 'date']).min()[['temperature', 'humidity']] \
    .rename(columns={'temperature': 'min_temp', 'humidity': 'min_humidity'})
df_max = df.groupby(['roomArea', 'date']).max()[['temperature', 'humidity']] \
    .rename(columns={'temperature': 'max_temp', 'humidity': 'max_humidity'})
df_median = df.groupby(['roomArea', 'date']).median()[['temperature', 'humidity']] \
    .rename(columns={'temperature': 'median_temp', 'humidity': 'median_humidity'})
df_mean = df.groupby(['roomArea', 'date']).mean()[['temperature', 'humidity']] \
    .rename(columns={'temperature': 'mean_temp', 'humidity': 'mean_humidity'})

result = pd.concat([df_min, df_max, df_median, df_mean], axis=1)
f.close()
print(result)
result.to_json('./output_sensor_aggregation.json', orient='table')

