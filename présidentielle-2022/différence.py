# -*- coding: utf-8 -*-
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
pd.set_option("display.float_format", lambda x: '{:,.2f}'.format(x).replace(",", " "))

# %%
df = (pd
    .read_html(
        "https://www.resultats-elections.interieur.gouv.fr/presidentielle-2022/FE.html",
        thousands=" ",
        decimal=",",
    )
    [1]
    .assign(
        diff = lambda df_: (df_["Voix"]
            .rolling(window=2)
            .apply(lambda s : -(s.iloc[0] - s.iloc[1]))
        )
    )
)

df

# %%
df.dtypes

# %%
url_2017 = "https://www.interieur.gouv.fr/Elections/Les-resultats/Presidentielles/elecresult__presidentielle-2017/(path)/presidentielle-2017//FE.html"

df_2017 = (pd
    .read_html(url_2017, encoding="utf-8",
        thousands=" ",
        decimal=",",)
    [2]
)

df_2017

# %%
(pd
    .merge(df, df_2017, on="Liste des candidats", suffixes=('_2022', '_2017'))
    [["Liste des candidats", "Voix_2017", "Voix_2022"]]
    .assign(
        difference = lambda df_: df_["Voix_2022"] - df_["Voix_2017"],
        pct = lambda df_: df_["Voix_2022"] / df_["Voix_2017"] - 1
    )
    .set_index("Liste des candidats")
    .style
        .format(thousands=" ",
            formatter={'pct': '{:,.2%}'.format}
#            formatter = {('difference'): lambda x: "🔼 "+str(x) if x > 0 else "🔽 "+str(x) }
        )
)

# %%
