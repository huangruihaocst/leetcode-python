# 371. Sum of Two Integers

## Solution

最快的方法过于奇葩。不过按位运算的方法很重要，要学会。可以参考[[编程题]不用加减乘除做加法](https://www.nowcoder.com/questionTerminal/59ac416b4b944300b617d4f7f111b215)和[不用＋、－、×、÷对两个数求和](https://blog.csdn.net/zhang_shuai12/article/details/46462175)。

### 原理

设两个数分别是$K$和$L$，它们之中大数为$n$位，则分别可以写成$K=\sum_{i=0}^{n}k_i\cdot2^i$和$L=\sum_{i=0}^{n}l_i\cdot2^i$。

则
$$
\begin{aligned}
K+L &= \sum_{i=0}^{n}k_i\cdot2^i+\sum_{i=0}^{n}l_i\cdot2^i \\
&= \sum_{i=0}^{n}(k_i+l_i)\cdot2^i \\
\end{aligned}
$$
而$k_i+l_i$分三种情况，分别是$0$，$1$和$2$（十进制）。于是
$$
\begin{aligned}
K+L &= \sum_{\substack{i=0 \\ k_i+l_i=1}}^n 2^i+2\cdot\sum_{\substack{i=0 \\ k_i+l_i=2}}^n2^i \\
&= K \oplus L + 2 \cdot (K \wedge L) \\
\end{aligned}
$$
也即`K ^ L + (K & L) << 1`。令`K = K ^ L, L = (K & L) << 1`，如此循环直至`L`为`0`即可。

至于为什么一定会停下来，因为`(K & L) << 1`的`1`的个数不比`L`多，而如果有正好相同`1`的数量，说明`K == L`，而此时`K ^ L == 0`了，也能停下来。