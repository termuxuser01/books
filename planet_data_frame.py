import pandas as pd

pandas_df = pd.read_csv('http://0.0.0.0/planets.csv', index_col='Name')
print(pandas_df)
pandas_df.to_csv('./pandas.csv')