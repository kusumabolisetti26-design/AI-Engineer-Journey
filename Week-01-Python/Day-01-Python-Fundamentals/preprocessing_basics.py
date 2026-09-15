import pandas as pd

data = {
    "Name": ["Kusuma", "Meghana", "Madhavi", "Rahul", "Anil"],
    "Age": [20, None, 21, 22, None],
    "Experience": [1, 2, None, 3, 1],
    "Salary": [60000, 50000, 70000, None, 55000]
}

df = pd.DataFrame(data)

print("===== ORIGINAL DATA =====")
print(df)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())
print("\n===== AFTER FILLING AGE =====")

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)
print("\n===== AFTER FILLING EXPERIENCE =====")

df["Experience"] = df["Experience"].fillna(df["Experience"].median())

print(df)
print("\n===== AFTER FILLING SALARY =====")

df["Salary"] = df["Salary"].fillna(df["Salary"].median())

print(df)

print("\n===== FINAL MISSING VALUES =====")

print(df.isnull().sum())

print("\n===== ADDING DUPLICATE =====")

df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

print(df)
print("\n===== DUPLICATE CHECK =====")

print(df.duplicated())

print("\n===== REMOVING DUPLICATES =====")

df = df.drop_duplicates()

print(df)

print("\n===== CLEAN DATASET =====")
print(df)

print("\nRows:", len(df))
print("Columns:", len(df.columns))

df["Skill"] = ["Python", "Java", "AI", "Python", "Java"]

print("\n===== CATEGORICAL DATA =====")
print(df)

print("\n===== ONE-HOT ENCODING =====")

encoded_df = pd.get_dummies(df, columns=["Skill"])

print(encoded_df)

print("\n===== FINAL PREPROCESSED DATA =====")

print(encoded_df)

print("\nMissing values:")
print(encoded_df.isnull().sum())

print("\nRows:", len(encoded_df))