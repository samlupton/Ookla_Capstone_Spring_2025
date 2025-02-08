import pandas as pd

def print_parquet_column_names(file_path):
    try:
        df = pd.read_parquet(file_path)
        for col in df.columns:
            print(col)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")