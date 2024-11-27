# Counting problem

---

[toc]

## Problem Description

There are $m$ (unknown) items, numbered as $0, 1 \dots m$.
Randomly choice $k$ items without replacement.
And the maximum number of chosen items is $n$.
Find the solution of

$$\tag{1} \hat{m} = \arg\max_m \varphi(k, n, m)$$

where $\varphi(k, n, m)$ refers the probability of the pair of $(k, n, m)$.
Naturally, $m \ge n \ge k$.

## Analysis: Maximum likelihood estimation

Analysis the $\varphi$, it equals the combination of two things

1. In prior, select $k$ items from $m$ without replacement.
2. The maximum number of the chosen items is $n$.

As a result, having the conditional probability

$$p(n \vert m, k) = \frac{C_{n-1}^{k-1}}{C_m^k}$$

where the probability is computed as the division between choosing $k-1$ items from $n-1$ numbers and choosing $k$ items from $m$ total (since $n$ is locked).
In theory, the probability follows

$$\sum_{n=k}^{m} p(n \vert m, k) = 1$$

which satisfiers all the possible $k$.
And the joint probability between $m$ and $n$ is drawn below

![joint prob](./binomial-distribution-img/joint%20prob%20of%20m%20n.png "joint prob")

It derives

$$p(n \vert k) = \sum_{m=n}^{\infty} p(n \vert m, k) p(m | k)$$

### Lemma 1

For the large enough $M>m$ we have

$$p(m \vert k) = \frac{1}{M-k} $$

which shows the $p(m\vert k)$ is irrelevant with $m$, what ever the $M$ is.

$\blacksquare$

### Lemma 2

In this section, we use the notions for the better working memory

- $t$, the total number which is unknown.
- $m$, the obtained maximum number.
- $k$, the count of the observations.

Using Bayesian probability function, we have

$$p(t \vert m, k) = \frac{p(m \vert t, k)p(t \vert k)}{p(m \vert k)}$$

Thus, we have

$$p(t \vert m, k) = \frac{p(m \vert t, k) p(t \vert k)}{\sum_{\tau=m}^{\infty} p(m \vert \tau, k) p(\tau \vert k)}$$

where $\tau$ refers the variable of $t$, and $p(\tau \vert k) = p(t \vert k)$ (see [Lemma 1](#lemma-1)). It consists

$$\tag{2} p(t \vert m, k) = \frac{p(m \vert t, k)}{\sum_{\tau=m}^{\infty} p(m \vert \tau, k)}$$

In general, we have

$$p(m \vert t, k) = \frac{C_{m-1}^{k-1}}{C_t^k}$$

$$\frac{C_{m-1}^{k-1}}{C_m^k} = \frac{k}{m}$$
$$\frac{C_{m-1}^{k-1}}{C_{m+1}^k} = \frac{k(m+1-k)}{m(m+1)}$$

It produces the series

$$\begin{cases}
a_0 &=\frac{k}{m}\\
a_x &= a_{x-1} \cdot \frac{m+x-k}{m+x}, x \in [1, 2 \dots]
\end{cases}$$

It seems that (how to prove?)

$$\sum_{i=0}^{\infty} a_i = \frac{k}{k-1}$$

---

$$p(n \vert m, k) = \frac{p(n, m \vert k)}{p(m \vert k)}$$

The denominator is

$$\sum_{\mu} \frac{p(n, \mu \vert k)}{p(\mu \vert k)}$$

$\blacksquare$

## Tail
