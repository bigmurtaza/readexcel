import os 
import shutil

files = os.listdir('D:\FIFA Manager Stadium Project\Team Spreadsheet Template\leagues')
files = {x.replace(".txt", "") for x in files}

# Sort by alphabet
files = sorted(files) 
# Convert set to list
files = list(files)

print(files)

# Copied a file with a list of names!
for x in files:
    shutil.copy("D:\FIFA Manager Stadium Project\Team Spreadsheet Template\SampleNew.xlsx", f"D:\FIFA Manager Stadium Project\Team Spreadsheet Template\Leagues\{x}.xlsx")
