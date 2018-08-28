# 747. Largest Number At Least Twice of Others

## Solution

### 方法一

暴力算法。求出最大值后再遍历一遍。注意不能用`m / i`因为`i`有可能是`0`。

### 方法二

只遍历一遍数组求出最大的两个数，然后对比。

但是我把二者的index都记下来了，实际只需要记录最大值的index。