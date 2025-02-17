"""
File: experiment-1.py
Author: Chuncheng Zhang
Date: 2025-02-13
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    What will happen if Images are randomized enough?

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2025-02-13 ------------------------
# Requirements and constants
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tqdm.auto import tqdm
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# %% ---- 2025-02-13 ------------------------
# Function and class
def mk_ground_truth():
    size = (100, 1000)
    ground_truth = np.zeros(size)
    for i in range(size[0]):
        ground_truth[i] = np.linspace(50, 200, size[1], endpoint=False)
    return ground_truth


def add_noise(mat: np.ndarray):
    mat = mat.copy()
    # mat += np.random.randn(*mat.shape) * 50
    mat += np.random.randint(-30, 30, size=mat.shape)
    return mat


def quantize(mat: np.ndarray, quant=50):
    mat = mat.copy()
    mat -= mat % quant
    return mat


# %% ---- 2025-02-13 ------------------------
# Play ground
ground_truth = mk_ground_truth()
qmat = quantize(ground_truth)
rmat = add_noise(ground_truth)
qrmat = quantize(rmat)

display(Image.fromarray(ground_truth.astype(np.uint8)))
display(Image.fromarray(qmat.astype(np.uint8)))
display(Image.fromarray(qrmat.astype(np.uint8)))

# %%
many_qrmats = []
for _ in tqdm(range(100)):
    rmat = add_noise(ground_truth)
    qrmat = quantize(rmat)
    many_qrmats.append(qrmat)
mean_qrmat = np.mean(many_qrmats, axis=0).astype(np.uint8)
display(Image.fromarray(mean_qrmat))

# %%
gt0 = ground_truth[0]

sns.set_theme(context='paper')
sns.lineplot(data=mean_qrmat[0], label='Mean QR Mat Row 0')
sns.lineplot(data=np.mean(mean_qrmat, axis=0), label='Mean of Mean QR Mat')
sns.lineplot(data=qmat[0], label='Quantized Ground Truth Row 0')
sns.lineplot(data=gt0, label='Ground Truth Row 0')
plt.legend()
plt.show()

sns.lineplot(data=np.mean(mean_qrmat, axis=0)-gt0, label='Mean of Mean QR Mat')
sns.lineplot(data=qmat[0]-gt0, label='Quantized Ground Truth Row 0')
sns.lineplot(data=gt0-gt0, label='Ground Truth Row 0')
plt.legend()
plt.show()


# %% ---- 2025-02-13 ------------------------
# Pending


# %% ---- 2025-02-13 ------------------------
# Pending
