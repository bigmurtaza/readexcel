# This python file checks if the folder exists with related name. I plan to change value of 'folder' with actual folder existence.

import os
import pandas as pd

d = {'UID': ["00010002", "00010004"], 'folder': ['a', 'a']}
df = pd.DataFrame(data=d)

for a in d['UID']:
    if os.path.isdir(f'D:\FIFA Manager 14\data\stadium\FIFA\{a}'):
        print("yes")
    else:
        print("no")
