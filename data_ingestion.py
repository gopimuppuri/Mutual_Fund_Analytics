import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

for file in csv_files:

    print("\n" + "=" * 60)
    print(f"FILE: {file}")

    df = pd.read_csv(os.path.join(DATA_PATH, file))

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

print("\nData Ingestion Completed")