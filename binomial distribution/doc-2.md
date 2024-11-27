# 二项分布二三事（二）

---

[toc]

## 二项分布的矩母函数

二项分布的概率密度函数满足

$$p(x) = C_n^x \cdot p^x \cdot q^{n-x}$$

其中，$x \in [0, 1 \dots n]$，且$p+q=1$。
其矩母函数为$E(e^{xt})$

$$M(t) = \sum_{x=0}^{n} e^{xt} \cdot C_n^x \cdot p^x \cdot q^{n-x}$$

整理得

$$M(t) = (q + p e^t)^n$$

则，其一阶矩$E(X)$为

$$M'|_{t=0}=n(q+p e^t)^{n-1} \cdot p e^t |_{t=0} = np$$

其二阶矩$E(X^2)$亦可通过二阶导数求得

$$M'' = npe^t(n-1)(q+p e^t)^{n-2} \cdot p e^t + n(q+p e^t)^{n-1} \cdot p e^t $$

$$M''|_{t=0}=n(n-1)pp + np = n^2p^2+np-npp = n^2p^2+npq$$

易得，其方差为

$$\text{Var} = E(X^2) - E^2(X) = npq$$

## 附录：矩母函数与随机变量的矩

考虑随机变量$X$，其分布已知且解析

$$X \sim P(X)$$

构造如下函数，称为矩母函数

$$M(t) = E(e^{xt}) = \int_x e^{xt} p(x) dx$$

其$n$阶微分为

$$M_t^{(n)} = \frac{\partial^n M}{\partial t^n} = \int_x x^n \cdot e^{xt} \cdot p(x) dx$$

不难发现

$$M_t^{(n)} |_{t=0} = E(x^n)$$

$\blacksquare$
