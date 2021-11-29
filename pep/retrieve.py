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
import datetime

import requests
from bs4 import BeautifulSoup

import pandas as pd

from tqdm import tqdm
from tqdm.contrib import tmap
from tqdm.contrib.concurrent import thread_map  # or thread_map

from concurrent.futures import ThreadPoolExecutor, as_completed

import os
from dotenv import load_dotenv

# %%
load_dotenv()
source = os.getenv("PEP_INDEX")

# %%
keywords = [
    'data science',
    'data scientist',
    'data analyst',
    'analyste de données',
    'machine learning',
    'intelligence artificielle'
]

# %%
df = pd.read_csv(source, sep=";")

df['FirstPublicationDate'] = pd.to_datetime(df['FirstPublicationDate'])


# %%
def scrap(offer_id):
    base_url = f"https://place-emploi-public.gouv.fr/offre-emploi/2021-{offer_id}/"
    #print(base_url)
    
    req = requests.get(base_url)
    
    if (req.status_code == 200):
        soup = BeautifulSoup(req.content, 'html.parser')
        # print(soup.prettify())

        title = soup.find('h1', class_="single-title")
#        print(title.getText())

        content = soup.find('section', class_='single-offer-content')
#        print(content.getText())
        return {
            'title': title.getText(),
            'content': content.getText(),
            'url': base_url
        }
    else:
        # print(f"💀 {base_url}")
        return None


# %%
def select(offer):
    fields = offer.keys()

    return any([keyword in offer[field].lower() for keyword in keywords for field in fields])


# %% [markdown]
# ## Retrieval

# %% [markdown]
# ###  Mono-thread

# %%
def retrieve_mono():
    selected = []

    for offer_id in tqdm(df['OfferID']):
        offer = scrap(offer_id)

        if (offer):
            #print(offer['url'])
            match = select(offer)
            if match:
                print(offer['url'])
                print(offer)
                selected.append(offer)
    
    return selected


# %% [markdown]
# ### Multithread

# %%
def retrieve_multi():
    offers = thread_map(scrap, list(df['OfferID']))
    selected = [ offer for offer in offers if offer != None and select(offer)]
    return selected


# %% [markdown]
# ## Persistence

# %%
selected = retrieve_multi()


# %%
def save(offers):
    date = datetime.datetime.now().strftime("%Y%m%d")
    pd.DataFrame(offers).to_csv(f'offers/offers-{date}.csv')
    pd.DataFrame(offers).to_csv(f'offers/latest.csv')


# %%
save(selected)