# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Production d'un csv utilisable de la base FINESS
#
# En l'état, l'export CSV de la [base FINESS][finess] n'est pas vraiment satisfaisant et utilisable.
#
# - Le fichier n'est pas réellement un CSV.
#     - Il est bizarrement découpé en deux sections qui correspondent au XML.
#     - Les colonnes n'ont pas de nom.
# - Le fichier est encodé au format windows.
#
# [finess]: https://www.data.gouv.fr/en/datasets/finess-extraction-du-fichier-des-etablissements/

# %% gradient={"editing": false, "id": "4facc182", "kernelId": ""}
import pandas as pd
import numpy as np
import requests

# %% gradient={"editing": false, "id": "3f7b5d32", "kernelId": ""}
dataset_api = "https://www.data.gouv.fr/api/1/datasets/finess-extraction-du-fichier-des-etablissements/"

# %% gradient={"editing": false, "id": "58d641d4", "kernelId": ""}
resources = (requests
    .get(dataset_api)
    .json()
    ['resources']
)

resource_geoloc = [ r for r in resources if r['type'] == 'main' and 'géolocalisés' in r['title']][0]

# %% gradient={"editing": false, "id": "13dd939b", "kernelId": ""}
headers = [
    'section',
    'nofinesset',
    'nofinessej',
    'rs',
    'rslongue',
    'complrs',
    'compldistrib',
    'numvoie',
    'typvoie',
    'voie',
    'compvoie',
    'lieuditbp',
    'commune',
    'departement',
    'libdepartement',
    'ligneacheminement',
    'telephone',
    'telecopie',
    'categetab',
    'libcategetab',
    'categagretab',
    'libcategagretab',
    'siret',
    'codeape',
    'codemft',
    'libmft',
    'codesph',
    'libsph',
    'dateouv',
    'dateautor',
    'maj',
    'numuai'
]

# %% gradient={"editing": false, "id": "b68dac89", "kernelId": ""}
geoloc_names = [
    'nofinesset',
    'coordxet',
    'coordyet',
    'sourcecoordet',
    'datemaj'
]

# %% gradient={"editing": false, "id": "4492d3dd", "kernelId": ""}
raw_df = (pd
    .read_csv(resource_geoloc['url'],
              sep=";", encoding="Windows-1252", header=None, skiprows=1,
              dtype='str',
              names=headers)
    .drop(columns=['section'])
)

raw_df

# %% gradient={"editing": false, "id": "2efc14bc", "kernelId": ""}
structures = (raw_df
    .iloc[:int(raw_df.index.size/2)]
)

structures

# %% gradient={"editing": false, "id": "283be3bb", "kernelId": ""}
geolocalisations = (raw_df
    .iloc[int(raw_df.index.size/2):]
    .drop(columns=raw_df.columns[5:])
    .rename(columns=lambda x: geoloc_names[list(raw_df.columns).index(x)])
)

geolocalisations

# %% gradient={"editing": false, "id": "b54e527e", "kernelId": ""}
clean_df = (structures
    .merge(geolocalisations, on="nofinesset", how="left")
)

clean_df

# %%
clean_df.sample().T

# %%
clean_df["siret"]

# %% [markdown] gradient={"editing": false, "id": "82306369-229c-418f-9138-d753e1b71ce4", "kernelId": ""}
# ## Vérification de la qualité des données

# %% gradient={"editing": false, "id": "64975e82-5f97-4bb4-b1d3-8aed85fa37cd", "kernelId": "", "source_hidden": false} jupyter={"outputs_hidden": false}
intersection = pd.Series(np.intersect1d(structures.nofinesset.values, geolocalisations.nofinesset.values))

intersection.shape

# %% gradient={"editing": false, "id": "07e3c1cb-7032-4d83-833c-0979d2592f3c", "kernelId": "", "source_hidden": false} jupyter={"outputs_hidden": false}
only_structures = (structures
    [ ~structures.nofinesset.isin(intersection) ]
)

only_structures

# %% gradient={"editing": false, "id": "cfb13e95-b622-4d89-be56-61397dc4370e", "kernelId": "", "source_hidden": false} jupyter={"outputs_hidden": false}
only_geolocalisations = (geolocalisations
    [ ~geolocalisations.nofinesset.isin(intersection) ]
)

only_geolocalisations

# %% gradient={"editing": false, "id": "92cd9e34-74c8-454c-96d8-3c628e7b94bd", "kernelId": "", "source_hidden": false} jupyter={"outputs_hidden": false}
geolocalisations_missing = []

# %% [markdown] gradient={"editing": false, "id": "ff24d2da-6b7e-49ca-8ac9-cc1e90d32235", "kernelId": ""}
# ## Export final

# %% gradient={"editing": false, "id": "8f6f3c73-4c14-4e82-ac63-cdf9ab8e4b21", "kernelId": "", "source_hidden": false} jupyter={"outputs_hidden": false}
clean_df.to_csv('finess-clean.csv', encoding='utf-8')

# %%
