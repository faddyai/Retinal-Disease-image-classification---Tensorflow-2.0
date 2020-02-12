1

import os
import pandas as pd

BASE_DIR = 'C:/Users/fad/Desktop/OCT2017/train/NORMAL/'
train_folder = BASE_DIR
train_annotation = BASE_DIR

files_in_train = sorted(os.listdir(train_folder))
files_in_annotated = sorted(os.listdir(train_annotation))

images=[i for i in files_in_train if i in files_in_annotated]

df = pd.DataFrame()
df['images']=[train_folder+str(x) for x in images]
df['labels']=[train_annotation+str(x) for x in images]

df.to_csv('newNORMSS.csv', header=None)