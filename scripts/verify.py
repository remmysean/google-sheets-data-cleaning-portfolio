import pandas as pd

df = pd.read_csv('data/cleaned_tickets.csv')

print("Rows:", len(df))
print("\nCategories:")
print(df['clean_category'].value_counts())
print("\nUnique categories:", df['clean_category'].nunique())
print("Avg response time (hours):", df.iloc[:, -1].mean())