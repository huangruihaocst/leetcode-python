# 232. Implement Queue using Stacks

## Solution

### 方法一

单栈。入队复杂度`O(1)`，出队和查看队头复杂度`O(n)`。

### 方法二

双栈。懒惰处理，更加平衡。入队和出队复杂度均为`O(1)`~`O(n)`。