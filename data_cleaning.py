
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print("Original Dataset")
print(df.head())

print("Missing Values")
print(df.isnull().sum())

print("Duplicate Records")
print(df.duplicated().sum())

df = df.drop_duplicates()

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["Cabin"] = df["Cabin"].fillna("Unknown")

df["Age"] = df["Age"].astype(float)

df["Fare"] = df["Fare"].astype(float)

df.columns = df.columns.str.strip()

df.to_csv("cleaned_titanic.csv", index=False)

print("Data cleaning completed successfully!")