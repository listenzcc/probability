# The probability distribution of Bayesian (2)

本文还是对“German tanks problem”的贝叶斯估计问题进行定量求解，完成了它的二阶矩的相关计算，目前的方法还算简单。

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

Computing the second order moment, we have

$$\tag{2} Var = \frac{(k-1)(m-1)(m-k+1)}{(k-3)(k-2)^2}$$

## The second order moment

The second order moment is $E(T^2)$

$$\sum_{t=m}^{\infty}t^2 \cdot p(t \vert m, k)$$

More specifically

$$ E(T^2) = \frac{(k-1) \cdot C_{m-1}^{k-1}}{k} \cdot\sum_{t=m}^{\infty} \frac{t^2}{C_t^k}$$

Inside the summation, each element is

$$\frac{t^2}{C_t^k} = \frac{t \cdot k! \cdot (t-k)!}{(t-1)!}$$

It changes into

$$ \sum_{x=0}^{\infty} \frac{(m+x) \cdot k! \cdot (m-k)! \cdot (m-k+1)_x}{(m-1)! \cdot (m)_x} $$

Simplify it

$$\frac{k! \cdot (m-k)!}{(m-1)!} \cdot \sum_{x=0}^{\infty}\frac{(m-1+x+1) \cdot (m-k+1)_x}{(m)_x}$$

Split the $E(T^2)$ into two parts,
The first part is

$$E_1(T^2) = (m-1)E(T)$$

Next, we compute the seconds part from

$$\frac{k! \cdot (m-k)!}{(m-1)!} \cdot \sum_{x=0}^{\infty}\frac{(x+1) \cdot (m-k+1)_x}{(m)_x}$$

The summation element is

$$\frac{(x+1) \cdot (1)_{x} \cdot (m-k+1)_x}{x! \cdot (m)_x}$$

It changes into

$$\frac{(2)_{x} \cdot (m-k+1)_x}{x! \cdot (m)_x}$$

Using the Gauss's Hypergeometric Theorem

$$\sum_{x=0}^\infty \frac{(a)_x(b)_x}{x!(c)_x} = \frac{\Gamma(c)\Gamma(c-a-b)}{\Gamma(c-a)\Gamma(c-b)}$$

Using the property of $(1)_x = x!$, it equals to $c=m, a=2, b=m-k+1$

$$\frac{k! \cdot (m-k)!}{(m-1)!} \cdot \frac{\Gamma(m) \Gamma(k-3)}{\Gamma(m-2) \Gamma(k-1)}$$

It equals to

$$\frac{k! \cdot (m-k)!}{(m-1)!} \cdot \frac{(m-1)(m-2)}{(k-2)(k-3)}$$

As a result, the second part is

$$E_2(T^2) = \frac{(k-1) \cdot C_{m-1}^{k-1}}{k} \cdot \frac{k! \cdot (m-k)!}{(m-1)!} \cdot \frac{(m-1)(m-2)}{(k-2)(k-3)}$$

Using

$$E(T) = \frac{(k-1) \cdot C_{m-1}^{k-1}}{k} \cdot \frac{k! \cdot (m-k)!}{(m-1)!} \cdot \frac{m-1}{k-2}$$

We have

$$E_2(T^2) = E(T) \cdot \frac{m-2}{k-3}$$

Finally

$$E(T^2) = E(T) \cdot ((m-1) + \frac{m-2}{k-3}) $$

$\blacksquare$

## Variation

We are interested in

$$Var = E(T^2) - E^2(T)$$

Since we have

$$E(t) = (m-1)(k-1)(k-2)^{-1}$$

So, we have

$$Var = E(T) \cdot ((m-1) + \frac{m-2}{k-3} - (m-1)(k-1)(k-2)^{-1})$$

The latter part equals to

$$\frac{(m-1)(k-2)(k-3) + (m-2)(k-2) - (m-1)(k-1)(k-3)}{(k-2)(k-3)}$$

then

$$\frac{(m-2)(k-2) - (m-1)(k-3)}{(k-2)(k-3)} = \frac{1+m-k}{(k-2)(k-3)}$$

Finally,

$$Var = \frac{(k-1)(m-1)(m-k+1)}{(k-3)(k-2)^2}$$

$\blacksquare$
