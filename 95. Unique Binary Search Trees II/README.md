# 95. Unique Binary Search Trees II

## Solution

分治。

对于一个列表`range(start, end + 1)`，定义函数`generate`求出这个列表的所有BST。
求其结果时，遍历所有可能的根节点，然后左右子树分别调用`generate`函数。
接起来。