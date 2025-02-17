"""
File: experiment-2.py
Author: Chuncheng Zhang
Date: 2025-02-14
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Experiment-1 in real image.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2025-02-14 ------------------------
# Requirements and constants
import numpy as np
from PIL import Image
from tqdm.auto import tqdm


# %% ---- 2025-02-14 ------------------------
# Function and class
def mk_ground_truth():
    img = Image.open('./img-2.jpg').resize((600, 600))
    ground_truth = np.array(img, dtype=np.float32)
    return ground_truth


def add_noise(mat: np.ndarray):
    mat = mat.copy()
    # mat += np.random.randn(*mat.shape) * 50
    mat += np.random.randint(-30, 30, size=mat.shape)
    return mat


def quantize(mat: np.ndarray, quant=70):
    mat = mat.copy()
    mat -= mat % quant
    return mat


def draw_mat(mat):
    mat = mat.copy()
    mat[mat > 255] = 255
    mat[mat < 0] = 0
    display(Image.fromarray(mat.astype(np.uint8)))


# %% ---- 2025-02-14 ------------------------
# Play ground
ground_truth = mk_ground_truth()
qmat = quantize(ground_truth)
rmat = add_noise(ground_truth)
qrmat = quantize(rmat)

draw_mat(ground_truth)
draw_mat(qmat)
draw_mat(qrmat)

# %% ---- 2025-02-14 ------------------------
# Pending
many_qrmats = []
for _ in tqdm(range(100)):
    rmat = add_noise(ground_truth)
    qrmat = quantize(rmat)
    many_qrmats.append(qrmat)
mat = np.mean(many_qrmats, axis=0)
draw_mat(mat)

# %% ---- 2025-02-14 ------------------------
# Pending

# %%
