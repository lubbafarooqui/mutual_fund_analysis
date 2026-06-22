import pandas as pd

df = pd.read_csv("data/raw/fund_master.csv")

print("\n===== UNIQUE FUND HOUSES =====")
print(df["fund_house"].unique())

print("\n===== CATEGORIES =====")
print(df["category"].unique())

print("\n===== SUB CATEGORIES =====")
print(df["subcategory"].unique())

print("\n===== RISK GRADES =====")
print(df["risk_grade"].unique())