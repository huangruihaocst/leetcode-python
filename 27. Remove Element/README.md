# 27. Remove Element

## Solution

从前往后遍历，如果发现`val`就把最后一个数`pop`掉换给这个数，注意可能得`pop`多次或者后面没有数不是`val`。

然而最简便的答案是`del nums[i]`，可以直接删除列表中的值。