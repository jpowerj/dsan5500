# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| error: true
x = 1 + 1
y = str(x)
print(x)
print(y)
#
#
#
#
#
#| error: true
print(x+1)
print(y+1)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
x = "Ceci n'est pas une string"
print(x)
print(type(x))
print(list(x))
#
#
#
#
#
#
#
#
y = b"Ceci n'est pas une string"
print(y)
print(type(y))
print(list(y))
#
#
#
#
#
#
#
#
print([format(character, 'b') for character in y])
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd
swim_df = pd.read_csv("assets/swimdata.csv", index_col=0)
swim_df.head()
#
#
#
#
#
#
#
#
short_df = swim_df[swim_df['distance'] == "50m"].copy()
short_df.sort_values(['style', 'time'], ascending=True).groupby('style').head(1)
#long_df = data_df[data_df['distance'] == "100m"].copy()
#
#
#
#
#
#
#
#
#
#
#
#
#
#