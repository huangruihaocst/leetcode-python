# 594. Longest Harmonious Subsequence

## Solution

首先统计每个数的出现次数，然后找到每个数的加一是否也存在，然后找到所有`val`和`val + 1`的个数和中的最大值。