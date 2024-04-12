# Pandas: Annotate data points while plotting from DataFrame 

import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'x': [0.79974873, 0.62466539, 0.65046638, 0.22819233, 0.47786481],
    'y': [0.97827185, 0.26413242, 0.88445034, 0.6379751,  0.63235667],
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan']
})

fig, ax = plt.subplots()

df.plot('x', 'y', kind='scatter', ax=ax)

for index, row in df.iterrows():
    ax.annotate(row['name'], (row['x'], row['y']))

ax.set_xlabel('horizontal label')
ax.set_ylabel('vertial label')

plt.show()
