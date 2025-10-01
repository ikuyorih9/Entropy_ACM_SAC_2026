import pandas as pd

time_csv = "../results/incremental_stats.csv"

df = pd.read_csv(time_csv)
idx = df.groupby("type")["median_time"].idxmin()
df = df.loc[idx].reset_index(drop=True)
print(df)

df = df['compressor'].value_counts().reset_index()
print(df)