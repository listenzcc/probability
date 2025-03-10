"""
File: random_activation_timeseries.py
Author: Chuncheng Zhang
Date: 2025-03-03
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Generates random activation timeseries.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2025-03-03 ------------------------
# Requirements and constants
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from rich import print


# %% ---- 2025-03-03 ------------------------
# Function and class
def mk_random_irrational_number(n1: int = 2, n2: int = 20):
    '''
    Generates random irrational number.

    :param n1: int, default 10, lower bound of the random number.
    :param n2: int, default 100, upper bound of the random number.

    :return r: float, random irrational number.
    '''
    r = np.random.uniform(n1, n2)
    return np.sqrt(r**2-1)


class Subject:
    seeds = None

    def __init__(self, k: int = 7):
        self.random_seeds(k)

    def random_seeds(self, k: int):
        seeds = [(mk_random_irrational_number(), mk_random_irrational_number())
                 for _ in range(k)]
        self.seeds = seeds
        return seeds

    def generate_step1(self, t, psi: float = 7.0):
        accumulate = np.sum([b*np.sin(np.sqrt(a)*0.7*t)
                            for a, b in self.seeds], axis=0)
        return 1+np.tanh(psi*accumulate)

    def generate_step2(self, t):
        s1 = self.generate_step1(t)
        for dt in range(10, 100, 10):
            s1 = s1 + self.generate_step1(t+dt)
        return s1/10

    def generate_step3(self, t):
        s2 = self.generate_step2(t)
        for dt in range(100, 400, 100):
            s2 = s2 + self.generate_step2(t+dt)
        return s2/4


def find_edges(array):
    array = np.round(array, 4)
    edges = []
    want = 'up'
    for i in range(1, len(array)-1):
        if want == 'up' and array[i] == 2 and array[i-1] < 2:
            edges.append({'edge': 'up', 'i': i})
            want = 'down'
            continue

        if want == 'down' and array[i] == 2 and array[i+1] < 2:
            edges.append({'edge': 'down', 'i': i})
            want = 'up'
            continue

    while not edges[0].get('edge') == 'up':
        edges.pop(0)

    detail = []
    for i in range(0, len(edges)-1, 2):
        a = edges[i]
        b = edges[i+1]
        try:
            assert a['edge'] == 'up' and b['edge'] == 'down'
        except AssertionError as err:
            print(a, b)
            raise err
        detail.append({'start': a['i'], 'stop': b['i'],
                       'length': b['i'] - a['i']})

    return edges, detail


def compute_auto_correlate(array):
    '''
    Choose the middle n//5 length window of the array.
    Compute the auto-correlation among the array by the sliding window.
    '''
    n = len(array)
    window_size = n // 5
    middle_start = (n - window_size) // 2
    middle_end = middle_start + window_size
    middle_window = array[middle_start:middle_end]

    auto_corr = np.correlate(middle_window, middle_window, mode='full')
    auto_corr /= window_size * 2
    return auto_corr


# %% ---- 2025-03-03 ------------------------
# Play ground
num_subjects = 10
t_axis = np.arange(0, 60, 0.01)

subjects = [Subject() for _ in range(num_subjects)]
gs = [subject.generate_step1(t_axis) for subject in subjects]


plt.style.use('seaborn-v0_8')
plt.style.use('seaborn-v0_8-paper')

fig, axes = plt.subplots(2, 2, figsize=(8, 8))

ax = axes[0][0]
ax.plot(t_axis, gs[0])
ax.set_title('Example sample')

ax = axes[0][1]
for g in gs:
    edges, detail = find_edges(g)
    a, b = np.histogram([e['length'] for e in detail])
    ax.plot(b[:-1], a)
ax.set_title('Length histogram')

ax = axes[1][0]
for g in gs:
    d = compute_auto_correlate(g)
    ax.plot(d)
ax.set_title('Auto correlation')

ax = axes[1][1]
m = np.corrcoef(gs)
sns.heatmap(m, fmt='.2f', ax=ax)
ax.set_title('Coefficients of samples')

plt.tight_layout()
plt.show()


# %% ---- 2025-03-03 ------------------------
# Pending


# %% ---- 2025-03-03 ------------------------
# Pending


# %%
