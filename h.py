import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

stud_per = pd.read_csv('StudentsPerformance.csv')
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', None)
pd.set_option('expand_frame_repr', True)

print(stud_per.head(7))
#print(stud_per.describe())
#print(stud_per.dtypes)
#print(stud_per.groupby('gender').aggregate({'writing score': 'mean'}))
#print(stud_per.iloc[0:5, 0:3]) - 5 строк, 3 колонки
#print(stud_per.iloc[:, 0])
#print(pd.Series([1,2,3,4,5]))
#print(stud_per.loc[stud_per.gender == 'female'])
#print(stud_per.groupby('lunch').aggregate({'math score':['count', 'mean', 'std'], 'reading score':['count', 'mean', 'std'], 'writing score' :['count', 'mean', 'std']}))
#print(stud_per.groupby('lunch').mean()[['math score']])
#print(stud_per.qury('writing_score > 74'))
#print(stud_per.groupby('gender').aggregate({'math score': 'mean', 'reading score': 'mean'}))
#print(stud_per.sort_values(['gender', 'math score']).groupby('gender').head(5))
stud_per.plot.scatter(x='math score', y='reading score')
plt.show()
#stud_per['total']=stud_per.mathscore + stud_per.reading_score + stud_per.writing_score