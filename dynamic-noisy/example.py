import matplotlib.pyplot as plt
import math
import numpy as np

# 迭代方程


def A(x, y):
    k = math.log1p(x)/math.log(2)*0.5*(1+math.tanh(5*(y+1.5)))
    return k

# 随机函数


def a(t):
    c = 1+math.tanh(7*(math.sin((math.sqrt(3))*0.7*t)+math.sin((math.sqrt(5))*0.7*t)+0.332*math.sin(
        (math.sqrt(16))*0.7*t)+math.sin((math.sqrt(14))*0.7*t)+1.02*math.sin((math.sqrt(2.5803)*0.7*t))))
    return c


def b(t):
    d = (a(t)+a(t+10)+a(t+20)+a(t+30)+a(t+40) +
         a(t+50)+a(t+60)+a(t+70)+a(t+80)+a(t+90))/10
    return d


def g(t):
    e = (b(t)+b(t+100)+b(t+200)+b(t+300))/4
    return e


# 时间步长
step = round(0.05, 5)

# F在t为0前取值的初始化
dict = {}  # 迭代数据暂存
hhh = -1
while hhh <= 0:
    dict[hhh] = g(hhh)
    hhh = round(hhh+step, 5)

# 记录突变时间
timelist = []
count = 0
realcount = 0
# 用于绘图记录数据
datadict = {}  # 响度记录
gdata = {}  # 发言意愿记录
# 迭代循环
t = 0
while t <= 3600:
    fl = (dict[round(t-0.05, 5)]+dict[round(t-0.1, 5)]+dict[round(t-0.15, 5)] +
          dict[round(t-0.2, 5)]+dict[round(t-0.25, 5)]+dict[round(t-0.3, 5)])/6
    fv = (((dict[round(t-0.05, 5)]+dict[round(t-0.1, 5)]+dict[round(t-0.15, 5)]+dict[round(t-0.2, 5)]+dict[round(t-0.25, 5)])/5) -
          ((dict[round(t-0.55, 5)] + dict[round(t-0.6, 5)]+dict[round(t-0.65, 5)]+dict[round(t-0.7, 5)]+dict[round(t-0.75, 5)])/5))*2
    dict[t] = g(t)*A(fl, fv)+0.001*g(t)
    datadict[t] = dict[t]
    gdata[t] = g(t)
    del dict[round(t-0.8, 5)]
    # 以上递推模拟
    last = count
    if (dict[round(t-0.05, 5)]+dict[round(t-0.1, 5)]+dict[round(t-0.15, 5)]+dict[round(t-0.2, 5)]+dict[round(t-0.25, 5)])/5 >= 0.1:
        count = 0
    else:
        count = 1

    if last-count <= -1:
        realcount = realcount+1
        timelist.append(t)
    # 以上突变计录

    print(t)
    t = round(t+step, 5)


# 1.75，50h，0     1.6 43    1.5 187(100h410个)     1.4 约475     1.3 约1250     1.2 约2550        1.1 约5075    1 约9200
# 以下突变绘制
# 绘图循环
n = 1
databar = {}
kkk = -5
tmd = 0.5
while kkk <= 5:
    databar[kkk] = 0
    kkk = round(kkk+0.05, 5)  # 平均值初始化
while n <= realcount:
    ctime = timelist[(n-1)]
    x_values = list(np.arange(ctime-5, ctime+5, 0.05))
    y_values = [datadict[round(x, 5)] for x in x_values]
    # g_values= [gdata[round(x,5)] for x in x_values]

    x_values = list(np.arange(-5, 5, 0.05))
    if datadict[round(ctime, 5)] >= 0.06:
        tmd = 0.7
    else:
        tmd = 0.01
    plt.plot(x_values, y_values, alpha=tmd)

    #    plt.plot(x_values,g_values,"c-")
    n = round(n+1, 2)
T = -5
while T <= 5:  # 求均值循环
    for m in timelist:
        databar[T] = databar[T]+(datadict[round(m+T, 5)])/realcount
    T = round(T+0.05, 5)
data_values = [databar[round(x, 5)] for x in x_values]
plt.plot(x_values, data_values, "c-")
plt.axis([-5, 5, 0, 2])
plt.show()
