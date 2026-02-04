import pandas as pd


data = {
    "Name":["LITU","DEBA","JIBAN"],
    "Age":[24,23,22],
    "City":["Bhubanswar","jajpur","Cuttack"]
}

# df = pd.DataFrame(data)
# print(df)
# df.to_excel("data.xlsx",index=False)

df = pd.read_excel("data.xlsx")
print(df)