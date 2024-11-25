"""
File: dense.py
Author: Chuncheng Zhang
Date: 2024-11-21
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Compare the scipy's dense representation with the theory value.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-11-21 ------------------------
# Requirements and constants
import scipy.stats
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from tqdm.auto import tqdm
from rich import print
from IPython.display import display


# %% ---- 2024-11-21 ------------------------
# Function and class
def pmf(n: int, x: int, p: float, a: float = None, b: float = None) -> float:
    q = 1-p
    res = 1
    num1 = range(1, n+1)
    num2 = [p]*x + [q]*(n-x)

    if a:
        num3 = [a]*x + [b] * (n-x)
    else:
        num3 = [1.0] * n

    den1 = list(range(1, x+1)) + list(range(1, n-x+1))

    for n1, n2, n3, d1 in zip(num1, num2, num3, den1):
        if a:
            res *= n1 * n2 * n3 / d1
        else:
            res *= n1 * n2 / d1

    return res


palette = 'flare'

# %% ---- 2024-11-21 ------------------------
# Play ground
m = 10
p = 0.5
a = 9.0
b = 0.1

dfs = []
for m in tqdm([3, 5, 7, 10, 20, 30]):
    bino = scipy.stats.binom(n=m, p=p)
    x_values = np.array(range(m+1))
    df = pd.DataFrame(x_values, columns=['x'])
    df['x_norm'] = df['x'] / m
    df['m'] = m
    df['pmf'] = df['x'].map(lambda x: bino.pmf(x))
    df['y'] = df['x'].map(lambda x: 1/m*bino.pmf(x) * (a*x + b*(m-x)))
    df['y2'] = df['x'].map(lambda x: 1/m/m*bino.pmf(x) *
                           np.power(a*x + b*(m-x), 2))
    dfs.append(df)

df = pd.concat(dfs)
display(df)

group = df.groupby('m')
df1 = group.sum()
df1['var'] = df1['y2'] - df1['y'] * df1['y']
df1['std'] = df1['var'].map(np.sqrt)
display(df1)

# Graph

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
# ax = axes[0]
# sns.lineplot(df, x='x_norm', y='pmf', hue='m', ax=ax, palette=palette)
# ax.set_title('Probability density function')

ax = axes[0]
sns.lineplot(df, x='x_norm', y='y', hue='m', ax=ax,
             palette=palette, legend=False)
ax.set_title('Expectation on separating')

ax = axes[1]
sns.lineplot(df1, x='m', y='std', color='gray', ax=ax)
sns.scatterplot(df1, x='m', y='std', hue='m', palette=palette, ax=ax)
ax.set_title('Std. shrinkage on m increasing')

fig.tight_layout()
fig.savefig('img/separating.png')
plt.show()


# %%
# Computation Exponential boom
n = 60
p = 0.5
a = 9.0
b = 0.1

dfs = []

for n in tqdm([10, 20, 30, 40, 50, 60], 'Computing'):
    bino = scipy.stats.binom(n=n, p=p)

    x_values = np.array(range(n+1))
    df = pd.DataFrame(x_values, columns=['x'])
    df['x_norm'] = df['x'] / n
    df['n'] = n
    df['pmf'] = df['x'].map(lambda x: bino.pmf(x))
    df['pmf_e'] = df['x'].map(lambda x:
                              bino.pmf(x) * np.power(a, x) * np.power(b, n-x))
    df['pmf_log'] = df['x'].map(lambda x:
                                bino.pmf(x) * np.log(np.power(a, x) * np.power(b, n-x)))
    df['high'] = df['x'].map(lambda x: pmf(n, x, p))
    df['high_e'] = df['x'].map(lambda x: pmf(n, x, p, a, b))

    dfs.append(df)

df = pd.concat(dfs)
display(df)

# Graph
df['compare'] = df['high'] / df['pmf']
df['compare_e'] = df['high_e'] / df['pmf_e']

sns.set_theme('paper')
fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=200)
ax = axes[0, 0]
sns.lineplot(df, x='x_norm', y='pmf', hue='n', ax=ax, palette=palette)
ax.set_xlabel('x')
ax.set_title('Probability density function')

ax = axes[0, 1]
sns.lineplot(df, x='x_norm', y='pmf_e', hue='n',
             ax=ax, palette=palette, legend=False)
ax.set_yscale('log')
ax.vlines(0.5, ymin=df['pmf_e'].min(), ymax=df['pmf_e'].max(), color='gray')
ax.hlines(1, xmin=0, xmax=1, color='gray')
ax.set_xlabel('x')
ax.set_title('Earns (raw)')

gs = gridspec.GridSpec(2, 2)
ax = fig.add_subplot(gs[1, :])

sns.lineplot(df, x='x_norm', y='pmf_log', hue='n',
             ax=ax, palette=palette, legend=False)
ax.vlines(0.5, ymin=-1, ymax=1, color='gray')
ax.hlines(0.0, xmin=0, xmax=1, color='gray')
ax.set_xlabel('x')
ax.set_title('Earns (log)')

axes[1, 0].axis('off')
axes[1, 1].axis('off')

fig.tight_layout()
fig.savefig('img/exponential boom.png')
plt.show()

# %% ---- 2024-11-21 ------------------------
# Pending


# %% ---- 2024-11-21 ------------------------
# Pending

# %%

# %%
