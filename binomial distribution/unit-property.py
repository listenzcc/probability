"""
File: unit-property.py
Author: Chuncheng Zhang
Date: 2024-12-09
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-12-09 ------------------------
# Requirements and constants
import math
import pandas as pd
from tqdm.auto import tqdm


# %% ---- 2024-12-09 ------------------------
# Function and class
def comp_p(t, m, k):
    a = math.comb(m-1, k-1)
    b = k-1
    c = math.comb(t, k)
    d = k
    return a*b/c/d


# %% ---- 2024-12-09 ------------------------
# Play ground
res = []
for k in tqdm(range(5, 10), 'k'):
    for m in tqdm(range(12, 20), 'm'):
        for t in range(m, 100):
            p = comp_p(t, m, k)
            res.append((p, t, m, k))

df = pd.DataFrame(res, columns=['p', 't', 'm', 'k'])
df


# %% ---- 2024-12-09 ------------------------
# Pending
group = df.groupby(['m', 'k'])
group['p'].sum()


# %% ---- 2024-12-09 ------------------------
# Pending
