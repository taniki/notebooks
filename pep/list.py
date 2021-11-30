# ---
# jupyter:
#   jupytext:
#     formats: py:hydrogen
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
from IPython.display import Markdown as md

# %%
df = pd.read_csv('offers/latest.csv')

# %%
content = ""

for idx, offer in df.iterrows():
    content += f'- [{offer["title"]}]({offer["url"]})\n'
    
md(content)

# %%
len(df)

# %%
