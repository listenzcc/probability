"""
File: maximum-likelihood-estimation-of-m-knowing-n.py
Author: Chuncheng Zhang
Date: 2024-11-26
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


# %% ---- 2024-11-26 ------------------------
# Requirements and constants
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy.special import comb
from IPython.display import display


# %% ---- 2024-11-26 ------------------------
# Function and class
def phi(k, n, m):
    a = 1
    b = comb(n-1, k-1)
    c = comb(m, k)
    return a*b/c


# %% ---- 2024-11-26 ------------------------
# Play ground
k = 5

res = []

for m in range(10, 30):
    for n in range(k, m+1):
        res.append(dict(k=k, m=m, n=n, p=phi(k, n, m)))

res = pd.DataFrame(res)
display(res)


# %% ---- 2024-11-26 ------------------------
# Pending

pivot = res.pivot(index='m', columns='n', values='p')
display(pivot)

sns.heatmap(pivot, cmap='Blues')
title = 'Conditional prob of n at m and k=5'
plt.title(title)
plt.tight_layout()
plt.savefig(f'./binomial-distribution-img/{title}.png')
plt.show()


# %% ---- 2024-11-26 ------------------------
# Pending
