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
import os
import requests
import datetime
from dotenv import load_dotenv

# %%
load_dotenv()

# %%
rebuild_endpoint = os.getenv("REBUILD")


# %%
def rebuild():
    res = requests.post(rebuild_endpoint)
    
    return res


# %%
rebuild()

# %%
