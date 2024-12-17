# The probability distribution of Bayesian

本文对“German tanks problem”的贝叶斯估计问题进行定量求解，证明了前文列出的概率密度函数的归一性，并给出了其分布的均值。二者都是用超几何分布，经简单推导即可得到。
还遗漏了它的二阶矩的相关计算，目前还没想到简单的算法。

---

[toc]

## Probabilities dense

Using the notions:

- $t$, the total number which is unknown.
- $m$, the obtained maximum number.
- $k$, the count of the observations.

where we naturally have $t \ge m \ge k$.

Take $T$ is random variable, the credibility of $t$ is

$$\tag{1} p(T=t \vert m, k) = \frac{C_{m-1}^{k-1}}{C_t^k} \cdot \frac{k-1}{k}$$

It follows the unit property of the probability dense function (see [Unit property](#unit-property)).

And the expectation is also quite simple (see [Expectation](#expectation))
$$E(t) = (m-1)(k-1)(k-2)^{-1}$$

## Unit property

Lemma 1:

$$\sum_{t=m}^{\infty}p(t \vert m, k) = 1$$

Proof:

It equals to the equation

$$ \tag{L1.1} \sum_{t=m}^{\infty} \frac{1}{C_t^k} = \frac{k}{(k-1) \cdot C_{m-1}^{k-1}}$$

And each element is

$$\frac{1}{C_t^k} = \frac{k! \cdot (t-k)!}{t!}$$

Using the Gauss's Hypergeometric Theorem

$$\sum_{x=0}^\infty \frac{(a)_x(b)_x}{x!(c)_x} = \frac{\Gamma(c)\Gamma(c-a-b)}{\Gamma(c-a)\Gamma(c-b)}$$

In my case, the $L1.1$ changes into

$$ \sum_{x=0}^{\infty} \frac{k! \cdot (m-k)! \cdot (m-k+1)_x}{m! \cdot (m+1)_x} $$

Using the property of $(1)_x = x!$, it equals to $c=m+1, a=1, b=m-k+1$

$$\frac{k! \cdot (m-k)!}{m!} \cdot \frac{\Gamma(m+1) \Gamma(k-1)}{\Gamma(m) \Gamma(k)}$$

It equals to

$$\frac{k! \cdot (m-k)!}{m!} \cdot \frac{m}{k-1}$$

It turns into

$$\frac{k}{k-1} \frac{(k-1)! \cdot (m-k)!}{(m-1)!} = \frac{k}{(k-1) \cdot C_{m-1}^{k-1}}$$

$\blacksquare$

## Expectation

Lemma 2:

$$E(t) = (m-1)(k-1)(k-2)^{-1}$$

Proof:

The expectation is

$$\sum_{t=m}^{\infty}t \cdot p(t \vert m, k)$$

More specifically

$$ E(t) = \frac{(k-1) \cdot C_{m-1}^{k-1}}{k} \cdot\sum_{t=m}^{\infty} \frac{t}{C_t^k}$$

Inside the summation, each element is

$$\frac{t}{C_t^k} = \frac{k! \cdot (t-k)!}{(t-1)!}$$

It changes into

$$ \sum_{x=0}^{\infty} \frac{k! \cdot (m-k)! \cdot (m-k+1)_x}{(m-1)! \cdot (m)_x} $$

Using the Gauss's Hypergeometric Theorem

$$\sum_{x=0}^\infty \frac{(a)_x(b)_x}{x!(c)_x} = \frac{\Gamma(c)\Gamma(c-a-b)}{\Gamma(c-a)\Gamma(c-b)}$$

Using the property of $(1)_x = x!$, it equals to $c=m, a=1, b=m-k+1$

$$\frac{k! \cdot (m-k)!}{(m-1)!} \cdot \frac{\Gamma(m) \Gamma(k-2)}{\Gamma(m-1) \Gamma(k-1)}$$

As a result

$$E(t) = \frac{(k-1) \cdot C_{m-1}^{k-1}}{k} \cdot \frac{k! \cdot (m-k)!}{(m-1)!} \cdot \frac{m-1}{k-2}$$

Because of

$$C_{m-1}^{k-1} = \frac{(m-1)!}{(k-1)! \cdot (m-k)!}$$

We finally have

$$E(t) = (m-1)(k-1)(k-2)^{-1}$$

$\blacksquare$
