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
df = pd.read_csv('~/Downloads/RP2018_LOGEMTZA_csv/FD_LOGEMTZA_2018.csv', sep= ";")

# %%
df.head()

# %%
df.shape

# %% [markdown]
# - source : https://www.insee.fr/fr/statistiques/fichier/5542867/RP2018_LOGEMTZA_csv.zip
# - dictionnaire des variables : https://www.insee.fr/fr/statistiques/5542867?sommaire=5395764#dictionnaire

# %% [markdown]
# ## À faire
#
# - [ ] regroupement par code commune INSEE (python)
#     - [ ] filtrer pour ne garder que les arrondissements de paris
#     - [ ] profil sociodémographique
#     - [ ] faire un indicateur pour classer les différents arrondissements
# - [ ] exporter en CSV et le mettre sur data.gouv.fr
# - [ ] récupérer le profil type des habitants de logements sociaux (python ou observable)
# - [ ] voir l'impact sur le profil sociodémographique si on remplit les logements vacants avec le profil socio-démographique des quartiers les plus pauvres (python ou observable)

# %%
