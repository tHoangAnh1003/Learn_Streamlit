import pandas as pd
import matplotlib.pyplot as plt

file_path = 'result_ndvi_statistic.csv'
df = pd.read_csv(file_path)

# df.head()

df['time_period'] = df['file_path'].apply(lambda x: x.split('/')[-1].split('.')[0])

plt.figure(figsize=(14, 7))

plt.plot(df['time_period'], df['mean'], label='Mean')
plt.plot(df['time_period'], df['max'], label='Max')
plt.plot(df['time_period'], df['min'], label='Min')

plt.xlabel('Tuần')
plt.ylabel('NDVI index')
plt.title('NDVI')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
