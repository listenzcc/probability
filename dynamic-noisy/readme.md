# 模拟随机on-off的随机函数

```python
# a and b is irrational numbers.
noise = np.sum([b*np.sin(np.sqrt(a)*0.7*t) for a, b in self.seeds], axis=0)
```

`noise` 生成随机 on-off 序列的原理如下：

1. **随机无理数生成**:
    - `self.seeds` 包含一组随机生成的无理数对 `(a, b)`，其中 `a` 和 `b` 是通过 `mk_random_irrational_number` 函数生成的无理数。

2. **正弦函数叠加**:
    - 对于每一对 `(a, b)`，计算 `b * np.sin(np.sqrt(a) * 0.7 * t)`，其中 `t` 是时间轴。
    - 这里使用了正弦函数 `sin`，其周期性特性有助于生成类周期性的 on-off 序列。
    - 而当`a, b`是无理数时，`sin(at)+sin(bt)`是非周期函数。

3. **叠加结果求和**:
    - 将所有正弦函数的结果进行叠加，得到 `noise`。
    - 叠加的结果会形成一个复杂的波形，其中包含多个频率成分。

4. **双曲正切函数**:
    - 在 `generate_step1` 函数中，叠加结果通过双曲正切函数 `tanh` 进行非线性变换，进一步增强 on-off 序列的随机性和复杂性。

通过上述步骤，`noise` 生成了一个复杂的随机 on-off 序列，该序列具有随机性和周期性特征。
