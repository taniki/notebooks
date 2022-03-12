# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# %%
df = pd.read_csv('WID_data_FR.csv', sep=";")

# %%
df

# %%
df.loc[df['value'] == 42926]

# %%
# tptinc992j income before tax

income = df.loc[
    df['variable'].str.contains('tptinc992j')
#     * ~df['percentile'].str.contains('p100')
#     * ~df['percentile'].str.contains('p0')
    * df['year'] == 2021
][
    ['percentile','value']
]

income.reset_index(drop=True, inplace=True)

income

# %%
income.to_csv('wid-2021-income.csv')

# %%
wealth = df.loc[
    df['variable'].str.contains('thweal992j')
#    * ~df['percentile'].str.contains('p100')
    * df['year'] == 2020
][
    ['percentile','value']
]

wealth.reset_index(drop=True, inplace=True)

wealth

# %%
wealth.to_csv('wid-2020-wealth.csv')

# %%
wealth[ wealth['value'] > 60000 ]

# %%
wealth[ wealth['value'] > 50000 ].sort_values(by=['value'])

# %%
