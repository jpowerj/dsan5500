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
#| label: plot-langs
#| code-fold: true
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "notebook"
lang_df = pd.read_csv("assets/gh_issues.csv")
# The data for 2022 is essentially useless
lang_df = lang_df[lang_df['year'] <= 2021].copy()
lang_df['time'] = lang_df['year'].astype(str) + "_" + lang_df['quarter'].astype(str)
lang_df['prop'] = lang_df['count'] / lang_df.groupby('time')['count'].transform('sum')
lang_df.head()
#sns.lineplot(data=lang_df, x='year', y='count', color='name')
# Keep only most popular languages
keep_langs = ['Python','JavaScript','C','C++','C#','Java','Ruby']
pop_df = lang_df[lang_df['name'].isin(keep_langs)].copy()
fig = px.line(pop_df,
  x='time', y='prop', color='name',
  template='simple_white', title='Programming Language Popularity Since 2012',
  labels = {
    'time': 'Year',
    'prop': 'Proportion of GitHub Issues'
  }
)
fig.update_layout(
  xaxis = dict(
    tickmode = 'array',
    tickvals = [f"{year}_1" for year in range(2012,2022)],
    ticktext = [f"{year}" for year in range(2012,2022)]
  )
)
fig.show()
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
#| code-fold: show
#| label: py-memory-example
import datetime
import pandas as pd
country_df = pd.read_csv("assets/country_pop.csv")
pop_col = country_df['pop']
num_rows = len(country_df)
filled = all(~pd.isna(country_df))
alg_row = country_df.loc[country_df['name'] == "Algeria"]
num_cols = len(country_df.columns)
username = "Jeff"
cur_date = datetime.datetime.now()
i = 0
j = None
z = 314
country_df
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
#| label: indentation-example
for i in range(5):
    print(i)
#
#
#
#| label: indentation-2
#| error: true
for i in range(5):
print(i)
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
#| label: type-hints
def multiply(thing1, thing2):
  return thing1 * thing2
print(multiply(5, 3))
print(multiply("fiveee", 3))
#
#
#
#
#
#
#| label: type-hints-safe
from numbers import Number
def multiply(thing1: Number, thing2: Number) -> Number:
  return thing1 * thing2
print(multiply(5, 3))
print(multiply("fiveee", 3))
#
#
#
#
#
#
from mypy import api
result = api.run(['-c',_i])
print(result[0])
#
#
#
