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
df = pd.read_csv('~/Downloads/RP2018_LOGEMTZA_csv/FD_LOGEMTZA_2018.csv', sep= ";")

# %%
df.head()

# %% [markdown]
# source : https://www.insee.fr/fr/statistiques/fichier/5542867/RP2018_LOGEMTZA_csv.zip
# dictionnaire des variables : https://www.insee.fr/fr/statistiques/5542867?sommaire=5395764#dictionnaire
