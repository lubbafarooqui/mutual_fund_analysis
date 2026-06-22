import pandas as pd
import os

RAW_FOLDER = "data/raw"


def inspect_csv(file_path, file_name):
    try:
        print("\n" + "=" * 70)
        print(f"FILE: {file_name}")

        df = pd.read_csv(file_path)

        print("\n1. Shape")
        print(df.shape)

        print("\n2. Data Types")
        print(df.dtypes)

        print("\n3. First 5 Rows")
        print(df.head())

        print("\n4. Data Quality Checks")

        print("\nMissing Values:")
        print(df.isnull().sum())

        duplicates = df.duplicated().sum()
        print(f"\nDuplicate Rows: {duplicates}")

        if len(df.columns) != len(df.columns.unique()):
            print("Duplicate column names found")

        print("\nInspection Complete")

    except Exception as e:
        print(f"\nError reading {file_name}")
        print(e)


def main():

    if not os.path.exists(RAW_FOLDER):
        print("Folder not found:", RAW_FOLDER)
        return

    csv_files = [
        f for f in os.listdir(RAW_FOLDER)
        if f.endswith(".csv")
    ]

    print(f"\nTotal CSV Files Found: {len(csv_files)}")

    for file in csv_files:

        path = os.path.join(RAW_FOLDER, file)

        inspect_csv(path, file)


if __name__ == "__main__":
    main()