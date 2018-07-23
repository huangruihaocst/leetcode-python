# 167. Two Sum II - Input array is sorted

## Solution

### 方法一

不管递增的条件，直接用`dict`，记录当前访问过的值和下标，再次访问的时候的复杂度为`O(1)`。
访问到`numbers[i]`的时候检查一下`target - numbers[i]`是否被访问过即可。

### 方法二

应用递增的条件。

设置两个下标位置，开始分别在头和尾。如果这两个位置的数之和大于`target`，则大数挪到上一个；
如果小于`target`，则小数挪到下一个。直到找到这个数。