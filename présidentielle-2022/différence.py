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
df = (pd
    .read_html("https://www.resultats-elections.interieur.gouv.fr/presidentielle-2022/FE.html",
        thousands=" ",
        decimal=",")
    [1]
    .assign(**{
            "diff": lambda df_: (df_["Voix"]
                .rolling(window=2)
                .apply(lambda s : -(s.iloc[0] - s.iloc[1])))
    })
)

df

# %%
