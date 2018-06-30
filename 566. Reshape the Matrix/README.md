# 566. Reshape the Matrix

## Solution

列表表达式的嵌套：按照普通循环的顺序即可，比如`[x for row in matrix for x in row]`即可遍历矩阵的所有元素。
