import sys
print(sys.prefix)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
from sklearn.preprocessing import LabelEncoder
liver_df = pd.read_csv('C:\\Users\\hp\\Desktop\\ML\\indian_liver_patient.csv',header = 0)
#print('fuck')
print(liver_df.head())

Y = liver_df.values[1:,10:11]
count1 = 0
count2 = 0
for y in Y:
    if y == 1:
        count1 =count1+1
    else:
        count2 = count2+1
print(count1,count2)
liver_df.info()
sns.factorplot(x="Age", y="Gender", hue="Dataset", data=liver_df);
M, F = liver_df['Gender'].value_counts()
print('Number of patients that are male: ',M)
print('Number of patients that are female: ',F)
liver_df[['Gender', 'Dataset','Age']].groupby(['Dataset','Gender'], as_index=False).count().sort_values(by='Dataset', ascending=False)
