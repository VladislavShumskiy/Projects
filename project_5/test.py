import pandas as pd
import os
pa = os.path.dirname(__file__)
files = os.listdir(pa)
text_files = []
for i in files:
    if i[-4:] == '.txt':
        text_files.append(i)
b = pd.read_csv(os.path.join(pa,text_files[1]), header=0, names = ['a', 'b'])
new_col = []
for i in range(b.shape[0]):
    new_col.append(0)
b['c'] = new_col
print(b)
b.to_csv(os.path.join(pa, text_files[1].replace('.txt', '_mod.txt')))