import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

for file in csv_files:

    print("\n" + "=" * 60)
    print(f"FILE: {file}")

    try:
        df = pd.read_csv(os.path.join(DATA_PATH, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")

print("\nData Ingestion Completed")