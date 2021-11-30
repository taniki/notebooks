# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DGFR_API_KEY")

dataset = "619cf721d75793df6b628065"


def publish(filename):
    headers = {
        'X-API-KEY': api_key,
    }

    url = f'https://www.data.gouv.fr/api/1/datasets/{dataset}/upload/'
    
    response = requests.post(url, files={
        'file': open(filename, 'rb'),
    }, headers=headers)
    
    resource = response.json()
    
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    
    resource_url = f'https://www.data.gouv.fr/api/1/datasets/{dataset}/resources/{resource["id"]}/'
    
    res = requests.put(resource_url, json={
        'title': f'offres à la date du {date}'
    },headers=headers)


publish('offers/latest.csv')
