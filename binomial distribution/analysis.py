"""
File: analysis.py
Author: Chuncheng Zhang
Date: 2024-11-18
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Analysis the binomial distribution problem.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-11-18 ------------------------
# Requirements and constants
import scipy.stats
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from rich import print
from tqdm.auto import tqdm
from IPython.display import display


# %% ---- 2024-11-18 ------------------------
# Function and class

precision_buffer = []


class Binomial(object):
    a = 0.1
    b = 9.0
    p = 0.5
    n = 10
    compute_in_log = True

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
        self.mk_binomial()

    def mk_binomial(self):
        self.binominal = scipy.stats.binom(self.n, self.p)
        return self.binominal

    def compute_pmf(self, hue=None):
        x = np.array([m for m in range(self.n+1)])
        y = np.array([self.pmf(m) for m in x])
        expectation = np.sum(y)

        df = pd.DataFrame(x, columns=['x'])
        df['nx'] = df['x'] / n
        df['y'] = y
        df['hue'] = hue
        df['name'] = 'pmf'
        self.df_pmf = df

        return expectation

    def compute_dist(self, hue=None):
        x = np.array([m for m in range(self.n+1)])
        y = np.array([self.g(m) for m in x])
        [self.f(m) for m in x]
        expectation = np.sum(y)

        df = pd.DataFrame(x, columns=['x'])
        df['nx'] = df['x'] / n
        df['y'] = y
        df['hue'] = hue
        df['name'] = 'dist'
        self.df_dist = df

        self.e = expectation
        return expectation

    def get_result(self, hue=None):
        if not hasattr(self, 'e'):
            self.compute_dist(hue=hue)

        return dict(
            a=self.a,
            b=self.b,
            p=self.p,
            n=self.n,
            e=self.e
        )

    def pmf(self, m):
        return self.binominal.pmf(m)

    def f(self, m):
        """
        Compute the product of power of a, b, and the probability mass function (PMF) of binomial distribution.

        Parameters:
        m (int): The number of successes in the binomial experiment.

        Returns:
        float: The product of power of a, b, and the PMF of binomial distribution.
        """
        array = np.array((
            np.power(self.a, m),
            np.power(self.b, self.n-m),
            self.pmf(m)
        ), dtype=np.float64)

        prod = np.prod(array)

        precision_buffer.append(dict(
            n=self.n,
            m=m,
            value=prod,
            name='raw'
        ))

        return prod

    def g(self, m):
        """
        Compute the expectation of a function involving power of a, b, and the probability mass function (PMF) of binomial distribution.

        It keeps the high precision during the production of large numbers.

        Parameters:
        m (int): The number of successes in the binomial experiment.

        Returns:
        float: The expectation of the function. If `compute_in_log` is True, the expectation is calculated in logarithmic scale.
        """
        a = self.a
        b = self.b
        p = self.p
        q = 1-self.p
        n = self.n

        k = m*np.log(a)+(n-m)*np.log(b)

        num1 = [a] * m + [b] * (n-m)
        num2 = list(range(1, n+1))
        num3 = [p] * m + [q] * (n-m)
        den = list(range(1, m+1)) + list(range(1, n-m+1))

        res = 1
        for n1, n2, n3, d in zip(num1, num2, num3, den):
            if self.compute_in_log:
                res *= n2*n3/d
            else:
                res *= n1*n2*n3/d

        if self.compute_in_log:
            res *= k

        precision_buffer.append(dict(
            n=self.n,
            m=m,
            value=res,
            name='highp'
        ))

        return res


# %% ---- 2024-11-18 ------------------------
# Play ground
if __name__ == "__main__":
    compute_in_log = False

    while precision_buffer:
        precision_buffer.pop()

    results = []
    df_pmf = []
    df_dist = []

    for n in tqdm([2, 5, 10, 20, 30, 40, 50, 60], 'Computing'):
        kwargs = dict(
            a=0.1,
            b=9,
            p=0.5,
            n=n,
            compute_in_log=compute_in_log,
        )

        kwargs = dict(
            a=0.1,
            b=9,
            p=0.5,
            n=n,
            compute_in_log=compute_in_log
        )

        bino = Binomial(**kwargs)
        bino.compute_pmf(hue=n)
        result = bino.get_result(hue=n)
        results.append(result)

        if n < 300:
            df_pmf.append(bino.df_pmf)
            df_dist.append(bino.df_dist)

    df_pmf = pd.concat(df_pmf, axis=0)
    df_dist = pd.concat(df_dist, axis=0)

    # print(df_pmf)
    # print(df_dist)

    df = pd.DataFrame(results)
    display(df)

    sns.set_theme('notebook')
    palette = 'flare'
    fig, axes = plt.subplots(1, 2, figsize=(8, 4), dpi=200)
    ax = axes[0]
    sns.lineplot(
        df_pmf, x='nx', y='y', hue='hue', ax=ax, palette=palette)
    ax.set_title('pmf')
    ax.set_ylabel('Dense')
    ax.set_xlabel('')

    ax = axes[1]
    sns.lineplot(
        df_dist, x='nx', y='y', hue='hue', ax=ax, palette=palette, legend=False)

    if compute_in_log:
        ax.set_title('dist in log')
        ax.set_ylabel('Expectation')
        ax.set_xlabel('')
        ax.hlines(0, 0, 1, color='gray')
        ax.vlines(0.5, df_dist['y'].min(), df_dist['y'].max(), color='gray')
    else:
        ax.set_title('dist')
        ax.set_yscale('log')
        ax.set_ylabel('Expectation (log)')
        ax.set_xlabel('')
        ax.hlines(1, 0, 1, color='gray')
        ax.vlines(0.5, df_dist['y'].min(), df_dist['y'].max(), color='gray')

    fig.tight_layout()
    fig.savefig(f'img/res-log.png' if compute_in_log else f'img/res-raw.png')
    plt.show()

    # Compute the precision lost
    # supporting url: https://stackoverflow.com/questions/56480879/precision-error-in-scipy-stats-binom-method
    if not compute_in_log:

        df = pd.DataFrame(precision_buffer)
        df['compare'] = 0.0
        a = df[df['name'] == 'highp']
        b = df[df['name'] == 'raw']

        ap = a.pivot(index='n', columns='m', values='value')
        bp = b.pivot(index='n', columns='m', values='value')
        cp = ap / bp
        for c in cp.columns:
            cp[c] = np.log(np.abs(cp[c]))

        fig, ax = plt.subplots(1, 1, figsize=(4, 4))
        sns.heatmap(cp, cmap=palette, ax=ax)
        ax.set_title('Precision map (log scaled)')
        fig.tight_layout()
        fig.savefig(f'img/precision-map.png')
        plt.show()

# %% ---- 2024-11-18 ------------------------
# Pending


# %% ---- 2024-11-18 ------------------------
# Pending

# %%
