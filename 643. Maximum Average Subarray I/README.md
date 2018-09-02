# 643. Maximum Average Subarray I

## Solution

### 方法一

维护一个队列，当前选中的子数组。

### 方法二

利用前缀和，再往回减。

### 方法三

遍历一次，每次加上新数，减去`k`项前的数。