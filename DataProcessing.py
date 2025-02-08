import pandas as pd
from ColumnTitles import * 

parquet_file_path = '2024-01-01_performance_mobile_tiles.parquet'

df = pd.read_parquet(parquet_file_path)
print(df.head())
print("Number of columns in this file:", df.size)

print_parquet_column_names(parquet_file_path)