"""
RECORD CHECK  -  my version
===========================

Name  :  Navami Pradeep Shetty
Lane  :  AI
Date  :  05/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD

df = pd.read_csv('/Users/navamishetty/Desktop/ /YEAR 1/SEM 1/CST1510 - PROGRAMMING FOR DATA COMMUNICATIONS AND NETWORKS/CST1510/Week 06 - Pandas/LAB/mini_project.csv')

# ================================================================= PROCESS

df['percent'] = (df['value'] / df['limit']) * 100
df['status'] = df['percent'].apply(lambda p: 'OVER LIMIT' if p > 100 else 'WARNING' if p > 90 else 'OK')

# ================================================================== OUTPUT

print(df)

filter = df[df['status'] != 'OK']
print(filter)

grouped = df.groupby('status')
print(grouped['status'].count())

df.to_csv('/Users/navamishetty/Desktop/ /YEAR 1/SEM 1/CST1510 - PROGRAMMING FOR DATA COMMUNICATIONS AND NETWORKS/CST1510/Week 06 - Pandas/LAB/mini_project_final.csv',index = False)

df['status'].value_counts().plot(kind = 'bar')
plt.title('Status counts')
plt.savefig('/Users/navamishetty/Desktop/ /YEAR 1/SEM 1/CST1510 - PROGRAMMING FOR DATA COMMUNICATIONS AND NETWORKS/CST1510/Week 06 - Pandas/LAB/mini_project.png')
plt.show()