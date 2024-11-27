"""
File: program-proof.py
Author: Chuncheng Zhang
Date: 2024-11-27
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


# %% ---- 2024-11-27 ------------------------
# Requirements and constants
import random
import numpy as np


# %% ---- 2024-11-27 ------------------------
# Function and class
# Change the k and m, and make sure m > k
for _ in range(100):
    a = random.randint(10, 100)
    b = random.randint(10, 100)

    if a > b:
        k = b
        m = a

    if a < b:
        k = a
        m = b

    if a == b:
        continue

    array = [k/m]
    for x in range(1, 1000):
        v = array[x-1] * (m+x-k) / (m+x)
        array.append(v)

    # It produces two values which are the same.
    print(k, m, np.sum(array), k/(k-1))


# %% ---- 2024-11-27 ------------------------
# Play ground


# %% ---- 2024-11-27 ------------------------
# Pending


# %% ---- 2024-11-27 ------------------------
# Pending
