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
    "data science",
    "data scientist",
    "data analyst",
    "analyste de données",
    "machine learning",
    "intelligence artificielle",
]

# %%
df = pd.read_csv(source, sep=";")

df["FirstPublicationDate"] = pd.to_datetime(df["FirstPublicationDate"])


# %%
def scrap(offer_id, save=False):
    base_url = f"https://place-emploi-public.gouv.fr/offre-emploi/{offer_id}/"
    # print(base_url)

    req = requests.get(base_url)

    if req.status_code == 200:
        soup = BeautifulSoup(req.content, "html.parser")
        # print(soup.prettify())

        title = soup.find("h1", class_="single-title")
        #        print(title.getText())

        content = soup.find("section", class_="single-offer-content").get_text()
        #        print(content.getText())

        parts = soup.find_all("li", class_="offer-subtitle-section-part")
        
        org = None
        dep = None
        
        for part in parts:
            spans = part.find_all('span')
            if (len(spans) >= 2):
                if (spans[0].get_text() == "Employeur"):
                    org = spans[1].get_text().strip()
                elif (spans[0].get_text() == "Organisme de rattachement"):
                    dep = spans[1].get_text().strip()
        
        return {
            "title": title.getText(),
            "content": content,
            "organization": org,
            "department": dep,
            "id": offer_id,
            "url": base_url,
        }
    else:
        # print(f"💀 {base_url}")
        return None

# test
# scrap("MEF_2021-5172")


# %%
def select(offer):
    fields = offer.keys()

    return any(
        [keyword in offer[field].lower() for keyword in keywords for field in fields if offer[field] != None ]
    )


# %% [markdown]
# ## Retrieval

# %% [markdown]
# ###  Mono-thread

# %%
def retrieve_mono():
    selected = []

    for offer_id in tqdm(df["OfferID"]):
        offer = scrap(offer_id)

        if offer:
            # print(offer['url'])
            match = select(offer)
            if match:
                print(offer["url"])
                print(offer)
                selected.append(offer)

    return selected


# %% [markdown]
# ### Multithread

# %% [markdown]
# - scrapping d'environ 5500 pages
# - ~5 minutes sur mbp à Ségur
# - ~20 minutes sur github action

# %%
def retrieve_multi():
    res = thread_map(scrap, list(df["Offer_Reference_"]))
    offers = [o for o in res if o != None]

    return offers


# %%
offers = retrieve_multi()

# %% [markdown]
# ## Persistence

# %%
pd.DataFrame(offers).to_csv("offers/all.csv")

# %%
selected = [offer for offer in offers if offer != None and select(offer)]

# %%
print("annonces sélectionnées : " + str(len(selected)))


# %%
def save(offers):
    date = datetime.datetime.now().strftime("%Y%m%d")
    pd.DataFrame(offers).to_csv(f"offers/offers-{date}.csv")
    pd.DataFrame(offers).to_csv(f"offers/latest.csv")


# %%
save(selected)

# %%
select(scrap("MEF_2021-5172"))

# %%
len(offers)

# %%
[id for id in pd.DataFrame(offers)["id"] if id == "MEF_2021-5172"]

# %%
[id for id in df["Offer_Reference_"] if id == "MEF_2021-5172"]

# %%
