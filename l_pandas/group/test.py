import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Department': ['Sales', 'Sales', 'IT', 'IT', 'HR'],
    'Employee': ['A', 'B', 'C', 'D', 'E'],
    'Salary': [1000, 1200, 1300, 1100, 900]
})
#print(df)
df_c = df.copy()

print(df_c["Department"], end="\n\n")
print(df_c["Department"].drop_duplicates())
groups = df.groupby('Department')
