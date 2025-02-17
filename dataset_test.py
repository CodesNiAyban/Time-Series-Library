import pandas as pd

file_path = "data/BTCUSDT.csv"
df = pd.read_csv(file_path)

print(df.columns)