# 256. Paint House

## Solution

动态规划。

设`dp[i][j]`表示当选择到第`i`栋房子并且染为`j`色时最小的消费，
则当第`i + 1`栋房子时，最小的消费取决于上一栋房子的颜色，从不是`j`的颜色中选择两个，
求最小值并加上`costs[i + 1][color_now]`，也即

```
dp[i + 1][j] = min(dp[i][k]) + costs[i + 1][j], for all k != j
```