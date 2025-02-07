"""
File: poisson-distribution.py
Author: Chuncheng Zhang
Date: 2025-02-07
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Simulation for the poisson distribution.

    Poisson distribution equation:
    P(X = k) = (lambda^k * e^(-lambda)) / k!

    The script simulates the Poisson distribution by generating time gaps between events
    using an exponential distribution with parameter lambda. These gaps are then accumulated
    to simulate the occurrence of events over time.

    Run the script with the following command using the streamlit.
    $ streamlit run .\poisson-distribution.py

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2025-02-07 ------------------------
# Requirements and constants
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy.special import factorial
import streamlit as st

# %% ---- 2025-02-07 ------------------------
# Function and class


def generate_time_gaps(lamb, n=1e5):
    n = int(n)
    u = np.random.uniform(1e-3, 1, size=(n,))
    gaps = -1/lamb * np.log(u)
    return gaps


def generate_table(gaps):
    accum = np.cumsum(gaps)
    df = pd.DataFrame(accum, columns=['onset'])
    return df


def sampling(df, n=1e3):
    n = int(n)
    times = np.random.uniform(df['onset'].min(), df['onset'].max(), (n,))
    data = []
    for t in times:
        m = df.query(f'onset < {t+1} & onset > {t}')
        data.append(len(m))
    return data


# %% ---- 2025-02-07 ------------------------
# Streamlit app
st.title('Poisson Distribution Simulation')

st.markdown("""
### Purpose
Simulation for the Poisson distribution.

The script simulates the Poisson distribution by generating time gaps between events
using an exponential distribution with parameter lambda. These gaps are then accumulated
to simulate the occurrence of events over time.

**Poisson distribution equation:**
""")

st.latex(r"""
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
         """)


lamb = st.slider('Select lambda value', min_value=1, max_value=10, value=3)
df = generate_table(generate_time_gaps(lamb))

data = sampling(df)

# plot the histogram of data using seaborn plot
# draw the theoretical Poisson distribution with lambda = lamb
sns.set_theme('paper')
fig, ax = plt.subplots()
sns.histplot(data, kde=True, stat='density',
             label='Sampled Data', discrete=True, ax=ax)
x = np.arange(0, max(data) + 1)
poisson_pmf = (np.exp(-lamb) * lamb**x) / factorial(x)
ax.plot(x, poisson_pmf, 'o-', label='Theoretical Poisson PMF', color='red')
ax.set_xlabel('Counts')
ax.set_ylabel('Density')
ax.set_title('Histogram of Poisson Distributed Data with Theoretical PMF')
ax.legend()
st.pyplot(fig)
st.write(df)

# %% ---- 2025-02-07 ------------------------
# Pending


# %% ---- 2025-02-07 ------------------------
# Pending
