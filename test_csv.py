import pandas as pd

# Load CSV
df = pd.read_csv("data/weatherHistory.csv")

# Fill missing values in 'Precip Type' with mode (most common value)
df["Precip Type"].fillna(df["Precip Type"].mode()[0], inplace=True)

# Confirm cleaning
print("Missing values after cleaning:")
print(df.isnull().sum())