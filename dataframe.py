import pandas as pd
import numpy as np

# ---------------------------
# Question 1
# ---------------------------
data1 = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df1 = pd.DataFrame(data1)
print("Question 1:\n", df1, "\n")

# ---------------------------
# Question 2
# ---------------------------
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 
                'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a','b','c','d','e','f','g','h','i','j']
df2 = pd.DataFrame(exam_data, index=labels)
print("Question 2:\n", df2, "\n")

# ---------------------------
# Question 2.1 Basic Info
# ---------------------------
print("Question 2.1: Info")
print(df2.info(), "\n")

# ---------------------------
# Question 2.2 First 3 Rows
# ---------------------------
print("Question 2.2:\n", df2.head(3), "\n")

# ---------------------------
# Question 2.3 Select 'name' and 'score'
# ---------------------------
print("Question 2.3:\n", df2[['name', 'score']], "\n")

# ---------------------------
# Question 2.4 Select specific rows & columns
# ---------------------------
print("Question 2.4:\n", df2.loc[['b','d','f','g'], ['name','score']], "\n")

# ---------------------------
# Question 2.5 attempts > 2
# ---------------------------
print("Question 2.5:\n", df2[df2['attempts'] > 2], "\n")

# ---------------------------
# Question 2.6 Rows and Columns count
# ---------------------------
print("Question 2.6: Rows, Cols = ", df2.shape, "\n")

# ---------------------------
# Question 2.7 score between 15 and 20
# ---------------------------
print("Question 2.7:\n", df2[df2['score'].between(15,20)], "\n")

# ---------------------------
# Question 2.8 attempts < 2 and score > 15
# ---------------------------
print("Question 2.8:\n", df2[(df2['attempts'] < 2) & (df2['score'] > 15)], "\n")

# ---------------------------
# Question 2.9 change score in row 'd' to 11.5
# ---------------------------
df2.loc['d', 'score'] = 11.5
print("Question 2.9:\n", df2, "\n")

# ---------------------------
# Question 2.10 mean of scores
# ---------------------------
print("Question 2.10: Mean Score = ", df2['score'].mean(), "\n")

# ---------------------------
# Question 2.11 append new row 'k', then delete it
# ---------------------------
df2.loc['k'] = ['Ayan', 15, 2, 'yes']
print("After Append:\n", df2, "\n")
df2 = df2.drop('k')
print("After Delete Row 'k':\n", df2, "\n")

# ---------------------------
# Question 2.12 sort by name desc, score asc
# ---------------------------
print("Question 2.12:\n", df2.sort_values(by=['name','score'], ascending=[False,True]), "\n")

# ---------------------------
# Question 2.13 replace qualify yes/no with True/False
# ---------------------------
df2['qualify'] = df2['qualify'].map({'yes': True, 'no': False})
print("Question 2.13:\n", df2, "\n")

# ---------------------------
# Question 2.14 change James to Suresh
# ---------------------------
df2['name'] = df2['name'].replace('James','Suresh')
print("Question 2.14:\n", df2, "\n")

# ---------------------------
# Question 2.15 delete attempts column
# ---------------------------
df2 = df2.drop(columns=['attempts'])
print("Question 2.15:\n", df2, "\n")

# ---------------------------
# Question 2.16 write DataFrame to CSV with tab separator
# ---------------------------
df2.to_csv("exam_data.tsv", sep="\t", index=True)
print("Question 2.16: DataFrame written to exam_data.tsv with tab separator\n")
