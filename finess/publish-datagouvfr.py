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
import os
import requests
import datetime
from dotenv import load_dotenv

# %%
load_dotenv()

# %%
api_key = os.getenv("DGFR_API_KEY")

# %%
resource = "3dc9b1d5-0157-440d-a7b5-c894fcfdfd45"


# %%
def publish(filename):
    headers = {
        'X-API-KEY': api_key,
    }

    resource_url = f'https://www.data.gouv.fr/api/1/datasets/community_resources/{resource}/upload/'

    response = requests.post(resource_url, files={
        'file': open(filename, 'rb'),
    }, headers=headers)
    
    return response


# %%
result = publish('finess-clean.csv')

# %% [markdown]
# lien de téléchargement de la ressource : https://www.data.gouv.fr/en/datasets/r/3dc9b1d5-0157-440d-a7b5-c894fcfdfd45

# %%
result

# %%
