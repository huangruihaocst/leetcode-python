# 561. Array Partition I

## Solution

贪心算法。从小到大排序，然后从后往前数，为了使和最大，应该用最大的数和第二大的数配对，以此类推。
注意，可以用`sum`对`iterable`进行求和。可以用slice中的第三个参数获得奇数项，如`nums[::2]`。
