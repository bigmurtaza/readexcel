# Random xlsx selection. Use while instead of for, when I use for, the list is half length, I have 200 files and it shows an order with 100 files, me not like

import random
import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)
files

files_xlsx = [f for f in files if f[-4:]=='xlsx' and f!='fifam-uids.xlsx' and f!='Teams.xlsx'] 

g = []

while len(files_xlsx):
    a = random.choice(files_xlsx)
    print (a)

    g.append(a)
    files_xlsx.remove(a)
