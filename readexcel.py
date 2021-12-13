# First I want to reach all files at directory "D:\FIFA Manager Stadium Project\Team Spreadsheet Yeni\" so that I have all the data. I need to make sure I read ALL The excels
# import necessary libraries

import os
import pandas as pd
import numpy as np

# List of files in a directory
# print(glob.glob("D:\FIFA Manager Stadium Project\Team Spreadsheet Yeni\*.xlsx"))

path = os.getcwd()
files = os.listdir(path)
files

files_xlsx = [f for f in files if f[-4:]=='xlsx']
files_xlsx

df = pd.DataFrame()

#Burada tüm veriler birleşecek :D

for f in files_xlsx:
    data = pd.read_excel(f)
    data.columns=[column.replace("Do we have a stadium?", "is_stadium_exist") for column in data.columns]

    df = df.append(data)
    df.drop(df.columns[4:], axis=1, inplace=True)

    df['is_stadium_exist'] = df['is_stadium_exist'].str.replace('+',"True", regex=True)
    df=df.fillna("False")

league = input("league?")
dg=df.loc[df['League'] == league]
print(dg)

# df append, df drop'tan sonra geldiği için en son dosyadan sütunlar eksilmedi. Sıra önemli. Önce organizasyon.
