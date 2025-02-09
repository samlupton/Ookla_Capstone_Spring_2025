import pandas as pd
from ColumnTitles import * 

parquet_file_path = '2024-01-01_performance_mobile_tiles.parquet'
df = pd.read_parquet(parquet_file_path)
print(df.head())
print("Number of columns in this file:", df.size)
print_parquet_column_names(parquet_file_path)

column_values = df['avg_lat_down_ms']

for value in column_values: 
    print(value)

column_values = df['tile_y']

for value in column_values: 
    print(value)