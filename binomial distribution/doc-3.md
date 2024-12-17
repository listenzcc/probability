# Counting problem

这就是著名的“德国坦克”统计问题。
该问题可以简单地描述成这样一句话：

> 我面前是一个黑箱，箱子里面的元素按顺序编号。我从中无放回地采样`10`次，得到的最大标号为`100`，那么请问这个箱子里的元素数量是多少？

这个问题十分有趣，因为贝叶斯学派和频率学派分别给出了不同的估计结果。
而且两派各有道理。

本文尝试从贝叶斯学派的观点来解释这个问题，之后将尝试记录频率学派的分析结果。

写在前面：

1. 因为这个问题涉及的知识比较繁杂，我目前还没有完全理清楚，因此暂时写出来放在这里。
2. 现阶段想到哪里写到哪里，没有到校对和整理的阶段，因此不同章节的符号使用可能略有不同。
3. 我习惯用vim进行笔记，这个东西（尤其是在输入公式时）对中文输入法并不友好，因此草稿以英文为主。
4. 严格来说这也并不是二项分布问题，但由于组合数的存在，这个问题总是容易与二项分布联系起来。

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

## Bayesian Analysis

Analysis the $\varphi$, it equals the combination of two things

1. In prior, select $k$ items from $m$ without replacement.
2. The maximum number of the chosen items is $n$.

The conditional probability is

$$p(n \vert m, k) = \frac{C_{n-1}^{k-1}}{C_m^k}$$

where the probability is computed as the division between choosing $k-1$ items from $n-1$ numbers and choosing $k$ items from $m$ total (since $n$ is locked).
In theory, the probability follows

$$\sum_{n=k}^{m} p(n \vert m, k) = 1$$

which satisfiers all the possible $k$.
And the joint probability between $m$ and $n$ is drawn below
It also derives

$$p(n \vert k) = \sum_{m=n}^{\infty} p(n \vert m, k) p(m | k)$$

![Conditional prob](./binomial-distribution-img/Conditional%20prob%20of%20n%20at%20m%20and%20k=5.png "Conditional prob")

## Probability formula

To find the closed-formula[^closed-formula] for the probability, the key take-away is the $(2)$ of the [Lemma 2](#lemma-2).
[^closed-formula]: <https://en.wikipedia.org/wiki/Closed-form_expression>

It gives the probability mass function[^probability-mass-function] for the unknown value under observations.
[^probability-mass-function]: <https://en.wikipedia.org/wiki/Probability_mass_function>

### Lemma 1

For the large enough $M>m$ we have

$$p(m \vert k) = \frac{1}{M-k} $$

It shows the $p(m\vert k)$ is irrelevant with $m$, what ever the $M$ is.

$\blacksquare$

### Lemma 2

In this section, we use the notions for the better working memory

- $t$, the total number which is unknown.
- $m$, the obtained maximum number.
- $k$, the count of the observations.

Take $T$ is random variable, the credibility of $t$ is

$$\tag{2} p(T=t \vert m, k) = \frac{C_{m-1}^{k-1}}{C_t^k} \cdot \frac{k-1}{k}$$

Using Bayesian probability function, we have

$$p(t \vert m, k) = \frac{p(m \vert t, k)p(t \vert k)}{p(m \vert k)}$$

Thus, we have

$$p(t \vert m, k) = \frac{p(m \vert t, k) p(t \vert k)}{\sum_{\tau=m}^{\infty} p(m \vert \tau, k) p(\tau \vert k)}$$

where $\tau$ refers the variable of $t$, and $p(\tau \vert k) = p(t \vert k)$ (see [Lemma 1](#lemma-1)). It consists

$$p(t \vert m, k) = \frac{p(m \vert t, k)}{\sum_{\tau=m}^{\infty} p(m \vert \tau, k)}$$

In general, we have

$$p(m \vert t, k) = \frac{C_{m-1}^{k-1}}{C_t^k}$$

and the $t$ can be rewritten as $\tau$

$$p(m \vert \tau, k) = \frac{C_{m-1}^{k-1}}{C_\tau^k}$$

We notice that

$$\frac{C_{m-1}^{k-1}}{C_m^k} = \frac{k}{m}$$

and

$$\frac{C_{m-1}^{k-1}}{C_{m+1}^k} = \frac{k(m+1-k)}{m(m+1)}$$

It produces the series

$$\begin{cases}
a_0 &=\frac{k}{m}\\
a_x &= a_{x-1} \cdot \frac{m+x-k}{m+x}, x \in [1, 2 \dots]
\end{cases}$$

The summation is (see [Lemma 3](#lemma-3))

$$\sum_{i=0}^{\infty} a_i = \frac{k}{k-1}$$

As a result, the credibility of $t$ is

$$p(t\vert m, k) = \frac{p(m \vert t, k)}{\sum_{i=0}^{\infty} a_i}$$

It equals to

$$p(t \vert m, k) = \frac{C_{m-1}^{k-1}}{C_t^k} \cdot \frac{k-1}{k}$$

or, in the alignment format

$$p(t \vert m, k) = (k-1)C_{m-1}^{k-1} \cdot \begin{pmatrix}k {C_m^k}\end{pmatrix}^{-1}$$

$\blacksquare$

### Lemma 3

Using Gauss's Hypergeometric Theorem[^wiki-ght] (Gauss's summation theorem), we have

[^wiki-ght]: https://en.wikipedia.org/wiki/Hypergeometric_function

$$\sum_{x=0}^\infty \frac{(a)_x(b)_x}{x!(c)_x} = \frac{\Gamma(c)\Gamma(c-a-b)}{\Gamma(c-a)\Gamma(c-b)}$$

where $(a)_x = a(a+1)\dots (a+x-1)$. For a special case, we have

$$ (1)_x = x! $$

In my case

$$a_x = \frac{k}{m} \cdot \frac{(m+x-k)_x}{(m+1)_x}$$

It is transformed to

$$a_x = \frac{k}{m} \cdot \frac{(1)_x \cdot (m+1-k)_x}{x! \cdot (m+1)_x}$$

As the result, the summation is

$$\frac{k}{m} \cdot \frac{\Gamma(m+1)\Gamma(k-1)}{\Gamma(m)\Gamma(k)} = \frac{k}{k-1}$$

where

$$\begin{cases}
a&=1\\
b&=m+1-k\\
c&=m+1
\end{cases} \Rightarrow
\begin{cases}
c-a &= m\\
c-b &= k\\
c-a-b &= k-1
\end{cases}$$

and

$$\begin{cases}
n \Gamma(n) &= n!\\
\Gamma(n) &= (n-1)!, n \in \bold{N}^+
\end{cases}$$

$\blacksquare$
