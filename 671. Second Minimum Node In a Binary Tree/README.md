# 671. Second Minimum Node In a Binary Tree

## Solution

带剪枝的宽搜。

如果不带剪枝的话就是用宽搜遍历整个树，然后找到比`root.val`大的最小的数，因为`root.val`就是树中最小的数。
剪枝的方法是如果当前已经有临时解了，那么如果当前访问的节点比`root.val`大，那么后面的孩子就不用访问了。

Test Cases比较松。