# 879. Profitable Schemes

## Solution

### 方法一

动态规划。不是很懂，见：[Profitable Schemes - LeetCode Articles](https://leetcode.com/articles/profitable-schemes/)。

### 方法二

深度优先搜索。设`DFS(g, p, i)`表示选到第`i`个crime的时候，剩余`g`人，需要实现的利益为`p`，
此时的选法数量。那么存在第`i`个crime选或不选的情况，如果`group[i] <= g`说明能选，
那么就是两种情况之和；反之则一定不选。

需要注意的是对于`p < 0`的情况均用`p == 0`代替，这样能减少状态的数目。此处用`lru_cache`
来保存`DFS`函数的返回值，似的深搜强行变成动态规划，但这样仍然不能过所有测例，超时。