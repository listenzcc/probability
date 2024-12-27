# The probability distribution of Frequency

---

[toc]

## Frequency analysis

Using the notions:

- $t$, the total number which is unknown.
- $m$, the obtained maximum number.
- $k$, the count of the observations.

where we naturally have $t \ge m \ge k$.
Take $T$ and $M$ are random variables, what we control is how many observations are.
As a result, the probability of maximum number of observations is determined as

$$\tag{1} Pr(M=m) = \frac{C_{m-1}^{k-1}}{C_t^k}$$

Firstly, we have

$$\sum_{m=k}^{t} Pr(m) = 1$$

see [Lemma-1](#lemma-1-unit-property) for details.
It should be noticed that the equation is true for every $t \ge k$.

Secondly, in frequency's opinion at the $m$ value, the total number of unknown is estimated as

$$\tag{2} \hat{t} = m \frac{k+1}{k} - 1$$

see the latter for details.

## The relationship between k, m and t

The relationship between $k, m, t$ is

$$Pr(m) = \frac{1}{C_t^k} C_{m-1}^{k-1}$$

The $E(m)$ follows

$$C_t^kE(m) = \sum_{m=k}^{t}m \frac{(m-1)!}{(m-k)!(k-1)!}$$

And

$$\frac{(k-1)!}{k!}C_t^kE(m) = \sum_{m=k}^{t} \frac{m!}{(m-k)!k!}$$

And

$$\frac{1}{k}C_t^kE(m) = \sum_{m=k}^{t} C_m^k$$

Using the [Hockey-stick Identity](https://en.wikipedia.org/wiki/Hockey-stick_identity), one has

$$\sum_{m=k}^{t}C_m^k = C_{t+1}^{k+1}$$

As a result

$$E(m) = \frac{k C_{t+1}^{k+1}}{C_t^k} =\frac{k}{k+1}(t+1)$$

Finally, one has

$$\hat{t} = m \frac{k+1}{k} - 1$$

## Lemma-1: Unit property

Lemma:

$$\sum_{m=k}^{t} Pr(m) = 1$$

Proof:

Firstly, one has

$$C_{t}^k = \frac{t!}{k!(t-k)!}$$

When it comes to $t+1$, one has

$$C_{t+1}^k = C_{t}^k \frac{t+1}{t+1-k}$$

The sum is

$$C_t^k + C_{t}^{k-1} = \frac{t!}{k!(t-k)!} + \frac{t!}{(k-1)!(t-k+1)!}$$

It reduces into

$$C_t^k + C_{t}^{k-1} = \frac{t! \cdot (t-k+1+k)}{k!(t-k+1)!}$$

Finally, it produces

$$\tag{L1-1} C_t^{k} + C_t^{k-1} = C_{t+1}^k$$

Secondly, the sum is

$$\sum_{m=k}^{t}\frac{C_{m-1}^{k-1}}{C_t^k}$$

where $t \ge m \ge k$.
To make the sum equals to one, one can pull out the denominator. And it should satisfy

$$C_t^k = \sum_{m=k}^{t} C_{m-1}^{k-1}$$

To prove that, one can use the [mathematical induction](https://en.wikipedia.org/wiki/Mathematical_induction) method.
Starts with assuming it satisfies

$$C_t^k = \sum_{m=k}^{t} C_{m-1}^{k-1}$$

Using the $\text{eq. L1-1}$, it produces

$$C_{t+1}^k = \sum_{m=k}^{t} C_{m-1}^{k-1} + C_t^{k-1}$$

Easy to see that the latter equals to $m=t+1$, so one has

$$C_{t+1}^k = \sum_{m=k}^{t+1} C_{m-1}^{k-1}$$

In the first factor $t=k$, it follows

$$C_k^k = \sum_{m=k}^{k}C_{k-1}^{k-1}$$

As a result, the induction is satisfied, which proves

$$C_t^k = \sum_{m=k}^{k} C_{m-1}^{k-1}$$

$\blacksquare$
