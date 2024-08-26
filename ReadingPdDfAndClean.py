import pandas as pd

df = pd.read_csv("sample_grpr_input.csv")
print(df)

#Counting the null values in keyword column
nullvals=df["Keyword"].isnull().sum()
print("Number of null values in Keyword Column: ", nullvals)

#Storing rows with not null values in the keyword column
df = df[df["Keyword"].notna()]
print(df)

#Counting the null values in volume column
nullvals=df["Volume"].isnull().sum()
print("Number of null values in Volume Column: ",nullvals)

#Storing rows with not null values in the keyword column
df = df[df["Volume"].notna()]
print(df)

#Replacing Null values with a default value in CPC and CPS columns, 1 for CPC, 0.1 for CPS
df["CPC"].fillna(1, inplace=True)
df["CPS"].fillna(0.1, inplace=True)

print(df)

df.to_csv("CleanedUpInput.csv")

