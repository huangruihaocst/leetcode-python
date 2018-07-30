# 878. Nth Magical Number

## Solution

### 方法一

二分查找。易知，对于正整数$A$和$B$，在$[1,x]$范围内，要么能被$A$整除，要么能被$B$整除的数的个数为
$$
\lfloor\frac{x}{A}\rfloor + \lfloor\frac{x}{B}\rfloor - \lfloor\frac{x}{[A,B]}\rfloor
$$
其中$[A,B]$表示$A$和$B$的最小公倍数。由于上式对于$x$是单增的，因此可以用二分查找，找到一个$x$，使得$x$是$A$或者$B$的倍数，同时上式的值为$N$。开始时左边为$1$，右边为$N\times min(A,B)$。

### 方法二

找规律。易知，从$1$到$[A,B]$，有
$$
L=\frac{[A,B]}{A}+\frac{[A,B]}{B}-1
$$
个数要么是$A$的要么是$B$的倍数，而且下$[A,B]$个数也是如此。因此，可以先数数$N$中包含多少个$L$，$N=L\times q+r$，就先加上$q \times [A,B]$，而对于剩余的$r$个数，用暴力算法，每次加$A$或者$B$，小的是下一个数。